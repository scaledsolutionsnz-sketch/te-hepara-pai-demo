#!/usr/bin/env python3
"""Builds the static pages for te-hepara-pai-demo from shared partials.
Run from the repo root: python3 tools/build.py"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://te-hepara-pai-demo.vercel.app"

# ---------------------------------------------------------------- icons
ICONS = {
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 "cup": '<path d="M4 8h13v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z"/><path d="M17 9h1.5a2.5 2.5 0 0 1 0 5H17"/><path d="M8 3c0 1 1 1 1 2s-1 1-1 2M12 3c0 1 1 1 1 2s-1 1-1 2"/>',
 "child": '<circle cx="12" cy="5" r="2.5"/><path d="M7 10h10M12 10v5m0 0-3 6m3-6 3 6"/>',
 "access": '<circle cx="12" cy="4.5" r="2"/><path d="M5 8.5 12 10l7-1.5M12 10v5m0 0-3.5 6M12 15l3.5 6"/>',
 "car": '<path d="M5 16V11l2-5h10l2 5v5"/><path d="M3 16h18v3H3z"/><circle cx="7.5" cy="13" r="1"/><circle cx="16.5" cy="13" r="1"/>',
 "walk": '<circle cx="13" cy="4" r="2"/><path d="m9 21 2-7 3 3v4M10 9l3-1 3 4h3M8 13l2-4"/>',
 "basket": '<path d="M4 10h16l-1.5 9a2 2 0 0 1-2 1.7h-9A2 2 0 0 1 5.5 19z"/><path d="m8 10 4-6 4 6M9 14v3M12 14v3M15 14v3"/>',
 "heart": '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
 "book": '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 21V5M9 7h6"/>',
 "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 "plus": '<path d="M12 5v14M5 12h14"/>',
 "close": '<path d="M6 6l12 12M18 6 6 18"/>',
 "left": '<path d="M19 12H5M11 6l-6 6 6 6"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "directions": '<path d="m12 3 9 9-9 9-9-9z"/><path d="M9 13v-2h5V9l2.5 2.5L14 14v-2"/>',
 "home": '<path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "story": '<path d="M12 6c-2-1.5-5-2-8-1.5V19c3-.5 6 0 8 1.5 2-1.5 5-2 8-1.5V4.5C17 4 14 4.5 12 6zM12 6v14.5"/>',
 "palette": '<path d="M12 3a9 9 0 1 0 0 18c1.1 0 1.5-.8 1.2-1.6-.4-1 .3-2.4 1.8-2.4H17a4 4 0 0 0 4-4c0-5.5-4-10-9-10z"/><circle cx="7.5" cy="11" r="1"/><circle cx="10" cy="7" r="1"/><circle cx="15" cy="7.5" r="1"/>',
 "hands": '<path d="M7 11V6a1.5 1.5 0 0 1 3 0v5M10 10V4.5a1.5 1.5 0 0 1 3 0V10M13 10V6a1.5 1.5 0 0 1 3 0v6.5M7 11a1.5 1.5 0 0 0-3 0v2a8 8 0 0 0 8 8h1a6 6 0 0 0 6-6v-4"/>',
}

def icon(name, label=None):
    aria = f' role="img" aria-label="{label}"' if label else ' aria-hidden="true"'
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round"{aria}>{ICONS[name]}</svg>')

FB = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.8v3h2.6V21z"/></svg>'
GOOGLE = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M21.6 12.2c0-.7-.1-1.4-.2-2H12v3.8h5.4a4.6 4.6 0 0 1-2 3v2.5h3.2c1.9-1.7 3-4.3 3-7.3z"/><path d="M12 22c2.7 0 5-.9 6.6-2.4l-3.2-2.5c-.9.6-2 1-3.4 1-2.6 0-4.8-1.8-5.6-4.1H3.1v2.6A10 10 0 0 0 12 22z" opacity=".75"/><path d="M6.4 14c-.2-.6-.3-1.3-.3-2s.1-1.4.3-2V7.4H3.1a10 10 0 0 0 0 9.2z" opacity=".55"/><path d="M12 5.9c1.5 0 2.8.5 3.8 1.5l2.9-2.9A10 10 0 0 0 3.1 7.4L6.4 10c.8-2.4 3-4.1 5.6-4.1z" opacity=".9"/></svg>'
STAR = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 2.8 2.8 6 6.5.6-4.9 4.4 1.4 6.4L12 17l-5.8 3.2 1.4-6.4-4.9-4.4 6.5-.6z"/></svg>'

def stars(n, label=None):
    full = int(n)
    out = "".join(STAR for _ in range(full))
    if n - full >= 0.25:
        out += STAR.replace('<svg ', '<svg class="half" ', 1)
    lab = label or f"{n} out of 5 stars"
    return f'<span class="stars" role="img" aria-label="{lab}">{out}</span>'

# ---------------------------------------------------------------- facts
ADDRESS = "131 Cole Street, Masterton"
DIRECTIONS = "https://www.google.com/maps/dir/?api=1&destination=Te+Hepara+Pai+Church%2C+131+Cole+Street%2C+Masterton+5810"
MAPS_EMBED = "https://maps.google.com/maps?q=Te%20Hepara%20Pai%20Church%2C%20131%20Cole%20Street%2C%20Masterton%205810&z=16&output=embed"
GOOGLE_LISTING = "https://maps.google.com/?cid=9561486418656844581"
FACEBOOK = "https://www.facebook.com/search/top?q=Te%20Hepara%20Pai%20Masterton"
TEUPOKO = "https://www.teupoko.org/"
RATING, COUNT = 4.3, 6

PEOPLE = [
    ("Rev'd Emily Bartlett", "Co-priest", "021 053 6731", "+64210536731"),
    ("Rev'd Liz Greville", "Co-priest in charge", "027 474 5200", "+64274745200"),
    ("Deacon Richard Jackson", "Deacon", "027 811 0006", "+64278110006"),
    ("Rev'd Robin Irwin", "Secretary", "027 486 2714", "+64274862714"),
]
MAIN_TEL, MAIN_TEL_TXT = "+64210536731", "021 053 6731"

NAV = [("index.html", "Home"), ("who-we-are.html", "Who we are"), ("atrium.html", "Atrium"),
       ("marae.html", "Te Rangamarie Marae"), ("events.html", "Updates and events")]

# ---------------------------------------------------------------- images
_dims = {}
def dims(name):
    if name not in _dims:
        _dims[name] = Image.open(ROOT / "img" / f"{name}-1920.webp").size
    return _dims[name]

def img(name, alt, sizes="(min-width: 900px) 50vw, 100vw", eager=False, cls="", extra=""):
    w, h = dims(name)
    load = 'fetchpriority="high" loading="eager"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img src="img/{name}-1920.webp" srcset="img/{name}-1080.webp 1080w, img/{name}-1920.webp 1920w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{alt}" {load} decoding="async"{c}{extra}>')

def hero_img(name, alt, eager=False, cls="", extra=""):
    load = 'fetchpriority="high" loading="eager"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img src="img/hero-{name}-2560.webp" srcset="img/hero-{name}-1280.webp 1280w, img/hero-{name}-2560.webp 2560w" '
            f'sizes="100vw" width="2560" height="1440" alt="{alt}" {load} decoding="async"{c}{extra}>')

# ---------------------------------------------------------------- partials
POUTAMA_MARK = ('<svg class="brand-mark" viewBox="0 0 34 34" aria-hidden="true">'
                '<rect width="34" height="34" rx="8" fill="#a3301f"/>'
                '<path d="M6 28v-4h5v-4h5v-4h5v-4h5V8h2v6h-5v4h-5v4h-5v4H8v2z" fill="#f7f2e8"/>'
                '<path d="M23 4h2v6h-2z" fill="#f7f2e8"/></svg>')

def head(title, desc, path, og="te-rangamarie-marae"):
    url = f"{SITE}/{'' if path == 'index.html' else path}"
    return f'''<!doctype html>
<html lang="en-NZ">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/img/{og}-1920.webp">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/site.css?v=5">
'''

CUR = ' aria-current="page"'

def header(active):
    links = "".join(
        f'<li><a href="{h}"{CUR if h == active else ""}>{t}</a></li>' for h, t in NAV)
    mlinks = "".join(
        f'<a href="{h}"{CUR if h == active else ""}>{t}</a>' for h, t in NAV)
    return f'''</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="index.html" aria-label="Te Hepara Pai, home">{POUTAMA_MARK}<span><span class="brand-name">Te Hepara Pai</span><span class="brand-sub">Māori Anglican Church, Masterton</span></span></a>
    <nav aria-label="Main"><ul class="nav-links">{links}</ul></nav>
    <div class="nav-actions">
      <a class="btn btn-primary btn-sm" href="tel:{MAIN_TEL}" aria-label="Call Rev'd Emily Bartlett on {MAIN_TEL_TXT}">{icon("phone")}<span class="call-label">{MAIN_TEL_TXT}</span><span class="sr">Call</span></a>
      <button class="menu-btn" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu">{icon("menu")}</button>
    </div>
  </div>
  <nav id="mobile-menu" class="mobile-menu" aria-label="Mobile">{mlinks}</nav>
</header>
<main id="main">
'''

def contact_section():
    rows = "".join(
        f'<li><span class="who">{n}<span class="role">{r}</span></span>'
        f'<a href="tel:{t}">{icon("phone")}{p}</a></li>' for n, r, p, t in PEOPLE)
    return f'''
<section class="section green" id="contact" aria-labelledby="contact-h">
  <div class="wrap contact-grid">
    <div class="reveal">
      <h2 id="contact-h">Kōrero mai: talk to us</h2>
      <p class="lead">The quickest way to reach us is by phone. Call any of our ministry team with questions about services, Atrium, the marae or visiting for the first time.</p>
      <ul class="people">{rows}</ul>
      <ul class="info-rows">
        <li>{icon("pin")}<span>{ADDRESS} 5810, near Douglas Park School. <a href="{DIRECTIONS}" target="_blank" rel="noopener">Get directions</a></span></li>
        <li>{icon("clock")}<span>Sunday service 9:30 am every week, followed by morning tea</span></li>
      </ul>
      <div class="socials">
        <a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Find Te Hepara Pai on Facebook">{FB}</a>
        <a href="{GOOGLE_LISTING}" target="_blank" rel="noopener" aria-label="Te Hepara Pai on Google Maps">{GOOGLE}</a>
      </div>
    </div>
    <div class="contact-actions reveal">
      <a class="btn btn-primary" href="tel:{MAIN_TEL}">{icon("phone")}<span>Call Rev'd Emily Bartlett<small>{MAIN_TEL_TXT}</small></span></a>
      <a class="btn btn-ghost" href="tel:+64274745200">{icon("phone")}<span>Call Rev'd Liz Greville<small>027 474 5200</small></span></a>
      <a class="btn btn-ghost" href="#" data-gmail data-user="quaylew" data-domain="xtra.co.nz" data-su="Te%20Rangamarie%20Marae%20booking%20enquiry" data-body="Kia%20ora%20Bishop%20Wai%2C%0A%0AI%27d%20like%20to%20enquire%20about%20booking%20Te%20Rangamarie%20Marae.%0A%0ADates%3A%0ANumber%20of%20people%3A%0AType%20of%20gathering%3A%0A%0ANg%C4%81%20mihi%2C">{icon("mail")}<span>Email about a marae booking<small>Bishop Wai Quayle</small></span></a>
      <a class="btn btn-ghost" href="{DIRECTIONS}" target="_blank" rel="noopener">{icon("directions")}<span>Directions to the church<small>{ADDRESS}</small></span></a>
    </div>
  </div>
</section>
<section class="map" aria-label="Map showing Te Hepara Pai Church">
  <div class="wrap"><iframe src="{MAPS_EMBED}" title="Map: Te Hepara Pai Church, 131 Cole Street, Masterton" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</section>
'''

def footer():
    X, L, R = icon('close'), icon('left'), icon('arrow')
    navl = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f'''</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <h2>Te Hepara Pai</h2>
        <p>Part of Te Pihopatanga o Aotearoa | The Maori Anglican Church in New Zealand, in <a href="{TEUPOKO}" target="_blank" rel="noopener" style="padding:0;text-decoration:underline">Te Hui Amorangi ki Te Upoko o te Ika</a>.</p>
        <div class="socials">
          <a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Find Te Hepara Pai on Facebook">{FB}</a>
          <a href="{GOOGLE_LISTING}" target="_blank" rel="noopener" aria-label="Te Hepara Pai on Google Maps">{GOOGLE}</a>
        </div>
      </div>
      <div><h3>Explore</h3><ul>{navl}</ul></div>
      <div><h3>Service times</h3><ul><li>Sunday services: 9:30 am (weekly)</li><li>Atrium: Thursdays, 3:30 pm to 4:45 pm</li><li><a href="events.html">Other services: see Updates and events</a></li></ul></div>
      <div><h3>Find us</h3><ul><li>{ADDRESS} 5810</li><li><a href="{DIRECTIONS}" target="_blank" rel="noopener">Get directions</a></li><li><a href="{GOOGLE_LISTING}" target="_blank" rel="noopener">Leave us a Google review</a></li><li><a href="privacy.html">Privacy</a></li></ul></div>
    </div>
    <div class="footer-base"><span>&copy; <span id="year">2026</span> Te Hepara Pai Church, Masterton</span><span>Ngā mihi nui ki a koutou katoa</span></div>
  </div>
</footer>
<dialog class="lightbox" id="lightbox" aria-label="Photo viewer">
  <button class="lb-btn lb-close" type="button" aria-label="Close photo">{X}</button>
  <button class="lb-btn lb-prev" type="button" aria-label="Previous photo">{L}</button>
  <button class="lb-btn lb-next" type="button" aria-label="Next photo">{R}</button>
  <figure><img src="" alt=""><figcaption></figcaption></figure>
</dialog>
<script src="js/site.js?v=5" defer></script>
</body>
</html>
'''

def page_hero(title, lede, image, alt):
    return f'''
<section class="hero">
  <div class="hero-media">{hero_img(image, alt, eager=True, cls="pos-top" if image == "priests" else "")}</div>
  <div class="wrap hero-text"><div class="hero-card"><h1>{title}</h1><p class="hero-lede">{lede}</p></div></div>
</section>
'''

def write(path, title, desc, body, og="te-rangamarie-marae"):
    html = head(title, desc, path, og) + header(path) + body + footer()
    assert "—" not in html, f"em dash in {path}"
    (ROOT / path).write_text(html, encoding="utf-8")
    print("wrote", path)

# ================================================================ HOME
REVIEWS = [
    ("Katie Olds", 5, "2 weeks ago", "This church is wonderful and welcoming. It worships God, but the services are fun and enjoyable. Everyone knows everyone, and the atmosphere is just amazing!"),
    ("Alice Duncan", 5, "a week ago", "inclusive, wonderful church."),
    ("Amanda Wu", 5, "a week ago", "A wonderful and inclusive church :)"),
    ("Ruth Olds", 5, "a week ago", "Very inclusive"),
]

def review_cards():
    out = []
    for i, (n, s, w, t) in enumerate(REVIEWS):
        cls = "review review-wide reveal" if i == 0 else "review reveal"
        out.append(f'<article class="{cls}">{stars(s, f"{s} out of 5 stars")}<blockquote><p>&ldquo;{t}&rdquo;</p></blockquote>'
                   f'<footer><strong>{n}</strong><span>Google review, {w}</span></footer></article>')
    return "".join(out)

hero_slides = [
    ("sunday", "The congregation gathered after a Sunday service"),
    ("marae", "Te Rangamarie Marae, beside the church on Cole Street"),
    ("procession", "A young member carries the processional cross"),
    ("service", "A reading at the altar during the service"),
]
slides = []
for k, (n, a) in enumerate(hero_slides):
    s = hero_img(n, a, eager=(k == 0), cls="is-on" if k == 0 else "", extra=f' data-caption="{a}"')
    slides.append(s)

faq = [
 ("What time is the Sunday service, and how long does it go?",
  "Our regular Sunday morning service begins at 9:30 am and typically lasts about an hour, followed by morning tea. We also hold additional services on special occasions such as Christmas, Ash Wednesday, Good Friday and Easter Sunday."),
 ("Where do I park, and is the church accessible?",
  "There is parking on the street outside 131 Cole Street and an Accessibility Park inside the grounds. You can also walk in from Essex Street through Douglas Park. The Church and Marae are fully accessible."),
 ("Do I need to bring anything?",
  "Nothing is required. Morning tea is shared after our Sunday services and we encourage you to bring a small plate of food to share. A small, optional koha is welcome during services, and we keep a food donation basket for the Masterton Foodbank if you would like to bring non-perishable items."),
 ("What is the service like?",
  "People of all ages, cultures, genders and faiths are welcome. Our communion services follow the New Zealand Prayer Book and we sing a range of hymns in Maori and English. Readings and the Prayers of the People are shared by members of the congregation on a rotation."),
 ("Is there anything for children?",
  "Instead of Sunday School, we offer Atrium, a fun after-school activity, on Thursdays from 3:30 pm to 4:45 pm during the school term. See the Atrium page for how a session runs."),
 ("Can we book Te Rangamarie Marae?",
  "Yes. The marae hosts hui, wānanga, retreats and community gatherings. To enquire about dates, costs and bookings, contact Bishop Wai Quayle on 027 240 9261 or by email (see the Te Rangamarie Marae page)."),
]
faq_html = "".join(
    f'<details><summary>{q}{icon("plus")}</summary><p>{a}</p></details>' for q, a in faq)

gallery_home = [
    ("sunday-service", "Members of the congregation together after the service"),
    ("whanau", "Two members of the church whānau at Te Hepara Pai"),
    ("procession", "The processional cross carried into the service"),
    ("te-rangamarie-marae", "Te Rangamarie Marae from the driveway"),
    ("service", "Clergy leading a reading at the altar"),
    ("altar-flowers", "Flowers and prayer books on the table inside the church"),
    ("priests-and-server", "Clergy with a young server at the altar"),
    ("atrium-children", "Children enjoying an Atrium activity"),
    ("paint-job", "Young members outside the freshly painted church"),
    ("liz-greville", "Rev Liz Greville at the altar"),
    ("bishop-wai-quayle", "Bishop Waitohiariki Quayle"),
    ("richard-jackson", "Deacon Richard Jackson reading at the lectern"),
    ("emily-bartlett", "Rev Emily Bartlett at the lectern"),
]
gallery_html = "".join(
    f'<figure class="reveal"><button type="button" data-full="img/{n}-1920.webp" aria-label="View larger: {a}">{img(n, a, sizes="(min-width: 900px) 33vw, 50vw")}</button></figure>' for n, a in gallery_home)

home = f'''
<section class="hero" aria-labelledby="hero-h">
  <div class="hero-media slides" aria-roledescription="slideshow" aria-label="Photos from Te Hepara Pai">
    {"".join(slides)}
  </div>
  <div class="wrap hero-text">
    <div class="hero-card">
      <h1 id="hero-h">A Māori Anglican whānau in the heart of Masterton</h1>
      <p class="hero-lede">Join us on Sunday at <strong>9:30 am</strong>, <strong>131 Cole Street</strong>. Readings and prayers are shared by the whole congregation, hymns are sung in Maori and English, and morning tea follows.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="#visit">{icon("calendar")}Plan your Sunday visit</a>
        <a class="btn btn-ghost" href="{DIRECTIONS}" target="_blank" rel="noopener">{icon("directions")}Get directions</a>
      </div>
      <a class="rating-badge" href="{GOOGLE_LISTING}" target="_blank" rel="noopener">{stars(RATING, "Rated 4.3 out of 5")}<span><strong>{RATING}</strong> from {COUNT} Google reviews</span></a>
      <p class="hero-caption">{hero_slides[0][1]}</p>
    </div>
  </div>
</section>

<section class="visit" id="visit" aria-label="Join us on Sunday">
  <div class="wrap">
    <div class="visit-card">
      <div class="visit-item">{icon("clock")}<div><h3>Sundays at 9:30 am</h3><p>About an hour, then morning tea. Bring a small plate to share if you can.</p></div></div>
      <div class="visit-item">{icon("pin")}<div><h3>131 Cole Street, Masterton</h3><p>Near Douglas Park School. <a href="{DIRECTIONS}" target="_blank" rel="noopener">Directions</a></p></div></div>
      <div class="visit-item">{icon("child")}<div><h3>Atrium for children</h3><p>Thursdays, 3:30 pm to 4:45 pm. <a href="atrium.html">How it works</a></p></div></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="welcome-h">
  <div class="wrap">
    <div class="section-head reveal">
      <h2 id="welcome-h">Welcome to Te Hepara Pai</h2>
      <p>Te Hepara Pai is part of Te Pihopatanga o Aotearoa | The Maori Anglican Church in New Zealand. We are in <a href="{TEUPOKO}" target="_blank" rel="noopener">Te Hui Amorangi ki Te Upoko o te Ika</a>. Here is everything you need for your first visit.</p>
    </div>
    <div class="trio">
      <article class="trio-item reveal" id="where">
        <figure>{img("te-rangamarie-marae", "Te Rangamarie Marae and the church grounds on Cole Street")}</figure>
        <div>
          <h2>Where</h2>
          <p>Te Hepara Pai Church is located at 131 Cole Street Masterton, near Douglas Park School.</p>
          <ul class="facts">
            <li>{icon("walk")}<span>The church can be accessed from Essex Street via the walkway through Douglas Park.</span></li>
            <li>{icon("car")}<span>There is parking on the street outside and there is an Accessibility Park inside the grounds.</span></li>
            <li>{icon("access")}<span>The Church and Marae are fully accessible.</span></li>
            <li>{icon("pin")}<span>We are within walking distance of St Matthew&rsquo;s Collegiate, Wairarapa College and approximately a 20&#8209;minute walk from the town centre.</span></li>
          </ul>
        </div>
      </article>
      <article class="trio-item reveal" id="how">
        <figure>{img("service", "Clergy and congregation members sharing a reading during the service")}</figure>
        <div>
          <h2>How</h2>
          <p>We are a multi-cultural congregation and our services actively involve the congregation. All readings, including the Old Testament, New Testament, and the Psalms, are delivered on a rotational basis by our regular church attendees. Similarly, our Prayers of the People are offered by members of the congregation ensuring we capture the thanks and concerns of the wider community.</p>
          <ul class="facts">
            <li>{icon("cup")}<span>Morning tea is shared after our Sunday services and we encourage you to bring a small plate of food to share.</span></li>
            <li>{icon("basket")}<span>We support our wider community by maintaining a food donation basket for the Masterton Foodbank. We welcome small contributions of non-perishable food items for local people in need.</span></li>
            <li>{icon("heart")}<span>To help maintain church operations, we kindly request a small, optional koha during services. Every dollar assists in keeping our church running.</span></li>
          </ul>
        </div>
      </article>
      <article class="trio-item reveal" id="when">
        <figure>{img("priests-and-server", "Two of our priests with a young server at the altar")}</figure>
        <div>
          <h2>When</h2>
          <p>Our regular Sunday morning service begins at 9:30 am and typically lasts about an hour, followed by morning tea.</p>
          <p>We also hold additional services on special occasions such as Christmas, Ash Wednesday, Good Friday and Easter Sunday.</p>
          <p>Instead of Sunday School, we offer Atrium, a fun after-school activity, on Thursdays from 3:30 pm to 4:45 pm.</p>
          <a class="btn btn-outline" href="events.html">{icon("calendar")}See upcoming services</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section green mission" aria-labelledby="mission-h">
  <div class="wrap mission-grid">
    <div class="reveal">
      <h2 id="mission-h" class="sr">Our purpose</h2>
      <blockquote><p>We seek <em>Te Oranga Ake o Te Iwi, o te Ao</em>, the expression of God&rsquo;s Kingdom through the flourishing of all people and of all creation.</p></blockquote>
    </div>
    <div class="reveal">
      <p>People of all ages, cultures, genders and faiths are welcome at Te Hepara Pai. Our communion services follow the New Zealand Prayer Book and we sing a range of hymns in Maori and English.</p>
      <a class="btn btn-ghost" href="who-we-are.html">{icon("arrow")}Meet our people</a>
    </div>
  </div>
</section>

<section class="section bone" aria-labelledby="explore-h">
  <div class="wrap">
    <div class="section-head reveal"><h2 id="explore-h">Explore our community</h2></div>
    <div class="cards">
      <a class="card reveal" href="who-we-are.html"><figure>{img("priests-and-server", "Two of our priests with a young server", sizes="(min-width: 760px) 50vw, 100vw")}</figure><h3>Who we are{icon("arrow")}</h3><p>Our leaders, our congregation and the voices of our people.</p></a>
      <a class="card reveal" href="atrium.html"><figure>{img("atrium-children", "Children at an Atrium session", sizes="(min-width: 760px) 50vw, 100vw")}</figure><h3>Atrium{icon("arrow")}</h3><p>A gentle, guided programme for children on Thursdays.</p></a>
      <a class="card reveal" href="marae.html"><figure>{img("te-rangamarie-marae", "Te Rangamarie Marae", sizes="(min-width: 760px) 50vw, 100vw")}</figure><h3>Te Rangamarie Marae{icon("arrow")}</h3><p>Book our wharenui and wharekai for hui, wānanga and retreats.</p></a>
      <a class="card reveal" href="events.html"><figure>{img("paint-job", "Young members outside the newly painted church", sizes="(min-width: 760px) 50vw, 100vw")}</figure><h3>Updates and events{icon("arrow")}</h3><p>Upcoming services and news, like our amazing new paint job.</p></a>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="photos-h">
  <div class="wrap">
    <div class="section-head reveal"><h2 id="photos-h">Photo wall</h2><p>Sundays, servers, Atrium and the marae: a few moments from life at Te Hepara Pai.</p></div>
    <div class="gallery">{gallery_html}</div>
  </div>
</section>

<section class="section bone" aria-labelledby="reviews-h">
  <div class="wrap">
    <div class="section-head reveal"><h2 id="reviews-h">What people say</h2><p>Real reviews from our Google listing.</p></div>
    <div class="reviews">{review_cards()}</div>
    <div class="reviews-summary reveal">
      <span class="score">{RATING}</span>{stars(RATING, "Rated 4.3 out of 5")}<span>from {COUNT} Google reviews</span>
      <a class="btn btn-outline" href="{GOOGLE_LISTING}" target="_blank" rel="noopener">See all our Google reviews</a>
    </div>
  </div>
</section>

<section class="banner" aria-label="Leave a review">
  <div class="wrap">
    <h2>Been to a service with us? Leave us a review</h2>
    <a class="btn btn-primary" href="{GOOGLE_LISTING}" target="_blank" rel="noopener">{GOOGLE}Review us on Google</a>
  </div>
</section>

<section class="section" aria-labelledby="faq-h">
  <div class="wrap">
    <div class="section-head reveal"><h2 id="faq-h">Coming for the first time?</h2><p>Answers to the questions people ask before their first Sunday.</p></div>
    <div class="faq reveal">{faq_html}</div>
  </div>
</section>
''' + contact_section()

write("index.html", "Te Hepara Pai | Māori Anglican Church, Masterton",
      "Te Hepara Pai is a Māori Anglican church at 131 Cole Street, Masterton. Join us for Sunday service at 9:30 am, followed by morning tea.", home)

# ================================================================ WHO WE ARE
def phone_link(p, t):
    return f'<a class="phone" href="tel:{t}">{icon("phone")}{p}</a>'

who = page_hero("Who we are",
    "A multi-cultural congregation in Te Hui Amorangi ki Te Upoko o te Ika, led by a small ministry team who serve alongside Bishop Waitohiariki.",
    "priests", "Two of our priests with a young server at the altar") + f'''
<section class="section" aria-labelledby="lead-h">
  <div class="wrap">
    <div class="section-head reveal"><h2 id="lead-h">Leadership</h2></div>
    <div class="leaders">
      <article class="leader feature reveal" id="bishop">
        <div>
          <h3>Pihopa Waitohiariki Quayle</h3>
          <p class="role">Pīhopa o te Hui Amorangi ki te Upoko o te Ika</p>
          <p>The first Pīhopa (Bishop) of Te Upoko was the Right Reverend Muru Walters, from his consecration on 7 March 1992 until his retirement in 2018. On 12 September 2019, Bishop Waitohiariki (Wai) Quayle was consecrated as Pīhopa o te Hui Amorangi ki te Upoko o te Ika, and in doing so she became the first Māori woman to become a Bishop.</p>
          <p>Bishop Quayle (Ngāti Kahungunu ki Wairarapa and Whakatohea) has a Bachelor of Bicultural Social Work degree from Te Wānanga o Aotearoa, and she worked previously as the Māori Community Health Services Manager at Whaiora Māori Health Services in Masterton.</p>
          <p>She was ordained deacon (2013) and priest (2014) by then-Bishop Muru Walters at the Church of Te Hepara Pai in Masterton. From 2015 until her appointment as Bishop, she was the Archdeacon of the Māori Pastorate of Wairarapa.</p>
          <p>As Pīhopa of Te Upoko, Bishop Quayle is responsible for guiding Mihinare (Māori Anglicans) in Wellington, Wairarapa, Kāpiti, Horowhenua, Manawatū, Rangitīkei, Whanganui, and Taranaki.</p>
          <img class="seal" src="img/seal-logo.png" width="1032" height="1752" alt="The seal of Waitohiariki Quayle, Pīhopa ki te Upoko o te Ika, 2019" loading="lazy">
        </div>
        <figure>{img("bishop-wai-quayle", "Bishop Waitohiariki Quayle in her robes, smiling", sizes="(min-width: 860px) 45vw, 100vw")}</figure>
      </article>

      <article class="leader reveal" id="liz">
        <figure>{img("liz-greville", "Rev Liz Greville at the altar of Te Hepara Pai", sizes="(min-width: 860px) 320px, 100vw", extra=' data-img-role="small"')}</figure>
        <div>
          <h3>Rev Liz Greville</h3>
          <p class="role">Co-priest in charge</p>
          <p>Reverend Liz Greville is a co-priest in charge at Te Hepara Pai, ordained over 20 years ago by Bishop Tom Brown, serving at the country churches, St Andrew&rsquo;s in the Paddock, Upper Plain, and St Francis, Bideford, as well as taking services of all sorts at St Matthew&rsquo;s, including sung Evensong.</p>
          <p>My service at Te Hepara Pai under He Amarangi ki te Upoko o te Ika began at the end of 2017. My ministry includes working alongside several catechists in our atrium, using the Catechesis of the Good Shepherd program, the spiritual arm of Montessori. I also serve as a minister, teaching three levels of theological, liturgical, church history, etc. to kaikarakia, deacons and priests.</p>
          <p>Outside of my formal job, I am the owner of Coco Chanel, my fabulous, intelligent, gloriously engineered Thermomix. I love making miniatures and one day I&rsquo;ll get back to lace making and embroidery.</p>
          {phone_link("027 474 5200", "+64274745200")}
        </div>
      </article>

      <article class="leader reveal" id="emily">
        <figure>{img("emily-bartlett", "Rev Emily Bartlett leading the service from the lectern", sizes="(min-width: 860px) 320px, 100vw", extra=' data-img-role="small"')}</figure>
        <div>
          <h3>Rev Emily Bartlett</h3>
          <p class="role">Co-priest</p>
          <p>Affiliated with Ngapuhi Iwi from Hokianga, my devotion lies in community ministry and supporting Bishop Waitohiariki. Working alongside my dear friend Rev&rsquo;d Liz, I serve as a co-Priest with a background rooted in the Ratana and Māori Anglican traditions.</p>
          <p>My spiritual journey has taken me from Gisborne to Waikato, eventually leading me here to Te Hepara Pai in 2018. My soul is nourished by the Divine, my grandchildren, and the art of Raranga Harakeke. Whether I am baking on a chilly day or enjoying a quiet moment with coffee, I am constantly reminded of God&rsquo;s grace protecting our church whanau.</p>
          {phone_link("021 053 6731", "+64210536731")}
        </div>
      </article>

      <article class="leader reveal" id="richard">
        <figure>{img("richard-jackson", "Deacon Richard Jackson reading at the lectern", sizes="(min-width: 860px) 320px, 100vw", extra=' data-img-role="small"')}</figure>
        <div>
          <h3>Deacon Richard Jackson</h3>
          <p class="role">Deacon</p>
          <p>I grew up in Hastings and attended the Presbyterian Church. After high school, I joined the Navy and enjoyed a full career of 31 years (most of which was behind a desk, interestingly!). I moved to Masterton in 2000 and commuted to Wellington for 14 years until my retirement. I began attending Te Hāhi Wairua in 2019 and was welcomed into a very supportive congregation. After serving as a Kaitautoko, I entered Deacon training and was ordained in 2024. My personal challenge is to learn Te Reo Māori.</p>
          {phone_link("027 811 0006", "+64278110006")}
        </div>
      </article>

      <article class="leader no-photo reveal" id="robin">
        <div><div class="avatar" aria-hidden="true">RI</div></div>
        <div>
          <h3>Rev Robin Irwin</h3>
          <p class="role">Secretary</p>
                    {phone_link("027 486 2714", "+64274862714")}
        </div>
      </article>
    </div>
  </div>
</section>

<section class="section green" aria-labelledby="cong-h" id="congregation">
  <div class="wrap">
    <div class="split">
      <div class="reveal">
        <h2 id="cong-h">Congregation</h2>
        <p class="lead">People of all ages, cultures, genders and faiths are welcome at Te Hepara Pai.</p>
        <p>Our communion services follow the New Zealand Prayer Book and we sing a range of hymns in Maori and English.</p>
      </div>
      <figure class="reveal">{img("whanau", "Two members of the congregation smiling together inside the church")}</figure>
    </div>
    <h3 class="reveal" style="margin-top:64px">Voices of our people</h3>
    <div class="voices">
      <div class="voice reveal"><h3>What makes our church special?</h3><ul>
        <li>Tikanga Maori<span>Richard</span></li><li>Everyone gets to be a part of the church<span>Ben</span></li><li>Maanakitanga<span>Lisa</span></li></ul></div>
      <div class="voice reveal"><h3>How do the services feel?</h3><ul>
        <li>Respectful, friendly and encouraging<span>Richard</span></li><li>Inspirational<span>Lisa</span></li><li>Respectful without being formal and respecting traditional Anglican liturgical practice<span>Robyn</span></li><li>Interesting<span>Ben</span></li></ul></div>
      <div class="voice reveal"><h3>What is one word to describe our church?</h3><ul>
        <li>Welcoming<span>Richard</span></li><li>Friendly<span>Ben</span></li><li>Inclusive<span>Lisa</span></li><li>Inclusive<span>Robyn</span></li></ul></div>
    </div>
  </div>
</section>
''' + contact_section()

write("who-we-are.html", "Who we are | Te Hepara Pai, Masterton",
      "Meet the leaders and congregation of Te Hepara Pai, the Māori Anglican church in Masterton: Bishop Waitohiariki Quayle, Rev Liz Greville, Rev Emily Bartlett, Deacon Richard Jackson and Rev Robin Irwin.",
      who, og="procession")

# ================================================================ ATRIUM
atrium = page_hero("Atrium",
    "Atrium is a gentle, guided program for children, helping them listen to God, learn the stories of our faith, and grow as a community.",
    "atrium", "Children smiling during an Atrium session") + f'''
<section class="visit" aria-label="Atrium at a glance">
  <div class="wrap">
    <div class="visit-card">
      <div class="visit-item">{icon("clock")}<div><h3>Thursdays, 3:30 pm to 4:45 pm</h3><p>Instead of Sunday School: a fun after-school activity.</p></div></div>
      <div class="visit-item">{icon("calendar")}<div><h3>Follows the school year</h3><p>From the second week of each term to the last week. Term 4 runs until around mid-December.</p></div></div>
      <div class="visit-item">{icon("pin")}<div><h3>At the church</h3><p>131 Cole Street, Masterton. Pick up from the church at 4:45 pm.</p></div></div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="session-h">
  <div class="wrap split" style="align-items:start">
    <div>
      <div class="section-head reveal">
        <h2 id="session-h">How a session runs</h2>
        <p>The weekly sessions strike a good balance between structure and child-friendly fun.</p>
      </div>
      <ol class="steps">
        <li class="reveal"><span class="time">{icon("sun")}</span><h3>3:30 pm: walk-in and welcome</h3><p>Everything kicks off at 3:30 PM, right after the kids have had their afternoon snack, so they&rsquo;re settled and ready. We start with a formal walk-in and a welcoming hello, creating a respectful but relaxed atmosphere.</p></li>
        <li class="reveal"><span class="time">{icon("book")}</span><h3>Presentation or story</h3><p>The core of the program is a carefully put-together presentation or story. This structured activity always focuses on a specific biblical or faith-based theme for the week, helping children gradually build their understanding of faith. To keep things fresh and connected to the wider church year, the weekly theme sometimes ties in with major seasons or holidays, like Advent, Lent, or big feast days.</p></li>
        <li class="reveal"><span class="time">{icon("palette")}</span><h3>Free time to explore</h3><p>After the teaching time, children get a period of free time. This gives them a chance to absorb the lesson and explore the environment at their own pace. They&rsquo;re encouraged to use the variety of resources in the specially stocked activity drawers, which contain materials for crafts, quiet thinking, and play, all subtly linked to the program&rsquo;s themes.</p></li>
        <li class="reveal"><span class="time">{icon("story")}</span><h3>A shared story</h3><p>The session wraps up with one final, shared activity. We read a story aloud from a simplified children&rsquo;s Bible. This reading reinforces the main scriptural message the congregation is meant to take away, cementing the spiritual lesson in a final, memorable way.</p></li>
        <li class="reveal"><span class="time">{icon("hands")}</span><h3>4:45 pm: prayers, song and home</h3><p>The whole program finishes at 4:45 PM with communal prayers and a song, offering a peaceful and thoughtful end to their time together.</p></li>
      </ol>
    </div>
    <figure class="tall reveal" style="position:sticky;top:96px">{img("priests-and-server", "A young server stands between two of our priests at the altar")}</figure>
  </div>
</section>

<section class="section green" aria-label="About Atrium">
  <div class="wrap mission-grid">
    <blockquote class="reveal" style="margin:0"><p class="pull">&ldquo;Atrium is a gentle, guided programme for all ages, helping us listen for God, learn the stories of our faith, and grow as a community.&rdquo;</p></blockquote>
    <div class="reveal">
      <p>Rev Liz Greville works alongside several catechists in our atrium, using the Catechesis of the Good Shepherd program.</p>
      <a class="btn btn-ghost" href="who-we-are.html#liz">{icon("arrow")}Meet Rev Liz</a>
    </div>
  </div>
</section>

<section class="section bone" aria-labelledby="terms-h">
  <div class="wrap split">
    <div class="reveal">
      <h2 id="terms-h">Term dates and pick-up</h2>
      <p>The Atrium program generally follows the school year. It usually starts in the second week of each school term and continues until the last week of the term. Because school end dates can vary, especially at the end of the year, the Term 4 session is uniquely scheduled to run until around mid-December, making sure the program covers the important lead-up to Christmas.</p>
      <p>When the program finishes at 4:45 PM, we have a clear dismissal process. Children can be picked up directly from the church by their parents or guardians, or, if we have permission, they can walk home on their own. This consistent timing and clear structure guarantee a reliable and spiritually enriching environment for everyone.</p>
      <a class="btn btn-primary" href="tel:+64274745200">{icon("phone")}Ask Rev Liz about Atrium</a>
    </div>
    <figure class="reveal">{img("atrium-children", "Three children at an Atrium activity with a wooden bowl")}</figure>
  </div>
</section>
''' + contact_section()

write("atrium.html", "Atrium for children | Te Hepara Pai, Masterton",
      "Atrium at Te Hepara Pai: a gentle, guided after-school programme for children on Thursdays, 3:30 pm to 4:45 pm, at 131 Cole Street, Masterton.",
      atrium, og="atrium-children")

# ================================================================ MARAE
marae = page_hero("Te Rangamarie Marae",
    "A warm, welcoming space for hui, wānanga, retreats and community gatherings, right beside the church.",
    "marae", "Te Rangamarie Marae with its red-trimmed wharenui and garden") + f'''
<section class="section" aria-labelledby="book-h">
  <div class="wrap split">
    <div class="reveal">
      <h2 id="book-h">Book our facilities</h2>
      <p class="lead">Te Rangamarie Marae is a warm, welcoming space for hui, wānanga, retreats and community gatherings. Our wharenui, wharekai and shared spaces are well cared for, with plenty of room for sleeping, meeting and sharing kai together.</p>
      <p>We&rsquo;re also working to upgrade our facilities, with new, modern bathroom areas opening in 2027 to make your stay even more comfortable.</p>
      <ul class="facts">
        <li>{icon("home")}<span>Wharenui, wharekai and shared spaces</span></li>
        <li>{icon("access")}<span>The Church and Marae are fully accessible, with an Accessibility Park inside the grounds</span></li>
        <li>{icon("pin")}<span>131 Cole Street, Masterton, near Douglas Park School</span></li>
      </ul>
    </div>
    <figure class="reveal"><span class="tag">Opening 2027: new bathrooms</span>{img("te-rangamarie-marae", "The marae grounds, with ponga fence posts and a lawn")}</figure>
  </div>
</section>

<section class="section green" aria-labelledby="enq-h">
  <div class="wrap contact-grid">
    <div class="reveal">
      <h2 id="enq-h">Enquire about dates, costs and bookings</h2>
      <p class="lead">To enquire about dates, costs, and bookings please contact Bishop Wai Quayle.</p>
      <ul class="info-rows">
        <li>{icon("phone")}<span><a href="tel:+64272409261">027 240 9261</a></span></li>
        <li>{icon("mail")}<span><a href="#" data-gmail data-user="quaylew" data-domain="xtra.co.nz" data-su="Te%20Rangamarie%20Marae%20booking%20enquiry" data-body="Kia%20ora%20Bishop%20Wai%2C%0A%0AI%27d%20like%20to%20enquire%20about%20booking%20Te%20Rangamarie%20Marae.%0A%0ADates%3A%0ANumber%20of%20people%3A%0AType%20of%20gathering%3A%0A%0ANg%C4%81%20mihi%2C"><span data-email-text data-user="quaylew" data-domain="xtra.co.nz">Email Bishop Wai</span></a></span></li>
      </ul>
    </div>
    <div class="contact-actions reveal">
      <a class="btn btn-primary" href="tel:+64272409261">{icon("phone")}<span>Call Bishop Wai Quayle<small>027 240 9261</small></span></a>
      <a class="btn btn-ghost" href="#" data-gmail data-user="quaylew" data-domain="xtra.co.nz" data-su="Te%20Rangamarie%20Marae%20booking%20enquiry" data-body="Kia%20ora%20Bishop%20Wai%2C%0A%0AI%27d%20like%20to%20enquire%20about%20booking%20Te%20Rangamarie%20Marae.%0A%0ADates%3A%0ANumber%20of%20people%3A%0AType%20of%20gathering%3A%0A%0ANg%C4%81%20mihi%2C">{icon("mail")}<span>Email a booking enquiry<small>Opens a pre-filled email</small></span></a>
    </div>
  </div>
</section>
<section class="map" aria-label="Map showing Te Rangamarie Marae">
  <div class="wrap"><iframe src="{MAPS_EMBED}" title="Map: Te Hepara Pai Church and Te Rangamarie Marae, 131 Cole Street, Masterton" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
</section>
'''

write("marae.html", "Te Rangamarie Marae | Te Hepara Pai, Masterton",
      "Book Te Rangamarie Marae at 131 Cole Street, Masterton for hui, wānanga, retreats and community gatherings. Enquiries to Bishop Wai Quayle on 027 240 9261.",
      marae, og="te-rangamarie-marae")

# ================================================================ EVENTS
events = page_hero("Updates and events",
    "Sunday services every week at 9:30 am, special services through the church year, and news from Te Hepara Pai.",
    "sunday", "The congregation gathered inside the church") + f'''
<section class="section" aria-labelledby="up-h">
  <div class="wrap split" style="align-items:start">
    <div class="reveal">
      <h2 id="up-h">Upcoming services</h2>
      <p>Sunday services: 9:30 am (weekly), at 131 Cole Street.</p>
      <ul class="dates" id="upcoming-sundays">
        <li class="date"><div class="cal"><small>Every</small><b>Sun</b></div><div><h3>Sunday service</h3><p>9:30 am, followed by morning tea. 131 Cole Street, Masterton</p></div></li>
      </ul>
    </div>
    <div class="reveal">
      <h2>Special services</h2>
      <p>We also hold additional services on special occasions such as:</p>
      <ul class="special"><li>Christmas</li><li>Ash Wednesday</li><li>Good Friday</li><li>Easter Sunday</li></ul>
      <p style="margin-top:24px">For dates and times of special services, give one of our ministry team a call.</p>
      <h2 style="margin-top:48px">Every Thursday in term</h2>
      <p>Atrium for children, 3:30 pm to 4:45 pm. <a href="atrium.html">Read about Atrium</a></p>
    </div>
  </div>
</section>

<section class="section bone" aria-labelledby="news-h">
  <div class="wrap split">
    <figure class="reveal">{img("paint-job", "Three young people with the processional cross outside the freshly painted church")}</figure>
    <div class="reveal">
      <h2 id="news-h">Amazing new paint job at Te Hepara Pai</h2>
      <p class="lead">Come and see it for yourself on Sunday at 9:30 am.</p>
    </div>
  </div>
</section>
''' + contact_section()

write("events.html", "Updates and events | Te Hepara Pai, Masterton",
      "Upcoming Sunday services at Te Hepara Pai, Masterton (9:30 am weekly), special services at Christmas, Ash Wednesday, Good Friday and Easter, and church news.",
      events, og="sunday-service")

# ================================================================ PRIVACY
privacy = f'''
<section class="section"><div class="wrap prose">
<h1>Privacy</h1>
<p>This website does not use contact forms, does not set tracking cookies and does not collect personal information.</p>
<p>When you tap a phone number your device makes a normal call. When you tap an email button, a draft opens in Gmail and nothing is sent until you choose to send it. The map is provided by Google Maps and the fonts by Google Fonts, which may receive standard technical information (such as your IP address) when those parts of the page load.</p>
<p>If you have any questions, please call Rev'd Robin Irwin, our Secretary, on <a href="tel:+64274862714">027 486 2714</a>.</p>
<p><a href="index.html">Back to the home page</a></p>
</div></section>
'''
write("privacy.html", "Privacy | Te Hepara Pai, Masterton", "Privacy information for the Te Hepara Pai Church website.", privacy)
