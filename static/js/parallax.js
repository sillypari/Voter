// Subtle parallax by mouse and scroll (very small offsets). Respects reduced-motion.
(function () {
  const prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReduced) return; // do nothing if user prefers reduced motion

  const root = document.querySelector('.parallax-3d');
  if (!root) return;

  const layers = Array.from(root.querySelectorAll('.layer'));
  if (!layers.length) return;

  // Parallax factors (smaller is more subtle)
  const factors = [0.6, 0.4, 0.25];

  let mx = 0, my = 0; // mouse target
  let sx = 0, sy = 0; // smoothed

  function onMouseMove(e) {
    const cx = window.innerWidth / 2;
    const cy = window.innerHeight / 2;
    mx = (e.clientX - cx) / cx; // -1..1
    my = (e.clientY - cy) / cy; // -1..1
  }

  window.addEventListener('mousemove', onMouseMove, { passive: true });

  // Scroll factor adds a tiny vertical drift
  function getScrollRatio() {
    const max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    return window.scrollY / max; // 0..1
  }

  function tick() {
    // ease mouse
    sx += (mx - sx) * 0.04;
    sy += (my - sy) * 0.04;

    const sr = getScrollRatio();

    layers.forEach((el, i) => {
      const f = factors[i % factors.length];
      const tx = sx * 6 * f;  // max ~6px * factor
      const ty = sy * 6 * f + sr * 8 * f; // small scroll influence
      el.style.transform = `translate3d(${tx}px, ${ty}px, 0)`;
    });

    requestAnimationFrame(tick);
  }

  requestAnimationFrame(tick);
})();
