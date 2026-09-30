"""Adds the looping SF Opener intro to the SF case study (SF/index.html).

Re-runnable: always starts from the page as it was just before the intro was added
(BASE, the parent of commit 5f0dc18), so running it twice never stacks edits. The page is a single-file bundle: its React JSX lives gzip+base64
inside <script type="__bundler/manifest"> (asset 05706c89-...), so the JSX is decoded,
patched and packed back.

Video assets it expects in SF/assets/video: sf-opener-{1080,720}.mp4 + sf-opener-poster.jpg (landscape)
and sf-opener-mobile-{1080,720}.mp4 + sf-opener-mobile-poster.jpg (portrait, used on tall screens)
"""
import base64, gzip, json, re, subprocess, sys, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGE = 'SF/index.html'
JSX_ID = '05706c89-902f-405f-9fc1-76e988a3ee42'
BASE = '5f0dc18^'   # the SF page just before the intro

src = subprocess.run(['git', 'show', BASE + ':' + PAGE], cwd=ROOT, capture_output=True, check=True).stdout.decode('utf-8')

m = re.search(r'(<script type="__bundler/manifest">)(.*?)(</script>)', src, re.S)
man = json.loads(m.group(2))
asset = man[JSX_ID]
jsx = gzip.decompress(base64.b64decode(asset['data'])).decode('utf-8')
if 'function OpenerIntro' in jsx:
    sys.exit('BASE already has the intro; point BASE at the commit before it')

def rep(old, new, count=1):
    global jsx
    n = jsx.count(old)
    if n != count:
        sys.exit('patch anchor found %d times (wanted %d): %r' % (n, count, old[:80]))
    jsx = jsx.replace(old, new)

INTRO = r'''
/* Landing intro. The SF Opener clip loops full-screen; the first scroll freezes it on the
   logo (the clip's first frame, its mid hold and its last frame are all that exact still)
   and the logo glides onto the hero collage's logo tile while the page slides into place.
   Scrolling back to the top restarts the loop from the logo, so the handoff is seamless. */
const OPENER_STILL = [[0, 0.14], [2.40, 2.84], [7.78, 99]];   /* seconds where the frame is the logo still */
const OPENERS = {
  /* landscape clip: covers the screen, logo capped at 80% of the width */
  wide: { file: 'sf-opener', w: 1920, h: 1080, logo: { x: 581.56, y: 257.21, w: 758.17, h: 566.15 }, fit: 'cover' },
  /* portrait clip for phones: shown whole so every piece of the explosion stays on screen */
  tall: { file: 'sf-opener-mobile', w: 1080, h: 1920, logo: { x: 119.13, y: 645.50, w: 843.19, h: 629.63 }, fit: 'contain' }
};
const pickOpener = () => (innerHeight > innerWidth * 1.1 ? 'tall' : 'wide');
function openerScale(O) {
  const W = innerWidth, H = innerHeight;
  if (O.fit === 'contain') return Math.min(W / O.w, H / O.h);
  return Math.min(Math.max(W / O.w, H / O.h), (0.8 * W) / O.logo.w);
}
function OpenerIntro() {
  const stage = React.useRef(null);
  const back = React.useRef(null);
  const vid = React.useRef(null);
  const logo = React.useRef(null);
  React.useEffect(() => {
    const st = stage.current, bg = back.current, v = vid.current, lg = logo.current;
    const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
    v.muted = true; v.defaultMuted = true;
    v.setAttribute('muted', ''); v.setAttribute('playsinline', ''); v.setAttribute('webkit-playsinline', '');
    let kind = null, O = null;
    function load() {
      kind = pickOpener(); O = OPENERS[kind];
      /* pick the file by the size the frame is actually shown at */
      const hi = O.w * openerScale(O) * (devicePixelRatio || 1) > 0.73 * O.w;
      v.poster = ASSET + 'video/' + O.file + '-poster.jpg';
      v.src = ASSET + 'video/' + O.file + '-' + (hi ? '1080' : '720') + '.mp4';
    }
    load();
    let fit = null, frozen = null, raf = 0;
    const target = () => document.querySelector('.sf-hero-logo');
    const ease = (x) => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2);
    function layout() {
      const W = innerWidth, H = innerHeight;
      const s = openerScale(O);
      const vw = O.w * s, vh = O.h * s, ox = (W - vw) / 2, oy = (H - vh) / 2;
      Object.assign(v.style, { left: ox + 'px', top: oy + 'px', width: vw + 'px', height: vh + 'px' });
      fit = { x: ox + O.logo.x * s, y: oy + O.logo.y * s, w: O.logo.w * s, h: O.logo.h * s };
      Object.assign(lg.style, { width: fit.w + 'px', height: fit.h + 'px' });
    }
    const still = (t) => OPENER_STILL.some(([a, b]) => t >= a && t <= b);
    function freeze() {
      if (frozen === true) return;
      const hard = reduce || frozen === null || still(v.currentTime);
      frozen = true;
      v.pause();
      v.style.transition = lg.style.transition = hard ? 'none' : 'opacity .25s ease';
      v.style.opacity = '0'; lg.style.opacity = '1';
    }
    function resume() {
      if (frozen === false) return;
      frozen = false;
      v.style.transition = lg.style.transition = 'none';
      if (reduce) { v.style.opacity = '0'; lg.style.opacity = '1'; return; }
      try { v.currentTime = 0; } catch (e) {}
      v.style.opacity = '1'; lg.style.opacity = '0';
      const p = v.play(); if (p && p.catch) p.catch(() => { v.style.opacity = '0'; lg.style.opacity = '1'; });
    }
    function frame() {
      raf = 0;
      const t = target();
      if (!t || !fit) return;
      const r = t.getBoundingClientRect();
      const tcx = r.left + r.width / 2, tcy = r.top + r.height / 2;
      /* the scroll at which the logo lands: its tile sits a little above the middle of the screen */
      const end = Math.max(innerHeight * 0.6, scrollY + tcy - innerHeight * 0.55);
      const p = Math.min(1, Math.max(0, scrollY / end));
      if (p <= 0) resume(); else freeze();
      const e = ease(p);
      const cx0 = fit.x + fit.w / 2, cy0 = fit.y + fit.h / 2;
      const cx = cx0 + (tcx - cx0) * e, cy = cy0 + (tcy - cy0) * e;
      const sc = 1 + (t.offsetWidth / fit.w - 1) * e;
      lg.style.transform = 'translate(' + (cx - fit.w / 2) + 'px,' + (cy - fit.h / 2) + 'px) scale(' + sc + ') rotate(' + 4 * e + 'deg)';
      bg.style.opacity = String(1 - Math.min(1, p / 0.55));
      st.style.visibility = p >= 1 ? 'hidden' : 'visible';
      t.style.visibility = p >= 1 ? 'visible' : 'hidden';
    }
    const schedule = () => { if (!raf) raf = requestAnimationFrame(frame); };
    const onResize = () => {
      /* turning the phone swaps clips; the new one starts on the logo still, like the old one */
      if (pickOpener() !== kind) { const was = frozen; load(); frozen = null; if (was === false) resume(); else freeze(); }
      layout(); schedule();
    };
    layout();
    frame();
    addEventListener('scroll', schedule, { passive: true });
    addEventListener('resize', onResize);
    /* the collage mounts and its images load after us; keep the landing spot current */
    const settle = setInterval(schedule, 250);
    setTimeout(() => clearInterval(settle), 4000);
    return () => {
      removeEventListener('scroll', schedule);
      removeEventListener('resize', onResize);
      clearInterval(settle);
      cancelAnimationFrame(raf);
    };
  }, []);
  return (
    <React.Fragment>
      <section className="sf-intro" aria-label="Smoker Friendly logo animation" style={{ height: '100vh', background: 'var(--surface-page)' }} />
      <div ref={stage} className="sf-intro-stage" aria-hidden="true" style={{ position: 'fixed', inset: 0, zIndex: 120, pointerEvents: 'none', overflow: 'hidden' }}>
        <div ref={back} style={{ position: 'absolute', inset: 0, background: '#ffffff' }} />
        <video ref={vid} loop playsInline preload="auto" style={{ position: 'absolute', display: 'block', maxWidth: 'none', background: '#ffffff' }} />
        <img ref={logo} src={ASSET + 'logos/smoker-friendly-logo-color.svg'} alt="" style={{ position: 'absolute', left: 0, top: 0, maxWidth: 'none', opacity: 0, transformOrigin: '50% 50%', willChange: 'transform' }} />
      </div>
    </React.Fragment>
  );
}
'''

# 1. the component, just ahead of the page root
rep('function PortfolioPage() {', INTRO.lstrip('\n') + '\nfunction PortfolioPage() {')
# 2. mounted first, before the nav and hero
rep('      <NavBar />\n      <Hero />', '      <OpenerIntro />\n      <NavBar />\n      <Hero />')
# 3. the collage's logo tile is the landing spot
rep("        <img src={ASSET + 'logos/smoker-friendly-logo-color.svg'} alt=\"Smoker Friendly logo\" />\n      </button>\n    </React.Fragment>",
    "        <img className=\"sf-hero-logo\" src={ASSET + 'logos/smoker-friendly-logo-color.svg'} alt=\"Smoker Friendly logo\" />\n      </button>\n    </React.Fragment>")

data = gzip.compress(jsx.encode('utf-8'), mtime=0)
asset['data'] = base64.b64encode(data).decode('ascii')
block = json.dumps(man).replace('</', '<\\/')
out = src[:m.start(2)] + block + src[m.end(2):]
open(os.path.join(ROOT, PAGE), 'w', encoding='utf-8').write(out)
print('wrote', PAGE, len(out), 'bytes; jsx', len(jsx))
