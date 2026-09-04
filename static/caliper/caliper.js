/* Dial Caliper Practice — mrwillingham.com
   Builds the caliper as SVG and animates it. No dependencies.

   Kinematics: the slider assembly (right jaw, index, body, dial) is fixed on
   screen. The beam and the left jaw are one piece and slide, so the scale
   travels under a stationary index — the way a caliper looks when you hold it
   by the slider. Everything below is derived from two animated numbers:
   the displayed cube size and the mode blend (0 = total width, 1 = one cube). */

(function () {
  'use strict';

  // ---------------------------------------------------------------- geometry
  var PPI    = 175;      // px per inch of jaw opening
  var VW     = 1010, VH = 790;
  var XI     = 380;      // right jaw face = index = screen datum (fixed)
  var BEAM_T = 200, BEAM_B = 300;   // thick beam, like the real tool
  var JAW_B  = 620;
  var OBJ_Y  = JAW_B - 16;          // object bottom in total-width mode
  var DX     = XI + 165, DY = (BEAM_T + BEAM_B) / 2, DR = 118;   // dial sits over the beam
  var JAW_TIP = BEAM_T - 150;       // both inside jaws end at the same height
  var DUR    = 700;                 // animation length, ms

  var PALETTE = [
    { name: 'red',     fill: '#E4322B', edge: '#A81F1A' },
    { name: 'orange',  fill: '#F5821F', edge: '#B85A08' },
    { name: 'amber',   fill: '#FFC20E', edge: '#B8860A' },
    { name: 'green',   fill: '#2FB457', edge: '#1B7A39' },
    { name: 'teal',    fill: '#00A9A5', edge: '#00726F' },
    { name: 'blue',    fill: '#2D7DD2', edge: '#1B5C9E' },
    { name: 'violet',  fill: '#7B4FD8', edge: '#54329B' },
    { name: 'magenta', fill: '#E5399B', edge: '#A81E6D' }
  ];

  var SVGNS = 'http://www.w3.org/2000/svg';

  function el(tag, attrs, parent) {
    var n = document.createElementNS(SVGNS, tag), k;
    if (attrs) { for (k in attrs) { if (attrs.hasOwnProperty(k)) n.setAttribute(k, attrs[k]); } }
    if (parent) { parent.appendChild(n); }
    return n;
  }
  function txt(parent, x, y, str, attrs) {
    var t = el('text', attrs || {}, parent);
    t.setAttribute('x', x); t.setAttribute('y', y);
    t.textContent = str;
    return t;
  }

  /* Outer (outside-measurement) jaw. face = x of the measuring face; sign +1 for
     the fixed jaw (body to the left), -1 for the slider jaw (mirrored).
     Shape follows the classic textbook drawing: a small relief step under the
     beam, a straight measuring face all the way to the point, a 45-degree bevel
     at the tip, and one long taper up the outside back to the full body. */
  function jawPath(face, sign) {
    var o = -sign * 56, n = -sign * 10, b = -sign * 28;
    return 'M' + (face + o) + ' ' + BEAM_B +
           ' L' + (face + n) + ' ' + BEAM_B +
           ' L' + (face + n) + ' ' + (BEAM_B + 22) +
           ' L' + face + ' ' + (BEAM_B + 22) +
           ' L' + face + ' ' + JAW_B +
           ' L' + (face + b) + ' ' + (JAW_B - 28) +
           ' L' + (face + o) + ' ' + (BEAM_B + 50) + ' Z';
  }
  /* The lapped measuring surface near the tip, drawn lighter. */
  function jawFace(face, sign) {
    var w = -sign * 11;
    return 'M' + face + ' ' + (JAW_B - 100) + ' h' + w + ' v86 h' + (-w) + ' z';
  }
  /* Inside-measurement jaw above the beam: a wedge whose point is at the top
     OUTER corner, so the outer edges are the measuring faces. xo = outer edge x. */
  function upperJaw(xo, y, sign) {
    var h = y - JAW_TIP;
    return 'M' + xo + ' ' + y + ' h' + (sign * 34) + ' v-' + Math.round(h * 0.4) +
           ' L' + xo + ' ' + JAW_TIP + ' Z';
  }
  function upperFace(xo, y, sign) {
    var h = y - JAW_TIP;
    return 'M' + xo + ' ' + (y - 16) + ' h' + (sign * 8) + ' v-' + Math.round(h * 0.6) +
           ' h' + (-sign * 8) + ' z';
  }

  // ---------------------------------------------------------------- build svg
  var wrap = document.getElementById('dc-stage-wrap');
  var svg  = el('svg', {
    viewBox: '0 0 ' + VW + ' ' + VH,
    preserveAspectRatio: 'xMidYMid meet',
    'aria-hidden': 'true', focusable: 'false'
  }, wrap);

  var defs = el('defs', null, svg);
  function grad(id, x2, y2, stops) {
    var g = el('linearGradient', { id: id, x1: '0', y1: '0', x2: x2, y2: y2 }, defs), i;
    for (i = 0; i < stops.length; i++) {
      el('stop', { offset: stops[i][0], 'stop-color': stops[i][1] }, g);
    }
  }
  grad('dcSteel', '0', '1', [[0, '#f4f6f9'], [0.42, '#d6dce3'], [0.52, '#bcc4ce'], [1, '#e6eaf0']]);
  grad('dcSteel2', '1', '1', [[0, '#eaeef3'], [1, '#b4bcc7']]);
  grad('dcFace', '0', '1', [[0, '#ffffff'], [1, '#eef1f5']]);
  var clip = el('clipPath', { id: 'dcClip' }, defs);
  el('rect', { x: 0, y: 0, width: VW, height: VH }, clip);

  var root = el('g', { 'clip-path': 'url(#dcClip)' }, svg);

  /* --- the object: drawn first so the jaw faces overlap its edges --- */
  var gObj = el('g', null, root);
  var cubes = [el('rect', { 'stroke-width': 3 }, gObj),
               el('rect', { 'stroke-width': 3 }, gObj),
               el('rect', { 'stroke-width': 3 }, gObj)];

  /* --- beam assembly: left jaw + beam + scale, all one moving piece --- */
  var gBeam = el('g', null, root);
  el('path', { d: jawPath(0, 1), fill: 'url(#dcSteel2)', stroke: '#8d97a3',
               'stroke-width': 1.6, 'stroke-linejoin': 'round' }, gBeam);
  el('path', { d: jawFace(0, 1), fill: '#eef2f6', stroke: '#9aa4b0', 'stroke-width': 1 }, gBeam);
  el('path', { d: upperJaw(-56, BEAM_T, 1), fill: 'url(#dcSteel2)', stroke: '#8d97a3',
               'stroke-width': 1.4, 'stroke-linejoin': 'round' }, gBeam);
  el('path', { d: upperFace(-56, BEAM_T, 1), fill: '#eef2f6', stroke: '#9aa4b0', 'stroke-width': 1 }, gBeam);
  el('rect', { x: -56, y: BEAM_T, width: 1180, height: BEAM_B - BEAM_T,
               fill: 'url(#dcSteel)', stroke: '#8d97a3' }, gBeam);
  txt(gBeam, -50, BEAM_B - 34, 'in', { 'font-size': 15, fill: '#3c4a59' });
  (function scale() {
    var i = 0, x = 0, inch;
    for (; x <= 1120; i++, x += PPI / 10) {
      inch = (i % 10 === 0);
      el('line', { x1: x, y1: BEAM_B, x2: x, y2: BEAM_B - (inch ? 62 : 18),
                   stroke: '#2b3a4a', 'stroke-width': inch ? 2.4 : 1.3 }, gBeam);
      if (inch) {
        txt(gBeam, x - 6, BEAM_T + 36, String(i / 10),
            { 'text-anchor': 'end', 'font-size': 30, 'font-weight': 700, fill: '#12283f' });
      } else {
        txt(gBeam, x - 4, BEAM_B - 5, String(i % 10),
            { 'text-anchor': 'end', 'font-size': 12, fill: '#3c4a59' });
      }
    }
  }());

  /* --- slider assembly: fixed on screen --- */
  var gSlide = el('g', null, root);
  el('path', { d: jawPath(XI, -1), fill: 'url(#dcSteel2)', stroke: '#8d97a3',
               'stroke-width': 1.6, 'stroke-linejoin': 'round' }, gSlide);
  el('path', { d: jawFace(XI, -1), fill: '#eef2f6', stroke: '#9aa4b0', 'stroke-width': 1 }, gSlide);
  el('rect', { x: XI, y: BEAM_T - 16, width: 300, height: BEAM_B - BEAM_T + 32, rx: 6,
               fill: 'url(#dcSteel2)', stroke: '#8d97a3', 'stroke-width': 1.6 }, gSlide);
  el('rect', { x: XI + 246, y: BEAM_B + 16, width: 50, height: 28, rx: 9,
               fill: '#9aa4b0', stroke: '#79838f' }, gSlide);                 // thumb roller
  el('rect', { x: XI + 258, y: BEAM_T - 34, width: 26, height: 20, rx: 3,
               fill: '#9aa4b0', stroke: '#79838f' }, gSlide);                 // lock screw
  (function knurl() {
    for (var k = 0; k < 6; k++) {
      el('line', { x1: XI + 252 + k * 9, y1: BEAM_B + 19, x2: XI + 252 + k * 9,
                   y2: BEAM_B + 41, stroke: '#7c8792' }, gSlide);
    }
  }());
  /* Inside jaw on the slider. Its measuring edge (the right edge) sits the same
     56 px to the left of the slider face as the fixed inside jaw's measuring edge
     sits to the left of the fixed face, so inside-edge to inside-edge always
     equals the outside-jaw opening, and the two blades meet edge-to-edge at zero.
     A carrier plate above the beam ties it back to the slider body. */
  el('rect', { x: XI - 92, y: BEAM_T - 34, width: 98, height: 32, rx: 3,
               fill: 'url(#dcSteel2)', stroke: '#8d97a3', 'stroke-width': 1.4 }, gSlide);
  el('path', { d: upperJaw(XI - 56, BEAM_T - 34, -1), fill: 'url(#dcSteel2)', stroke: '#8d97a3',
               'stroke-width': 1.4, 'stroke-linejoin': 'round' }, gSlide);
  el('path', { d: upperFace(XI - 56, BEAM_T - 34, -1), fill: '#eef2f6', stroke: '#9aa4b0', 'stroke-width': 1 }, gSlide);
  el('line', { x1: XI, y1: BEAM_T - 18, x2: XI, y2: BEAM_B + 18,
               stroke: '#c0392b', 'stroke-width': 2.5 }, gSlide);
  txt(gSlide, XI + 8, BEAM_B + 38, 'index',
      { 'font-size': 13, 'font-weight': 700, fill: '#c0392b' });

  /* --- dial --- */
  el('circle', { cx: DX, cy: DY, r: DR + 13, fill: '#c8cfd8', stroke: '#8d97a3', 'stroke-width': 2 }, gSlide);
  el('circle', { cx: DX, cy: DY, r: DR, fill: 'url(#dcFace)', stroke: '#5a6673', 'stroke-width': 2 }, gSlide);
  (function dialFace() {
    var k, ang, major, half, r1, r2, rt;
    for (k = 0; k < 100; k++) {
      ang = k * 3.6 * Math.PI / 180;
      major = (k % 10 === 0); half = (k % 5 === 0);
      r2 = DR - 4; r1 = r2 - (major ? 18 : (half ? 12 : 7));
      el('line', { x1: DX + r1 * Math.sin(ang), y1: DY - r1 * Math.cos(ang),
                   x2: DX + r2 * Math.sin(ang), y2: DY - r2 * Math.cos(ang),
                   stroke: '#2b3a4a', 'stroke-width': major ? 2.2 : 1.2 }, gSlide);
      if (major) {
        rt = DR - 36;
        txt(gSlide, DX + rt * Math.sin(ang), DY - rt * Math.cos(ang) + 6, String(k),
            { 'text-anchor': 'middle', 'font-size': 16, 'font-weight': 700, fill: '#2b3a4a' });
      }
    }
  }());
  txt(gSlide, DX, DY - 42, '1 rev = .100 in', { 'text-anchor': 'middle', 'font-size': 12, fill: '#8b98a6' });
  txt(gSlide, DX, DY + 48, '.001 in', { 'text-anchor': 'middle', 'font-size': 13, 'font-weight': 700, fill: '#5b6b7c' });
  var needle = el('g', null, gSlide);
  el('line', { x1: DX, y1: DY + 24, x2: DX, y2: DY - (DR - 14),
               stroke: '#c0392b', 'stroke-width': 4, 'stroke-linecap': 'round' }, needle);
  el('circle', { cx: DX, cy: DY, r: 9, fill: '#2b3a4a' }, gSlide);

  /* --- span marker across whatever is gripped --- */
  var gSpan = el('g', null, root);
  var spanLine = el('line', { stroke: '#ffffff', 'stroke-width': 3 }, gSpan);
  var spanA = el('path', { fill: '#ffffff' }, gSpan);
  var spanB = el('path', { fill: '#ffffff' }, gSpan);

  // ---------------------------------------------------------------- state
  var state = { cube: 0.437, mode: 0, color: 5 };   // mode 0 = total, 1 = one cube
  var shown = { cube: state.cube, mode: state.mode };
  var anim  = null;
  var tries = 0;

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function targetThou() {                       // the answer, in thousandths
    return Math.round(state.cube * (state.mode ? 1 : 2) * 1000);
  }

  function draw() {
    var c = shown.cube * PPI;                   // one cube, px
    var v = shown.cube * (2 - shown.mode);      // caliper reading, inches
    var z = XI - v * PPI;                       // beam zero / left jaw face
    var left = (XI - 2 * c) + shown.mode * c;   // object left edge
    var bot = OBJ_Y + shown.mode * 1.25 * c;    // object bottom edge
    var pal = PALETTE[state.color], i, gy;

    gBeam.setAttribute('transform', 'translate(' + z.toFixed(2) + ',0)');
    needle.setAttribute('transform', 'rotate(' + (v * 3600).toFixed(2) + ' ' + DX + ' ' + DY + ')');

    var pos = [[left, bot - c], [left + c, bot - c], [left, bot - 2 * c]];
    for (i = 0; i < 3; i++) {
      cubes[i].setAttribute('x', pos[i][0].toFixed(2));
      cubes[i].setAttribute('y', pos[i][1].toFixed(2));
      cubes[i].setAttribute('width', c.toFixed(2));
      cubes[i].setAttribute('height', c.toFixed(2));
      cubes[i].setAttribute('fill', pal.fill);
      cubes[i].setAttribute('stroke', pal.edge);
    }

    gy = bot - c / 2 - shown.mode * c;          // centre of the gripped region
    spanLine.setAttribute('x1', z.toFixed(2)); spanLine.setAttribute('y1', gy.toFixed(2));
    spanLine.setAttribute('x2', XI);           spanLine.setAttribute('y2', gy.toFixed(2));
    spanA.setAttribute('d', 'M' + z.toFixed(2) + ' ' + gy.toFixed(2) + ' l13 -6 l0 12 z');
    spanB.setAttribute('d', 'M' + XI + ' ' + gy.toFixed(2) + ' l-13 -6 l0 12 z');
  }

  function ease(t) { return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }

  function animate() {
    var from = { cube: shown.cube, mode: shown.mode };
    var to   = { cube: state.cube, mode: state.mode };
    if (reduce) { shown.cube = to.cube; shown.mode = to.mode; draw(); return; }
    var t0 = null;
    if (anim) { cancelAnimationFrame(anim); }
    function step(ts) {
      if (t0 === null) { t0 = ts; }
      var p = Math.min(1, (ts - t0) / DUR), e = ease(p);
      shown.cube = from.cube + (to.cube - from.cube) * e;
      shown.mode = from.mode + (to.mode - from.mode) * e;
      draw();
      if (p < 1) { anim = requestAnimationFrame(step); } else { anim = null; }
    }
    anim = requestAnimationFrame(step);
  }

  // ---------------------------------------------------------------- controls
  var caption = document.getElementById('dc-caption');
  var guess   = document.getElementById('dc-guess');
  var fb      = document.getElementById('dc-feedback');
  var btnT    = document.getElementById('dc-mode-total');
  var btnO    = document.getElementById('dc-mode-one');
  var dice    = document.getElementById('dc-dice');

  function setFeedback(cls, head, sub) {
    fb.className = 'dc-feedback ' + cls;
    fb.innerHTML = '';
    var s = document.createElement('strong'); s.textContent = head; fb.appendChild(s);
    if (sub) { var p = document.createElement('span'); p.textContent = sub; fb.appendChild(p); }
  }
  function resetRound(msg) {
    tries = 0;
    guess.value = '';
    setFeedback('is-idle', msg, 'Beam first, then the dial.');
  }
  function updateCaption() {
    caption.textContent = state.mode ? 'Measuring: one cube' : 'Measuring: total width (2 cubes)';
    svg.parentNode.setAttribute('aria-label',
      'Dial caliper measuring ' + (state.mode ? 'one cube' : 'the total width') + ' of a three-cube object');
  }

  (function swatches() {
    var host = document.getElementById('dc-swatches'), i, b;
    for (i = 0; i < PALETTE.length; i++) {
      b = document.createElement('button');
      b.type = 'button';
      b.className = 'dc-swatch' + (i === state.color ? ' is-on' : '');
      b.style.background = PALETTE[i].fill;
      b.setAttribute('role', 'radio');
      b.setAttribute('aria-checked', i === state.color ? 'true' : 'false');
      b.setAttribute('aria-label', PALETTE[i].name);
      b.setAttribute('data-i', i);
      b.addEventListener('click', function () {
        var n = +this.getAttribute('data-i'), all = host.querySelectorAll('.dc-swatch'), k;
        state.color = n;
        for (k = 0; k < all.length; k++) {
          all[k].classList.toggle('is-on', k === n);
          all[k].setAttribute('aria-checked', k === n ? 'true' : 'false');
        }
        draw();
      });
      host.appendChild(b);
    }
  }());

  function setMode(m) {
    if (state.mode === m) { return; }
    state.mode = m;
    btnT.classList.toggle('is-on', m === 0);
    btnO.classList.toggle('is-on', m === 1);
    btnT.setAttribute('aria-checked', m === 0 ? 'true' : 'false');
    btnO.setAttribute('aria-checked', m === 1 ? 'true' : 'false');
    updateCaption();
    resetRound(m ? 'Jaws re-set on one cube.' : 'Jaws re-set on the total width.');
    animate();
  }
  btnT.addEventListener('click', function () { setMode(0); });
  btnO.addEventListener('click', function () { setMode(1); });

  dice.addEventListener('click', function () {
    var next, was = Math.round(state.cube * 1000);
    do { next = 400 + Math.floor(Math.random() * 401); } while (next === was);   // 0.400–0.800 in
    state.cube = next / 1000;
    dice.classList.remove('is-rolling');
    void dice.offsetWidth;                       // restart the CSS animation
    dice.classList.add('is-rolling');
    resetRound('New size.');
    animate();
  });

  // ---------------------------------------------------------------- checking
  function split(thou) {
    var beam = Math.floor(thou / 100) * 100;
    return 'beam ' + (beam / 1000).toFixed(3) + ' + dial ' + ((thou - beam) / 1000).toFixed(3);
  }
  function check() {
    var raw = guess.value.trim().replace(/["]/g, '');
    var g = parseFloat(raw);
    var target = targetThou();
    if (raw === '' || isNaN(g)) {
      setFeedback('is-bad', 'Type a number.', 'Three decimal places, like 0.512');
      return;
    }
    var got = Math.round(g * 1000), diff = got - target;
    if (diff === 0) {
      setFeedback('is-good', 'Correct — ' + (target / 1000).toFixed(3) + ' in.', split(target));
      return;
    }
    tries++;
    if (tries >= 3) {
      setFeedback('is-bad', 'The answer is ' + (target / 1000).toFixed(3) + ' in.', split(target));
      return;
    }
    var dir = diff > 0 ? 'high' : 'low';
    if (Math.abs(diff) >= 95 && Math.abs(diff % 100) <= 5) {
      setFeedback('is-near', 'Your dial reading is right.',
                  'You are ' + dir + ' by a whole tenth or more — re-read the beam.');
    } else if (Math.abs(diff) <= 10) {
      setFeedback('is-near', 'Very close — a little ' + dir + '.', 'Check the dial again, one mark at a time.');
    } else {
      setFeedback('is-bad', 'Too ' + dir + '.', 'Beam first, then add the dial.');
    }
  }
  document.getElementById('dc-check').addEventListener('click', check);
  guess.addEventListener('keydown', function (e) {
    if (e.key === 'Enter') { e.preventDefault(); check(); }
  });

  // ---------------------------------------------------------------- go
  updateCaption();
  draw();
}());