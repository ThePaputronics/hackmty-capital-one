"use strict";

// The opener owns its animation clock; presentation navigation owns slide changes.
(() => {
  const DURATION_MS = 5000;
  const DOUBLE_PRESS_MS = 420;
  const stage = document.querySelector("#opener");
  const canvas = document.querySelector("#intro-canvas");
  const hint = document.querySelector("#intro-hint");
  const fallbackMessage = document.querySelector("#intro-fallback-message");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  let active = false;
  let state = "idle";
  let elapsed = 0;
  let previousTime = 0;
  let lastSkipPress = null;
  let frame = 0;
  let scene = null;
  let loading = null;
  let failed = false;
  let printing = false;
  let paused = false;
  let complete = null;
  let mouse = { x: 0, y: 0, power: 0, targetX: 0, targetY: 0, targetPower: 0 };

  function setState(value) {
    state = value;
    stage.dataset.state = value;
  }
  function lightweight(reason) {
    failed = true;
    stage.classList.remove("intro-rendered");
    stage.dataset.renderer = "fallback";
    if (scene) scene.dispose();
    scene = null;
    fallbackMessage.textContent = "Animación simplificada. Los controles siguen disponibles.";
    if (reason) console.warn("F.R.E.D opener: using the lightweight fallback.", reason);
  }
  function render(now, delta = 0) {
    const progress = elapsed / DURATION_MS;
    const blend = 1 - Math.exp(-delta / 85);
    mouse.x += (mouse.targetX - mouse.x) * blend;
    mouse.y += (mouse.targetY - mouse.y) * blend;
    mouse.power += (mouse.targetPower - mouse.power) * blend;
    stage.style.setProperty("--intro-progress", String(progress));
    stage.dataset.progress = progress.toFixed(3);
    const phase = state !== "running" ? "idle" : progress < 0.18 ? "ignite" : progress < 0.58 ? "scatter" : progress < 0.84 ? "assemble" : "resolve";
    if (stage.dataset.phase !== phase) stage.dataset.phase = phase;
    if (scene && !reduceMotion.matches) {
      try {
        scene.render({ progress, time: now / 1000, mouseX: mouse.x, mouseY: mouse.y, mousePower: mouse.power });
        stage.classList.add("intro-rendered");
        stage.dataset.renderer = "webgl";
      } catch (error) { lightweight(error); }
    }
  }
  function finish() {
    if (!active || state !== "running") return;
    setState("finished");
    stopLoop();
    hint.textContent = "Pulsa → para continuar";
  }
  function tick(now) {
    frame = 0;
    if (!active || paused) return;
    const delta = previousTime ? Math.max(0, now - previousTime) : 0;
    previousTime = now;
    if (state === "running") elapsed = Math.min(DURATION_MS, elapsed + delta);
    render(now, delta);
    if (state === "running" && elapsed >= DURATION_MS) { finish(); return; }
    frame = requestAnimationFrame(tick);
  }
  function startLoop() {
    if (active && !paused && !frame) {
      previousTime = performance.now();
      frame = requestAnimationFrame(tick);
    }
  }
  function stopLoop() {
    if (frame) cancelAnimationFrame(frame);
    frame = 0;
    previousTime = 0;
  }
  function syncPaused() {
    paused = document.hidden || printing || Boolean(document.querySelector("dialog[open]"));
    if (paused) stopLoop();
    else startLoop();
  }
  async function prepare() {
    if (loading || scene || failed || reduceMotion.matches) return;
    loading = (async () => {
      // Bundled locally: no CDN request or remote runtime dependency.
      const module = await import("./intro-scene.js");
      await Promise.race([
        document.fonts.load('400 158px "Cormorant Garamond"'),
        new Promise(resolve => setTimeout(resolve, 1200))
      ]);
      if (failed || reduceMotion.matches) return;
      scene = module.createIntroScene(canvas);
      if (active) {
        scene.resize(stage.clientWidth, stage.clientHeight);
        render(performance.now());
      }
    })().catch(lightweight).finally(() => { loading = null; });
    await loading;
  }
  function enter(onComplete) {
    active = true;
    complete = onComplete;
    elapsed = 0;
    lastSkipPress = null;
    mouse = { x: 0, y: 0, power: 0, targetX: 0, targetY: 0, targetPower: 0 };
    setState("idle");
    stage.dataset.phase = "idle";
    stage.dataset.progress = "0";
    stage.classList.toggle("intro-reduced", reduceMotion.matches);
    hint.textContent = "Pulsa → para comenzar";
    if (reduceMotion.matches) stage.dataset.renderer = "reduced-motion";
    if (scene) scene.resize(stage.clientWidth, stage.clientHeight);
    render(performance.now());
    syncPaused();
    prepare();
  }
  function leave() {
    active = false;
    complete = null;
    lastSkipPress = null;
    elapsed = 0;
    setState("idle");
    stopLoop();
  }
  function advance(now = performance.now()) {
    if (!active) return false;
    if (state === "idle") {
      elapsed = 0;
      previousTime = now;
      lastSkipPress = null;
      setState("running");
      hint.textContent = "Pulsa → dos veces rápido para saltar";
      startLoop();
    } else if (state === "running") {
      // The launch press does not count toward the in-animation double press.
      if (lastSkipPress !== null && now - lastSkipPress <= DOUBLE_PRESS_MS) finish();
      else lastSkipPress = now;
    } else if (state === "finished") {
      const callback = complete;
      complete = null;
      if (callback) callback();
    }
    return true;
  }
  stage.addEventListener("pointermove", event => {
    if (!active || reduceMotion.matches) return;
    const box = canvas.getBoundingClientRect();
    mouse.targetX = event.clientX - box.left - box.width / 2;
    mouse.targetY = box.height / 2 - (event.clientY - box.top);
    mouse.targetPower = 1;
  });
  stage.addEventListener("pointerleave", () => { mouse.targetPower = 0; });
  canvas.addEventListener("webglcontextlost", event => {
    event.preventDefault();
    lightweight(new Error("WebGL context was lost"));
  });
  const resizeObserver = new ResizeObserver(() => {
    if (!active || !scene) return;
    try { scene.resize(stage.clientWidth, stage.clientHeight); }
    catch (error) { lightweight(error); }
  });
  resizeObserver.observe(stage);
  const dialogObserver = new MutationObserver(syncPaused);
  document.querySelectorAll("dialog").forEach(dialog => dialogObserver.observe(dialog, { attributes: true, attributeFilter: ["open"] }));
  document.addEventListener("visibilitychange", syncPaused);
  window.addEventListener("beforeprint", () => { printing = true; syncPaused(); });
  window.addEventListener("afterprint", () => { printing = false; syncPaused(); });
  reduceMotion.addEventListener("change", () => {
    stage.classList.toggle("intro-reduced", reduceMotion.matches);
    stage.classList.remove("intro-rendered");
    if (reduceMotion.matches) stage.dataset.renderer = "reduced-motion";
    else prepare();
  });
  window.addEventListener("pagehide", () => { stopLoop(); });
  window.addEventListener("pageshow", syncPaused);

  window.FredOpener = {
    enter, leave, advance,
    get status() { return { active, state, progress: elapsed / DURATION_MS, renderer: stage.dataset.renderer, renderLoopActive: Boolean(frame) }; }
  };
})();
