#!/usr/bin/env bash
set -Eeuo pipefail

readonly AUTHORIZED_ROOT="/srv/hackathon"
readonly DEPLOY_ROOT="${AUTHORIZED_ROOT}/apps/hello-world"
readonly RELEASES_ROOT="${DEPLOY_ROOT}/releases"
readonly RELEASE_SHA="${GITHUB_SHA:?GITHUB_SHA is required}"
readonly RELEASE_DIR="${RELEASES_ROOT}/${RELEASE_SHA}"
readonly HEALTH_URL="http://127.0.0.1:${APP_PORT:-18080}/healthz"

fail() {
  printf 'deploy error: %s\n' "$*" >&2
  exit 1
}

assert_under_root() {
  local candidate="$1"
  case "$candidate" in
    "$AUTHORIZED_ROOT"|"$AUTHORIZED_ROOT"/*) ;;
    *) fail "path is outside authorized root: $candidate" ;;
  esac
}

assert_no_symlink_components() {
  local candidate="$1"
  local current="/"
  local component
  IFS='/' read -r -a components <<< "${candidate#/}"
  for component in "${components[@]}"; do
    current="${current%/}/${component}"
    if [[ -L "$current" ]]; then
      fail "symlink component is not allowed: $current"
    fi
  done
}

assert_under_root "$DEPLOY_ROOT"
assert_under_root "$RELEASE_DIR"
[[ "$RELEASE_SHA" =~ ^[0-9a-f]{40}$ ]] || fail "GITHUB_SHA must be a 40-character lowercase hexadecimal commit"
[[ "$(realpath -e "$AUTHORIZED_ROOT")" == "$AUTHORIZED_ROOT" ]] || fail "authorized root did not resolve exactly"
assert_no_symlink_components "$DEPLOY_ROOT"

command -v sudo >/dev/null || fail "sudo is required"
command -v docker >/dev/null || fail "docker is required"
sudo -n docker version >/dev/null || fail "runner cannot access Docker with non-interactive sudo"
sudo -n docker compose version >/dev/null || fail "Docker Compose is unavailable"

mkdir -p "$RELEASE_DIR"
cp Dockerfile compose.yaml "$RELEASE_DIR/"
cp -R deploy site "$RELEASE_DIR/"

previous_tag=""
if [[ -f "$DEPLOY_ROOT/current-tag" ]]; then
  previous_tag="$(<"$DEPLOY_ROOT/current-tag")"
fi

rollback() {
  trap - ERR
  if [[ -n "$previous_tag" ]]; then
    printf 'Health check failed; rolling back to %s\n' "$previous_tag" >&2
    APP_TAG="$previous_tag" sudo -n --preserve-env=APP_TAG,BIND_ADDRESS,APP_PORT \
      docker compose --project-directory "$DEPLOY_ROOT" -f "$DEPLOY_ROOT/compose.yaml" up -d --no-build --remove-orphans
  else
    printf 'Health check failed and no previous release exists; stopping failed service\n' >&2
    sudo -n docker compose --project-directory "$DEPLOY_ROOT" -f "$DEPLOY_ROOT/compose.yaml" down
  fi
}
trap rollback ERR

cp "$RELEASE_DIR/compose.yaml" "$DEPLOY_ROOT/compose.yaml"
APP_TAG="$RELEASE_SHA" sudo -n --preserve-env=APP_TAG,BIND_ADDRESS,APP_PORT \
  docker compose --project-directory "$RELEASE_DIR" -f "$DEPLOY_ROOT/compose.yaml" build --pull web
APP_TAG="$RELEASE_SHA" sudo -n --preserve-env=APP_TAG,BIND_ADDRESS,APP_PORT \
  docker compose --project-directory "$DEPLOY_ROOT" -f "$DEPLOY_ROOT/compose.yaml" up -d --no-build --remove-orphans

for attempt in {1..12}; do
  if curl --fail --silent --show-error "$HEALTH_URL" >/dev/null; then
    printf '%s\n' "$RELEASE_SHA" > "$DEPLOY_ROOT/current-tag"
    trap - ERR
    printf 'Deployment healthy at %s\n' "$HEALTH_URL"
    exit 0
  fi
  sleep 5
done

fail "health check did not pass after 60 seconds"
