import * as THREE from "./vendor/three/three.module.js";

const ATLAS_WIDTH = 2048;
const ATLAS_HEIGHT = 1024;

const backgroundVertex = `
  varying vec2 vUv;
  void main() { vUv = uv; gl_Position = vec4(position.xy, 0.0, 1.0); }
`;
const backgroundFragment = `
  precision highp float;
  uniform float uProgress;
  uniform float uTime;
  uniform vec2 uResolution;
  uniform vec2 uMouse;
  uniform float uMousePower;
  varying vec2 vUv;
  void main() {
    gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
  }
`;

const textVertex = `
  uniform float uTime;
  uniform float uProgress;
  uniform float uScale;
  uniform vec2 uMouse;
  uniform float uMousePower;
  varying vec2 vUv;
  varying float vLens;
  void main() {
    vUv = uv;
    vec3 p = position * uScale;
    vec2 delta = p.xy - uMouse;
    float distance = length(delta);
    float lens = exp(-distance * distance / 42000.0) * uMousePower;
    vec2 direction = delta / max(distance, 1.0);
    p.xy += direction * lens * 32.0;
    p.y += sin(p.x * 0.02 + uTime * 3.0) * lens * 13.0;
    float ignition = sin(clamp(uProgress / 0.22, 0.0, 1.0) * 3.141593);
    p.x += sin(p.y * 0.035 + uTime * 7.0) * ignition * 11.0;
    p.y += sin(p.x * 0.009 + uTime * 4.0) * ignition * 22.0;
    vLens = lens;
    gl_Position = projectionMatrix * modelViewMatrix * vec4(p, 1.0);
  }
`;
const textFragment = `
  precision highp float;
  uniform sampler2D uTexture;
  uniform float uProgress;
  uniform float uTarget;
  uniform float uTime;
  varying vec2 vUv;
  varying float vLens;
  void main() {
    float alpha = texture2D(uTexture, vUv).a;
    float sourceFade = 1.0 - smoothstep(0.035, 0.19, uProgress);
    float targetFade = smoothstep(0.71, 0.85, uProgress);
    alpha *= mix(sourceFade, targetFade, uTarget);
    if (alpha < 0.002) discard;
    vec3 color = mix(vec3(0.125, 0.122, 0.114), vec3(0.53, 0.34, 0.10), vLens * 0.75);
    color += vec3(0.07, 0.045, 0.02) * vLens * sin(vUv.x * 11.0 + uTime);
    color = mix(color, vec3(0.125, 0.122, 0.114), uTarget * 0.35);
    gl_FragColor = vec4(color, alpha);
  }
`;
const particleVertex = `
  uniform float uProgress;
  uniform float uTime;
  uniform float uScale;
  uniform float uPixelRatio;
  uniform vec2 uResolution;
  uniform vec2 uMouse;
  uniform float uMousePower;
  attribute vec3 aTarget;
  attribute vec3 aSeed;
  attribute float aCore;
  varying float vAlpha;
  varying float vHeat;
  varying float vSeed;
  const float PI = 3.14159265359;
  void main() {
    float stagger = aSeed.z * 0.035;
    float travel = smoothstep(0.09 + stagger, 0.76 + stagger, uProgress);
    float storm = sin(travel * PI);
    float twist = travel * PI * 2.0 + aSeed.x * PI * 2.0;
    float core = max(aCore, 0.0);
    vec3 p = mix(position, aTarget, travel) * uScale;
    float extent = mix(1.0, 0.24, core);
    float radius = (90.0 + aSeed.y * 360.0) * uScale;
    p.x += cos(twist) * radius * storm * extent * 2.4;
    p.y += sin(twist * 1.35 + aSeed.z * 4.0) * radius * storm * extent * 1.35;
    p.z += sin(twist + aSeed.y * 4.0) * storm * 120.0;
    p.y += sin(p.x * 0.013 + travel * 12.0 + aSeed.z * 3.0) * storm * 28.0;
    p.x += sin(p.y * 0.018 + uTime * 2.0) * storm * 18.0;
    vec2 delta = p.xy - uMouse;
    float distance = length(delta);
    float lens = exp(-distance * distance / 46000.0) * uMousePower;
    p.xy += delta / max(distance, 1.0) * lens * (42.0 + storm * 38.0);
    p.y += sin(p.x * 0.02 + uTime * 3.0) * lens * 13.0;
    float reveal = smoothstep(0.025, 0.10, uProgress);
    float finish = 1.0 - smoothstep(0.77, 0.93, uProgress);
    vAlpha = reveal * finish;
    if (aCore < -0.5) vAlpha *= storm * 0.72;
    vAlpha *= mix(0.46, 1.0, core);
    vHeat = storm * (0.35 + aSeed.x * 0.65) + lens * 0.45;
    vSeed = aSeed.y;
    gl_PointSize = min(20.0, (1.8 + aSeed.z * 1.6 + storm * (2.3 + aSeed.y * 3.0)) * uPixelRatio);
    gl_Position = projectionMatrix * modelViewMatrix * vec4(p, 1.0);
  }
`;
const particleFragment = `
  precision highp float;
  varying float vAlpha;
  varying float vHeat;
  varying float vSeed;
  void main() {
    vec2 point = gl_PointCoord - 0.5;
    float d = length(point) * 2.0;
    if (d > 1.0 || vAlpha < 0.001) discard;
    float halo = pow(max(0.0, 1.0 - d), 2.8);
    float core = exp(-d * d * 38.0);
    vec3 cool = mix(vec3(0.12, 0.25, 0.34), vec3(0.28, 0.15, 0.38), vSeed);
    vec3 gold = vec3(0.63, 0.42, 0.12);
    vec3 color = mix(gold, cool, smoothstep(0.3, 0.85, vSeed) * vHeat);
    color = mix(color, vec3(0.20, 0.18, 0.15), core * 0.8);
    gl_FragColor = vec4(color, (halo * 0.55 + core * 0.75) * vAlpha);
  }
`;

function seededRandom(seed = 17431) {
  return () => {
    seed = (seed * 1664525 + 1013904223) >>> 0;
    return seed / 4294967296;
  };
}

// Rasterize individual glyphs so F/r/E/D retain their own destinations.
function rasterize(target, compact) {
  const canvas = document.createElement("canvas");
  canvas.width = ATLAS_WIDTH;
  canvas.height = ATLAS_HEIGHT;
  const context = canvas.getContext("2d", { willReadFrequently: true });
  if (!context) throw new Error("Canvas text sampling is unavailable");
  const fontSize = target ? 360 : compact ? 218 : 158;
  context.font = `400 ${fontSize}px "Cormorant Garamond", Georgia, serif`;
  context.fillStyle = "white";
  context.textBaseline = "alphabetic";
  const lines = target ? ["F.R.E.D"] : compact ? ["Fraud", "Detection", "Engine"] : ["Fraud Detection Engine"];
  const baseline = target ? 633 : compact ? 300 : 569;
  const groups = { F: [], R: [], E: [], D: [], all: [] };
  let globalIndex = 0;
  for (let lineIndex = 0; lineIndex < lines.length; lineIndex++) {
    const text = lines[lineIndex];
    const tracking = target ? 20 : 0;
    const width = [...text].reduce((sum, char) => sum + context.measureText(char).width, 0) + tracking * (text.length - 1);
    let x = (ATLAS_WIDTH - width) / 2;
    const y = baseline + lineIndex * 263;
    for (let i = 0; i < text.length; i++) {
      const char = text[i];
      const metrics = context.measureText(char);
      const charCanvas = document.createElement("canvas");
      charCanvas.width = Math.ceil(metrics.width + 50);
      charCanvas.height = fontSize + 100;
      const c = charCanvas.getContext("2d", { willReadFrequently: true });
      c.font = context.font;
      c.fillStyle = "white";
      c.fillText(char, 25, fontSize);
      context.fillText(char, x, y);
      const pixels = c.getImageData(0, 0, charCanvas.width, charCanvas.height).data;
      let group = null;
      if (target && "FRED".includes(char)) group = char;
      if (!target) {
        if (globalIndex === 0) group = "F";
        if (globalIndex === 1) group = "R";
        if (char === "D") group = "D";
        if (char === "E") group = "E";
      }
      for (let py = 0; py < charCanvas.height; py += 3) {
        for (let px = 0; px < charCanvas.width; px += 3) {
          if (pixels[(py * charCanvas.width + px) * 4 + 3] < 100) continue;
          const position = [x + px - 25 - ATLAS_WIDTH / 2, ATLAS_HEIGHT / 2 - (y + py - fontSize), 0];
          groups.all.push(position);
          if (group) groups[group].push(position);
        }
      }
      x += metrics.width + tracking;
      globalIndex++;
    }
    globalIndex++;
  }
  if (!groups.all.length) throw new Error("Text atlas contains no pixels");
  const texture = new THREE.CanvasTexture(canvas);
  texture.minFilter = THREE.LinearFilter;
  texture.magFilter = THREE.LinearFilter;
  texture.generateMipmaps = false;
  return { texture, groups };
}

export function createIntroScene(canvas) {
  const renderer = new THREE.WebGLRenderer({ canvas, alpha: false, antialias: true, powerPreference: "high-performance" });
  renderer.setClearColor(0xffffff, 1);
  const scene = new THREE.Scene();
  const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, -1000, 1000);
  const uniforms = {
    uProgress: { value: 0 }, uTime: { value: 0 }, uScale: { value: 1 },
    uResolution: { value: new THREE.Vector2(1, 1) },
    uMouse: { value: new THREE.Vector2(10000, 10000) },
    uMousePower: { value: 0 }, uPixelRatio: { value: 1 }
  };
  let generated = [];
  let textures = [];
  let compact = null;
  let disposed = false;
  let shaderFailure = null;
  renderer.debug.onShaderError = () => { shaderFailure = new Error("Intro shaders could not be compiled"); };
  const backgroundGeometry = new THREE.PlaneGeometry(2, 2);
  const backgroundMaterial = new THREE.ShaderMaterial({ uniforms, vertexShader: backgroundVertex, fragmentShader: backgroundFragment, depthTest: false, depthWrite: false });
  const background = new THREE.Mesh(backgroundGeometry, backgroundMaterial);
  background.frustumCulled = false;
  background.renderOrder = 0;
  scene.add(background);

  function clearGenerated() {
    for (const object of generated) {
      scene.remove(object);
      object.geometry.dispose();
      object.material.dispose();
    }
    textures.forEach(texture => texture.dispose());
    generated = [];
    textures = [];
  }
  function build(isCompact) {
    clearGenerated();
    const source = rasterize(false, isCompact);
    const target = rasterize(true, isCompact);
    textures = [source.texture, target.texture];
    for (const [atlas, mode] of [[source, 0], [target, 1]]) {
      const material = new THREE.ShaderMaterial({
        uniforms: { ...uniforms, uTexture: { value: atlas.texture }, uTarget: { value: mode } },
        vertexShader: textVertex, fragmentShader: textFragment,
        transparent: true, depthTest: false, depthWrite: false
      });
      const mesh = new THREE.Mesh(new THREE.PlaneGeometry(ATLAS_WIDTH, ATLAS_HEIGHT, 160, 48), material);
      mesh.renderOrder = mode ? 4 : 2;
      mesh.frustumCulled = false;
      scene.add(mesh);
      generated.push(mesh);
    }
    const random = seededRandom();
    const count = isCompact ? 10000 : 20000;
    const positions = new Float32Array(count * 3);
    const targets = new Float32Array(count * 3);
    const seeds = new Float32Array(count * 3);
    const core = new Float32Array(count);
    const letters = ["F", "R", "E", "D"];
    for (let i = 0; i < count; i++) {
      const isCore = i % 5 !== 0;
      const letter = letters[i % 4];
      const sourcePixels = isCore && source.groups[letter].length ? source.groups[letter] : source.groups.all;
      const targetPixels = isCore ? target.groups[letter] : target.groups.all;
      const a = sourcePixels[Math.floor(random() * sourcePixels.length)];
      const b = targetPixels[Math.floor(random() * targetPixels.length)];
      positions.set(a, i * 3);
      targets.set(b, i * 3);
      seeds.set([random(), random(), random()], i * 3);
      core[i] = isCore ? 1 : 0;
      if (i > count * 0.94) {
        positions[i * 3] = (random() - 0.5) * 2400;
        positions[i * 3 + 1] = (random() - 0.5) * 1100;
        core[i] = -1;
      }
    }
    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute("aTarget", new THREE.BufferAttribute(targets, 3));
    geometry.setAttribute("aSeed", new THREE.BufferAttribute(seeds, 3));
    geometry.setAttribute("aCore", new THREE.BufferAttribute(core, 1));
    const particles = new THREE.Points(geometry, new THREE.ShaderMaterial({
      uniforms, vertexShader: particleVertex, fragmentShader: particleFragment,
      transparent: true, depthTest: false, depthWrite: false, blending: THREE.NormalBlending
    }));
    particles.frustumCulled = false;
    particles.renderOrder = 3;
    generated.push(particles);
    scene.add(particles);
  }
  function resize(width, height) {
    if (disposed || width < 1 || height < 1) return;
    const nextCompact = width < 700;
    const ratio = Math.min(window.devicePixelRatio || 1, nextCompact ? 1.5 : 1.75);
    renderer.setPixelRatio(ratio);
    renderer.setSize(width, height, false);
    camera.left = -width / 2;
    camera.right = width / 2;
    camera.top = height / 2;
    camera.bottom = -height / 2;
    camera.updateProjectionMatrix();
    uniforms.uResolution.value.set(width, height);
    uniforms.uPixelRatio.value = ratio;
    uniforms.uScale.value = Math.min(width / ATLAS_WIDTH * (nextCompact ? 1.48 : 0.97), height / ATLAS_HEIGHT * 0.85);
    if (nextCompact !== compact) {
      compact = nextCompact;
      build(compact);
    }
  }
  function render({ progress, time, mouseX, mouseY, mousePower }) {
    if (disposed) return;
    uniforms.uProgress.value = progress;
    uniforms.uTime.value = time;
    uniforms.uMouse.value.set(mouseX, mouseY);
    uniforms.uMousePower.value = mousePower;
    renderer.render(scene, camera);
    if (shaderFailure) throw shaderFailure;
  }
  function dispose() {
    if (disposed) return;
    disposed = true;
    clearGenerated();
    backgroundGeometry.dispose();
    backgroundMaterial.dispose();
    renderer.dispose();
  }
  try {
    resize(canvas.clientWidth, canvas.clientHeight);
    renderer.compile(scene, camera);
    if (shaderFailure) throw shaderFailure;
  } catch (error) { dispose(); throw error; }
  return { render, resize, dispose };
}
