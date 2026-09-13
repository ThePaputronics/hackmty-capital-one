"use strict";

const slides = [...document.querySelectorAll(".slide")];
const deck = document.querySelector("#deck");
const previous = document.querySelector("#previous");
const next = document.querySelector("#next");
let current = 0;
const opener = window.FredOpener;
const pitchCount = slides.length - 1;

function syncHeaderHeight() {
  document.documentElement.style.setProperty("--header-height", `${document.querySelector(".masthead").offsetHeight}px`);
}
function goToSlide(index, updateHash = true) {
  // Every explicit navigation cancels the previous opener completion callback.
  opener.leave();
  current = Math.max(0, Math.min(index, slides.length - 1));
  const isOpener = slides[current].id === "opener";
  document.body.classList.toggle("intro-mode", isOpener);
  slides.forEach((slide, i) => { slide.hidden = i !== current; });
  previous.disabled = current === 0;
  next.disabled = current === slides.length - 1;
  next.setAttribute("aria-label", isOpener ? "Iniciar animación; durante la animación, pulsar dos veces rápido para saltar" : "Diapositiva siguiente");
  document.querySelector("#slide-counter").textContent = isOpener ? "OPENER" : `${String(current).padStart(2, "0")} / ${String(pitchCount).padStart(2, "0")}`;
  document.querySelector("#progress").style.width = `${current / pitchCount * 100}%`;
  document.querySelectorAll("[data-slide]").forEach(button => {
    if (Number(button.dataset.slide) === current) button.setAttribute("aria-current", "step");
    else button.removeAttribute("aria-current");
  });
  if (updateHash) history.replaceState(null, "", `#${slides[current].id}`);
  deck.scrollTop = 0;
  syncHeaderHeight();
  document.querySelector("#app-status").textContent = slides[current].querySelector("h1").textContent;
  if (isOpener) opener.enter(() => {
    if (current === 0) goToSlide(1);
  });
}
function advance() {
  if (current === 0) opener.advance();
  else goToSlide(current + 1);
}
function fromHash() {
  const index = slides.findIndex(slide => `#${slide.id}` === location.hash);
  goToSlide(index < 0 ? 0 : index, false);
}
previous.addEventListener("click", () => goToSlide(current - 1));
next.addEventListener("click", advance);
window.addEventListener("hashchange", fromHash);
window.addEventListener("resize", syncHeaderHeight);

const dialogs = { overview: document.querySelector("#overview-dialog"), sources: document.querySelector("#sources-dialog") };
for (const [name, dialog] of Object.entries(dialogs)) {
  document.querySelector(`#${name}-button`).addEventListener("click", () => dialog.showModal());
  dialog.querySelector("[data-close]").addEventListener("click", () => dialog.close());
}
document.querySelectorAll("[data-slide]").forEach(button => button.addEventListener("click", () => {
  dialogs.overview.close();
  goToSlide(Number(button.dataset.slide));
  deck.focus({ preventScroll: true });
}));
async function toggleFullscreen() {
  try {
    if (document.fullscreenElement) await document.exitFullscreen();
    else if (document.documentElement.requestFullscreen) await document.documentElement.requestFullscreen();
    else throw new Error("Fullscreen unavailable");
  } catch {
    document.querySelector("#app-status").classList.remove("sr-only");
    document.querySelector("#app-status").textContent = "No se pudo activar pantalla completa. Puedes usar la opción de pantalla completa del navegador.";
  }
}
document.querySelector("#fullscreen-button").addEventListener("click", toggleFullscreen);
document.addEventListener("fullscreenchange", () => {
  document.querySelector("#fullscreen-button").textContent = document.fullscreenElement ? "Salir de pantalla completa" : "Pantalla completa";
  syncHeaderHeight();
});
document.addEventListener("keydown", event => {
  if (event.altKey || event.ctrlKey || event.metaKey || document.querySelector("dialog[open]") || event.target.closest("input, textarea, select, [contenteditable]")) return;
  const key = event.key;
  if (current === 0 && event.repeat) { event.preventDefault(); return; }
  if (["ArrowRight", "PageDown", "ArrowLeft", "PageUp", "Home", "End"].includes(key)) {
    event.preventDefault();
    if (key === "Home") goToSlide(0);
    else if (key === "End") goToSlide(slides.length - 1);
    else if (["ArrowRight", "PageDown"].includes(key)) advance();
    else goToSlide(current - 1);
  } else if (key === " " && !event.target.closest("button,a")) {
    event.preventDefault();
    if (event.shiftKey) goToSlide(current - 1);
    else advance();
  } else if (key.toLowerCase() === "f") { event.preventDefault(); toggleFullscreen(); }
  else if (key.toLowerCase() === "i") { event.preventDefault(); dialogs.overview.showModal(); }
});
syncHeaderHeight();
fromHash();
