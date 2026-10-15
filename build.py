from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent

FONT_LINKS = '''
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
'''


def icon(name):
    return f'<svg aria-hidden="true" class="lifecycle-stage__icon"><use href="/assets/icons.svg#icon-{name}"></use></svg>'


def header():
    return '''
<header class="site-header" aria-label="Primary navigation">
  <div class="header-inner">
    <a class="brand" href="/" aria-label="Priority Fitness home">
      <img class="brand-logo brand-logo--mark" src="/assets/images/pf-mark.png" alt="" width="48" height="36">
      <img class="brand-logo brand-logo--full" src="/assets/images/priority-fitness-logo.png" alt="Priority Fitness" width="150" height="64">
    </a>
    <nav class="nav" aria-label="Desktop navigation">
      <a class="nav-link" data-nav="used" href="/used-equipment/">Used Equipment</a>
      <div class="menu-wrap">
        <a class="nav-link" data-nav="services" href="/services/">Services</a>
        <div class="mega" aria-label="Services menu">
          <div class="mega-grid">
            <a href="/services/equipment-sourcing/">Equipment Sourcing</a>
            <a href="/services/equipment-installation/">Equipment Installation</a>
            <a href="/services/equipment-service-repair/">Repair + Service</a>
            <a href="/services/preventative-maintenance/">Preventative Maintenance</a>
            <a href="/services/equipment-relocation/">Equipment Relocation</a>
            <a href="/services/equipment-extraction/">Extraction + Removal</a>
          </div>
        </div>
      </div>
      <a class="nav-link" data-nav="sell" href="/sell-equipment/">Sell Your Equipment</a>
      <a class="nav-link" href="/industries/">Industries</a>
      <a class="nav-link" data-nav="projects" href="/projects/">Projects</a>
      <a class="nav-link" data-nav="about" href="/about/">About</a>
      <a class="nav-link" data-nav="contact" href="/contact/">Contact</a>
    </nav>
    <a class="btn btn--primary header-cta" href="/request-quote/">Request a Quote</a>
    <button class="mobile-toggle" type="button" aria-expanded="false" aria-controls="mobileNav" aria-label="Open navigation"><span></span></button>
  </div>
  <nav class="mobile-panel" id="mobileNav" aria-label="Mobile navigation">
    <a href="/used-equipment/">Used Equipment <span>↗</span></a>
    <a href="/services/">Services <span>↗</span></a>
    <div class="mobile-subhead">Core services</div>
    <a href="/services/equipment-sourcing/">Equipment Sourcing <span>→</span></a>
    <a href="/services/equipment-installation/">Installation <span>→</span></a>
    <a href="/services/equipment-service-repair/">Repair + Service <span>→</span></a>
    <a href="/services/preventative-maintenance/">Maintenance <span>→</span></a>
    <a href="/services/equipment-relocation/">Relocation <span>→</span></a>
    <a href="/services/equipment-extraction/">Extraction + Removal <span>→</span></a>
    <div class="mobile-subhead">More</div>
    <a href="/sell-equipment/">Sell Your Equipment <span>→</span></a>
    <a href="/industries/">Industries <span>→</span></a>
    <a href="/projects/">Projects <span>→</span></a>
    <a href="/about/">About <span>→</span></a>
    <a href="/contact/">Contact <span>→</span></a>
    <a class="btn btn--primary" href="/request-quote/">Request a Quote</a>
  </nav>
</header>
'''


def footer():
    return '''
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="/assets/images/pf-mark.png" alt="Priority Fitness mark" width="68" height="43">
        <p>Fitness equipment support from sourcing and installation through service, relocation, replacement, and removal.</p>
      </div>
      <div>
        <div class="footer-title">Navigation</div>
        <div class="footer-links">
          <a href="/used-equipment/">Used Equipment</a>
          <a href="/industries/">Industries</a>
          <a href="/projects/">Projects</a>
          <a href="/about/">About</a>
          <a href="/contact/">Contact</a>
        </div>
      </div>
      <div>
        <div class="footer-title">Services</div>
        <div class="footer-links">
          <a href="/services/equipment-sourcing/">Equipment Sourcing</a>
          <a href="/services/equipment-installation/">Installation</a>
          <a href="/services/equipment-service-repair/">Repair + Service</a>
          <a href="/services/preventative-maintenance/">Preventative Maintenance</a>
          <a href="/services/equipment-relocation/">Relocation</a>
          <a href="/services/equipment-extraction/">Extraction + Removal</a>
        </div>
      </div>
      <div>
        <div class="footer-title">Contact</div>
        <div class="footer-contact">
          <strong>920-765-3644</strong>
          <a href="tel:+19207653644">Call Priority Fitness</a>
          <strong>support@pf-pros.com</strong>
          <a href="mailto:support@pf-pros.com">Email Priority Fitness</a>
          <strong>433 S Industrial Park Rd</strong>
          <strong>8:00 AM–5:00 PM</strong>
          <a href="https://www.facebook.com/priorityfitnesspros" target="_blank" rel="noopener">Facebook ↗</a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© Priority Fitness. Front-end design system.</span>
      <div class="footer-utility"><span>Privacy</span><span>Accessibility</span></div>
    </div>
  </div>
</footer>
'''


def page(title, body, description='Priority Fitness fitness-equipment services across Wisconsin.', body_class=''):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} | Priority Fitness</title>
<meta name="description" content="{escape(description)}">
{FONT_LINKS}
<link rel="stylesheet" href="/assets/css/styles.css">
<link rel="icon" href="/favicon.ico" sizes="32x32 48x48">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/images/favicon/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/images/favicon/icon-192.png">
<link rel="apple-touch-icon" href="/assets/images/favicon/apple-touch-icon.png">
</head>
<body class="{body_class}">
{header()}
<main>
{body}
</main>
{footer()}
<script src="/assets/js/app.js" defer></script>
</body>
</html>'''


def page_hero(eyebrow, title, copy, image, buttons='', compact=False, position='center'):
    c = ' page-hero--compact' if compact else ''
    return f'''
<section class="page-hero{c}">
  <div class="page-hero__media"><img src="/assets/images/{image}" alt="" style="object-position:{position}" fetchpriority="high"></div>
  <div class="page-hero__overlay"></div>
  <div class="container page-hero__content">
    <div class="eyebrow">{eyebrow}</div>
    <h1>{title}</h1>
    <p>{copy}</p>
    {buttons}
  </div>
</section>'''


def final_cta(title='Whatever happens to your equipment, you know who to call.'):
    return f'''
<section class="cta-band">
  <div class="cta-band__bg" aria-hidden="true"></div>
  <div class="cta-band__overlay"></div>
  <div class="container">
    <div class="cta-band__content reveal">
      <div class="eyebrow">From one machine to full facilities</div>
      <h2 class="h2">{title}</h2>
      <div class="btn-row">
        <a class="btn btn--primary" href="/request-quote/">Request a Quote</a>
        <a class="btn btn--light" href="tel:+19207653644">920-765-3644</a>
      </div>
    </div>
  </div>
</section>'''


def certification_strip():
    return '''
<section class="section section--warm">
  <div class="container certs-grid reveal">
    <div>
      <div class="eyebrow">Certifications + brand experience</div>
      <h2 class="h2">Certified where it counts.<br>Experienced across the industry.</h2>
      <p class="lede">Priority Fitness is Matrix, Precor, and Core certified and works with all major fitness-equipment brands across residential and commercial environments.</p>
      <p class="cert-note">Certification logos identify confirmed certifications only. Broader brand-service capability is not presented as manufacturer certification.</p>
    </div>
    <div class="cert-logos" aria-label="Confirmed certifications">
      <div class="cert-logo"><img src="/assets/images/matrix.png" alt="Matrix"></div>
      <div class="cert-logo"><img src="/assets/images/precor.png" alt="Precor"></div>
      <div class="cert-logo"><img src="/assets/images/core-fitness.png" alt="Core Health & Fitness"></div>
    </div>
  </div>
</section>'''


def why_priority():
    items = [
        ('Fitness equipment specialists', 'This is the equipment category Priority Fitness works in every day.'),
        ('Statewide Wisconsin', 'Statewide coverage with flat statewide pricing and no zone fees.'),
        ('Certified', 'Confirmed Matrix, Precor, and Core certifications.'),
        ('One machine to full facilities', 'Residential and commercial work under one equipment-focused team.'),
        ('10+ years', 'Approximately a decade of fitness-industry experience.'),
        ('Real operator experience', 'Priority Fitness does not just service gyms. The team has experience operating six affiliated gyms.'),
        ('Complete lifecycle support', 'Buy, deliver, install, maintain, repair, move, replace, and remove.')
    ]
    rows = ''.join(f'''<div class="why-row"><div class="why-row__num">{i:02d}</div><div><h3>{t}</h3><p>{d}</p></div></div>''' for i,(t,d) in enumerate(items,1))
    return f'''
<section class="section section--dark">
  <div class="container why-layout">
    <div class="why-sticky reveal"><div class="eyebrow">Concrete proof</div><h2 class="h2">Why Priority Fitness?</h2><p class="lede">Less vague "great service" language. More reasons a facility manager, homeowner, school, manufacturer rep, or gym owner can actually evaluate.</p></div>
    <div class="why-list reveal">{rows}</div>
  </div>
</section>'''


def social_proof():
    return '''
<section class="section section--ink">
  <div class="container social-proof reveal">
    <div class="rating-block">
      <div><div class="eyebrow">Google rating</div><div class="rating-stars" aria-label="4.6 out of 5 stars">4.6 / 5</div></div>
      <div><div class="rating-value">4.6</div><div>Google rating</div></div>
    </div>
    <div class="proof-copy">
      <div class="eyebrow">Trusted with the heavy stuff</div>
      <h2 class="h2">People remember good work.</h2>
      <p class="lede">A 4.6-star Google rating sits alongside the strongest proof Priority Fitness has: real equipment work, confirmed certifications, and experience across residential and commercial environments.</p>
      <div class="proof-tags"><span class="proof-tag">Residential equipment</span><span class="proof-tag">Commercial install partners</span><span class="proof-tag">Equipment buyers</span></div>
      <a class="text-link" href="/projects/">See real project work</a>
    </div>
  </div>
</section>'''

# HOME
lifecycle = [
    ('buy','01','BUY','/assets/images/facility-after.webp','Need equipment? Start with what you’re looking for.','Find Equipment','/services/equipment-sourcing/','Completed mixed fitness facility with strength and cardio equipment'),
    ('deliver','02','DELIVER','/assets/images/moving-delivery.webp','From truck to the right place, with equipment handled by an equipment team.','Explore Installation','/services/equipment-installation/','Priority Fitness team member carrying fitness equipment from a delivery trailer'),
    ('install','03','INSTALL','/assets/images/hero-installation.webp','From delivery through final placement.','Explore Installation','/services/equipment-installation/','Fitness equipment installation and assembly in progress'),
    ('maintain','04','MAINTAIN','/assets/images/treadmill-service-corridor.webp','Keep equipment inspected, maintained, and ready for use.','Explore Maintenance','/services/preventative-maintenance/','Priority Fitness technicians working across a row of treadmills'),
    ('repair','05','REPAIR','/assets/images/equipment-service.webp','Something isn’t working right?','Request Service','/services/equipment-service-repair/','Technicians working directly on cardio equipment'),
    ('move','06','MOVE','/assets/images/equipment-moving.webp','One machine or an entire facility.','Move Equipment','/services/equipment-relocation/','Wrapped fitness equipment being moved at a delivery trailer'),
    ('replace','07','REPLACE','/assets/images/school-racks-after.webp','Old equipment out. The right replacement in.','Plan a Replacement','/request-quote/','Updated school weight-room rack installation'),
    ('remove','08','REMOVE','/assets/images/facility-before.webp','Clear space for what comes next.','Explore Removal','/services/equipment-extraction/','Cleared fitness room ready for its next equipment phase'),
]
stages=''.join(f'''<button class="lifecycle-stage{' is-active' if i==0 else ''}" role="tab" aria-selected="{'true' if i==0 else 'false'}" data-image="{img}" data-message="{msg}" data-cta="{cta}" data-url="{url}" data-alt="{alt}">{icon(ic)}<span class="lifecycle-stage__num">{num}</span><span class="lifecycle-stage__name">{name}</span></button>''' for i,(ic,num,name,img,msg,cta,url,alt) in enumerate(lifecycle))

home_body = f'''
<section class="home-hero">
  <div class="hero-media"><img id="heroLifecycleImage" src="/assets/images/facility-after.webp" alt="Completed mixed fitness facility" fetchpriority="high"></div>
  <div class="hero-content">
    <div class="hero-top">
      <div class="hero-kicker">Wisconsin fitness-equipment specialists</div>
      <h1 class="hero-headline">Never think about your equipment again.</h1>
      <p class="hero-sub">Source it. Deliver it. Install it. Maintain it. Repair it. Move it. Replace it. Remove it. Priority Fitness handles the equipment lifecycle from one machine to an entire facility.</p>
      <div class="btn-row"><a class="btn btn--primary" href="/request-quote/">Tell Us What You Need</a><a class="btn btn--light" href="/projects/">View Projects</a></div>
    </div>
    <div class="lifecycle-panel" aria-label="Equipment lifecycle selector">
      <div class="lifecycle-panel__meta"><div><div class="lifecycle-panel__label">Choose where you are in the lifecycle</div><div id="lifecycleMessage" class="lifecycle-message">Need equipment? Start with what you’re looking for.</div></div><a id="lifecycleCta" class="text-link lifecycle-cta" href="/services/equipment-sourcing/">Find Equipment</a></div>
      <div class="lifecycle-rail" role="tablist">{stages}</div>
    </div>
  </div>
</section>
<section class="trust-strip"><div class="container trust-grid">
  <div class="trust-item"><div class="trust-value">Statewide</div><div class="trust-label">Wisconsin coverage</div></div>
  <div class="trust-item"><div class="trust-value">Flat Pricing</div><div class="trust-label">No zone fees</div></div>
  <div class="trust-item"><div class="trust-value">10+ Years</div><div class="trust-label">Industry experience</div></div>
  <div class="trust-item"><div class="trust-value">6 Gyms</div><div class="trust-label">Operator experience</div></div>
  <div class="trust-item"><div class="trust-value">Certified</div><div class="trust-label">Matrix · Precor · Core</div></div>
  <div class="trust-item"><div class="trust-value">Major Brands</div><div class="trust-label">Residential + commercial</div></div>
</div></section>

<section class="section">
  <div class="container scale-grid">
    <div class="reveal">
      <div class="eyebrow">Any scale</div>
      <h2 class="h2 scale-title"><span class="display-line">One machine.</span><span class="display-line red">Or the entire room.</span></h2>
      <p class="lede">Commercial-grade equipment expertise without making a homeowner feel out of place. The same equipment-first team can move a home treadmill or build out a full fitness room.</p>
      <div class="scale-switch" aria-label="Scale example"><button class="is-active" data-focus="small">One machine</button><button data-focus="large">Full facility</button></div>
    </div>
    <div class="scale-visual reveal" data-focus="small">
      <div class="scale-photo scale-photo--large"><img src="/assets/images/hero-completed-installation.webp" alt="Large completed commercial fitness facility" loading="lazy"></div>
      <div class="scale-photo scale-photo--small"><img src="/assets/images/installation-in-progress.webp" alt="Priority Fitness crew assembling equipment in a smaller installation" loading="lazy"></div>
      <div class="scale-arrow">Same equipment team →</div>
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="container">
    <div class="router-header reveal"><div><div class="eyebrow">Skip the service jargon</div><h2 class="h2">What needs to happen to your equipment?</h2></div><p class="lede">Pick the problem in plain English. The interface routes you toward the right service without making you decode a contractor menu.</p></div>
    <div class="router reveal">
      <button class="router-row is-active" data-result="Need a machine, several pieces, or a facility package? Start with Equipment Sourcing." data-cta="Tell Us What You Need" data-url="/services/equipment-sourcing/"><span class="router-row__num">01</span><span class="router-row__title">I need equipment</span><span class="router-row__arrow">→</span></button>
      <button class="router-row" data-result="Already have equipment? Priority Fitness can coordinate installation, assembly, placement, and setup." data-cta="Explore Installation" data-url="/services/equipment-installation/"><span class="router-row__num">02</span><span class="router-row__title">I need it installed</span><span class="router-row__arrow">→</span></button>
      <button class="router-row" data-result="If something is not working right, route directly into equipment-specific repair and service." data-cta="Request Service" data-url="/services/equipment-service-repair/"><span class="router-row__num">03</span><span class="router-row__title">Something isn’t working</span><span class="router-row__arrow">→</span></button>
      <button class="router-row" data-result="Keep equipment inspected and maintained with planned service for residential or commercial settings." data-cta="Explore Maintenance" data-url="/services/preventative-maintenance/"><span class="router-row__num">04</span><span class="router-row__title">I need maintenance</span><span class="router-row__arrow">→</span></button>
      <button class="router-row" data-result="Move equipment within a facility, between locations, or from one home setup to another." data-cta="Move Equipment" data-url="/services/equipment-relocation/"><span class="router-row__num">05</span><span class="router-row__title">I’m moving equipment</span><span class="router-row__arrow">→</span></button>
      <button class="router-row" data-result="Remove obsolete or unwanted fitness equipment and clear the space for what comes next." data-cta="Explore Removal" data-url="/services/equipment-extraction/"><span class="router-row__num">06</span><span class="router-row__title">I need equipment removed</span><span class="router-row__arrow">→</span></button>
      <button class="router-row" data-result="Tell Priority Fitness what equipment you no longer need. Submitting equipment does not guarantee purchase." data-cta="Tell Us About It" data-url="/sell-equipment/"><span class="router-row__num">07</span><span class="router-row__title">I want to sell equipment</span><span class="router-row__arrow">→</span></button>
      <button class="router-row" data-result="For facility-scale needs, start with the project and let Priority Fitness route the equipment work from there." data-cta="Request a Quote" data-url="/request-quote/"><span class="router-row__num">08</span><span class="router-row__title">I need help with a facility</span><span class="router-row__arrow">→</span></button>
    </div>
    <div class="router-result reveal"><p id="routerText">Need a machine, several pieces, or a facility package? Start with Equipment Sourcing.</p><a id="routerCta" class="btn btn--primary" href="/services/equipment-sourcing/">Tell Us What You Need</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="capability-intro reveal"><div><div class="eyebrow">Complete equipment lifecycle</div><h2 class="h2">Everything your equipment needs.</h2></div><p class="lede">Four clear equipment categories cover the full lifecycle without making the visitor hunt through a wall of services.</p></div>
    <div class="capability-list reveal">
      <div class="capability"><span class="capability__index">01 / EQUIPMENT</span><h3>Get the right equipment.</h3><p>Used equipment, equipment sourcing, replacement, and facility-scale equipment needs.</p><div class="capability__links"><a href="/used-equipment/">Used equipment</a><a href="/services/equipment-sourcing/">Equipment sourcing</a></div></div>
      <div class="capability"><span class="capability__index">02 / INSTALLATION</span><h3>Get it where it belongs.</h3><p>Delivery coordination, assembly, placement, and setup for residential and commercial equipment.</p><div class="capability__links"><a href="/services/equipment-installation/">Installation</a></div></div>
      <div class="capability"><span class="capability__index">03 / SERVICE</span><h3>Keep it working.</h3><p>Repair, equipment diagnosis, inspections, preventative maintenance, and facility support.</p><div class="capability__links"><a href="/services/equipment-service-repair/">Repair + service</a><a href="/services/preventative-maintenance/">Maintenance</a></div></div>
      <div class="capability"><span class="capability__index">04 / MOVES + REMOVAL</span><h3>Move on without the headache.</h3><p>Relocation, extraction, removal, replacement coordination, and space-clearing equipment work.</p><div class="capability__links"><a href="/services/equipment-relocation/">Relocation</a><a href="/services/equipment-extraction/">Extraction + removal</a></div></div>
    </div>
  </div>
</section>

<section class="section section--mist">
  <div class="container">
    <div class="project-header reveal"><div><div class="eyebrow">Real Priority Fitness work</div><h2 class="h2">Proof in the room.</h2></div><a class="btn btn--dark" href="/projects/">View Our Work</a></div>
    <div class="project-grid reveal">
      <a class="project-tile" href="/projects/"><img src="/assets/images/finished-cardio-facility.webp" alt="Completed compact fitness room" loading="lazy"><div class="project-caption"><span>Finished facility</span><strong>Compact room complete</strong></div></a>
      <a class="project-tile" href="/projects/"><img src="/assets/images/purple-strength-room.webp" alt="Completed commercial strength room" loading="lazy"><div class="project-caption"><span>Strength facility</span><strong>Full-room buildout</strong></div></a>
      <a class="project-tile" href="/projects/"><img src="/assets/images/finished-strength-wide.webp" alt="Wide completed strength facility" loading="lazy"><div class="project-caption"><span>Commercial install</span><strong>Equipment placed at scale</strong></div></a>
    </div>
  </div>
</section>
{why_priority()}
{certification_strip()}
{social_proof()}
{final_cta()}
'''

# SERVICES HUB
services_body = page_hero('Full lifecycle support','Fitness equipment, from beginning to end.','Six core service areas cover the equipment lifecycle without making you stitch together multiple vendors.','finished-strength-wide.webp','<div class="btn-row"><a class="btn btn--primary" href="/request-quote/">Tell Us What You Need</a><a class="btn btn--light" href="#lifecycle">Explore Services</a></div>') + '''
<section class="section" id="lifecycle"><div class="container"><div class="split-heading reveal"><div><div class="eyebrow">Lifecycle map</div><h2 class="h2">Start where you are.</h2></div><p class="lede">Buy, install, service, maintain, move, replace, or remove. The site routes by the job that needs to happen.</p></div>
<div class="lifecycle-map reveal">
<a href="/services/equipment-sourcing/"><span class="lifecycle-map__num">01</span><strong>Equipment Sourcing</strong><p>Find one piece or plan a larger equipment need.</p></a>
<a href="/services/equipment-installation/"><span class="lifecycle-map__num">02</span><strong>Installation</strong><p>Delivery coordination, assembly, placement, and setup.</p></a>
<a href="/services/equipment-service-repair/"><span class="lifecycle-map__num">03</span><strong>Repair + Service</strong><p>Diagnosis, repair, parts coordination, and equipment support.</p></a>
<a href="/services/preventative-maintenance/"><span class="lifecycle-map__num">04</span><strong>Preventative Maintenance</strong><p>Planned inspections and maintenance to reduce downtime.</p></a>
<a href="/services/equipment-relocation/"><span class="lifecycle-map__num">05</span><strong>Relocation</strong><p>Move fitness equipment inside a facility or between locations.</p></a>
<a href="/services/equipment-extraction/"><span class="lifecycle-map__num">06</span><strong>Extraction + Removal</strong><p>Remove obsolete equipment and clear space for what comes next.</p></a>
<a href="/used-equipment/"><span class="lifecycle-map__num">07</span><strong>Used Equipment</strong><p>Browse current inventory when real equipment is available.</p></a>
<a href="/sell-equipment/"><span class="lifecycle-map__num">08</span><strong>Sell Equipment</strong><p>Tell Priority Fitness what equipment you no longer need.</p></a>
</div></div></section>
<section class="section section--dark"><div class="container image-duo reveal"><figure><img src="/assets/images/installation-in-progress.webp" alt="Fitness equipment installation in progress" loading="lazy"></figure><figure><img src="/assets/images/treadmill-service-corridor.webp" alt="Priority Fitness technicians servicing treadmills" loading="lazy"></figure></div></section>
''' + why_priority() + final_cta('One equipment partner. Every stage that follows.')

service_data = {
'equipment-sourcing': {
    'title':'Equipment Sourcing', 'eyebrow':'Find the right equipment', 'hero':'facility-after.webp',
    'copy':'Need equipment even if it is not sitting in current inventory? Start with the need, not a catalog wall.',
    'cta':'Tell Us What You Need',
    'intro_title':'Equipment sourcing that starts with the room, the need, and the equipment.',
    'intro':['Priority Fitness can help source single machines, multiple pieces, used equipment, or broader facility packages.', 'If current used inventory does not have the right fit, the next step is still simple: tell the team what you are looking for.'],
    'features':[('Single equipment needs','Start with a specific machine or equipment category.'),('Multiple-piece needs','Coordinate several pieces without turning the project into separate conversations.'),('Used equipment','Connect sourcing with current Priority Fitness used inventory when applicable.'),('Facility packages','Support larger commercial equipment needs and completed-space planning.')],
    'audiences':['Home gyms','Commercial gyms','Schools','Hotels + apartments','Municipal facilities','Healthcare + rehabilitation'],
    'process':[('Tell us the need','Describe the equipment, room, or facility goal.'),('Match the route','Current inventory or broader sourcing, depending on the need.'),('Coordinate next steps','Align equipment availability with delivery and installation needs.'),('Finish the lifecycle','Keep Priority Fitness involved for installation, service, moves, or removal.')],
    'images':['finished-cardio-facility.webp','purple-strength-room.webp'],
    'related':[('Installation','/services/equipment-installation/'),('Used Equipment','/used-equipment/'),('Request a Quote','/request-quote/')]
},
'equipment-installation': {
    'title':'Equipment Installation', 'eyebrow':'Equipment going in', 'hero':'hero-installation.webp',
    'copy':'Delivery coordination through final placement, with real Priority Fitness installation work front and center.',
    'cta':'Request Installation Quote',
    'intro_title':'Installation should end with equipment exactly where it belongs.',
    'intro':['Priority Fitness handles fitness-equipment installation for residential and commercial settings, from individual pieces through multi-piece facility work.', 'From equipment arrival through final placement, the work stays focused on the equipment and the finished room.'],
    'features':[('Delivery coordination','Coordinate the equipment arrival with the installation scope.'),('Assembly','Build and assemble fitness equipment for the intended environment.'),('Placement','Position equipment where it belongs in the room or facility.'),('Setup','Finish installation with equipment placed and ready for the next step.')],
    'audiences':['Homes','Commercial gyms','Schools','Colleges + universities','Hotels + multifamily','Community facilities'],
    'process':[('Scope the install','Understand equipment quantity, type, and facility conditions.'),('Coordinate arrival','Align delivery and on-site readiness.'),('Assemble + place','Complete assembly and equipment placement.'),('Close out the room','Finish the installation scope and identify any next equipment need.')],
    'images':['installation-in-progress.webp','hero-completed-installation.webp'],
    'related':[('Equipment Sourcing','/services/equipment-sourcing/'),('Relocation','/services/equipment-relocation/'),('Projects','/projects/')]
},
'equipment-service-repair': {
    'title':'Repair + Service', 'eyebrow':'When equipment stops cooperating', 'hero':'equipment-service.webp',
    'copy':'Fitness-equipment diagnosis and repair for residential and commercial environments, without the generic repair-company look.',
    'cta':'Request Service',
    'intro_title':'Equipment-specific service, not general handyman work.',
    'intro':['Priority Fitness works on fitness equipment across residential and commercial settings, including major brands and manufacturer-service contexts.', 'Residential broken-equipment traffic can route directly into the fixed-price residential service-call landing page.'],
    'features':[('Diagnosis','Identify what is not working and what the equipment needs next.'),('Repair','Complete approved equipment repair work within the service scope.'),('Parts coordination','Coordinate equipment-specific parts when a repair requires them.'),('Facility support','Support commercial sites that need equipment expertise across multiple machines.')],
    'audiences':['Home equipment','Commercial gyms','Hotels + apartments','Schools','Senior living','Healthcare facilities'],
    'process':[('Request service','Tell Priority Fitness what equipment is having an issue.'),('Diagnose','A technician evaluates the equipment and identifies the problem.'),('Approve next work','Additional parts or work can be aligned before proceeding.'),('Restore the equipment','Complete the approved service path and identify maintenance needs if relevant.')],
    'images':['treadmill-service-corridor.webp','finished-cardio-facility.webp'],
    'related':[('Residential Repair','/residential-repair/'),('Preventative Maintenance','/services/preventative-maintenance/'),('Contact','/contact/')]
},
'preventative-maintenance': {
    'title':'Preventative Maintenance', 'eyebrow':'Planned equipment care', 'hero':'treadmill-service-corridor.webp',
    'copy':'A more operational, B2B-forward service page for facilities that want equipment inspected and maintained before downtime becomes the story.',
    'cta':'Request Maintenance Quote',
    'intro_title':'Maintenance is easier when it is planned instead of reactive.',
    'intro':['Priority Fitness supports facilities that need scheduled fitness-equipment attention, condition visibility, and planned service.', 'The service approach is built around the real equipment mix, facility needs, and maintenance goals.'],
    'features':[('Inspections','Create visibility into equipment condition.'),('Scheduled maintenance','Plan recurring equipment attention around facility needs.'),('Condition monitoring','Track issues that may need future service.'),('Downtime reduction','Use planned service to reduce avoidable equipment interruptions.')],
    'audiences':['Commercial gyms','Hotels','Apartments + multifamily','Schools','Senior living','Municipal + healthcare'],
    'process':[('Define the facility','Identify equipment mix, site type, and service goals.'),('Set the service approach','Build the maintenance scope around the real facility.'),('Inspect + maintain','Perform scheduled equipment attention.'),('Plan what is next','Route repairs, replacements, or other equipment work as needed.')],
    'images':['equipment-service.webp','finished-strength-facility.webp'],
    'related':[('Repair + Service','/services/equipment-service-repair/'),('Equipment Sourcing','/services/equipment-sourcing/'),('Request a Quote','/request-quote/')]
},
'equipment-relocation': {
    'title':'Equipment Relocation', 'eyebrow':'Move fitness equipment, not the whole house', 'hero':'equipment-moving.webp',
    'copy':'The people who move full gyms can also move home gyms. Priority Fitness is an equipment mover, not a general moving company.',
    'cta':'Request Moving Quote',
    'intro_title':'One treadmill. A full room. Same equipment-first mindset.',
    'intro':['Priority Fitness can move fitness equipment within facilities, between locations, or as part of residential and commercial equipment projects.', 'The focus stays on disassembly, movement, reassembly, and placement of fitness equipment rather than furniture or household moving.'],
    'features':[('In-facility moves','Reposition fitness equipment inside the same site.'),('Commercial relocations','Move equipment between commercial locations or facility spaces.'),('Home gym moves','Move residential fitness equipment without becoming a whole-house mover.'),('Disassembly + reassembly','Break down and rebuild equipment when the move requires it.')],
    'audiences':['Home gyms','Commercial gyms','Schools','Hotels + apartments','Corporate wellness','Community facilities'],
    'process':[('Tell us what is moving','Identify equipment, quantity, origin, and destination.'),('Plan the movement','Determine disassembly, access, handling, and placement needs.'),('Move the equipment','Handle the equipment-specific relocation work.'),('Reassemble + place','Finish with the equipment positioned in its new space.')],
    'images':['moving-delivery.webp','installation-in-progress.webp'],
    'related':[('Installation','/services/equipment-installation/'),('Extraction + Removal','/services/equipment-extraction/'),('Request a Quote','/request-quote/')]
},
'equipment-extraction': {
    'title':'Extraction + Removal', 'eyebrow':'Make room for what comes next', 'hero':'moving-delivery.webp',
    'copy':'Remove obsolete, unwanted, or replacement-bound fitness equipment without making unsupported disposal or recycling promises.',
    'cta':'Request Removal Quote',
    'intro_title':'Equipment out, space back.',
    'intro':['Priority Fitness supports equipment removal, extraction, facility cleanout, and replacement-oriented projects where fitness equipment needs to leave the space.', 'Removal can connect directly to relocation, replacement, installation, or equipment sourcing when the project continues beyond extraction.'],
    'features':[('Equipment removal','Remove fitness equipment that no longer belongs in the space.'),('Facility cleanout','Coordinate larger equipment-removal scopes.'),('Replacement projects','Connect old-equipment removal with the next equipment phase.'),('Relocation coordination','Separate what is leaving permanently from what is moving elsewhere.')],
    'audiences':['Commercial gyms','Schools','Hotels + apartments','Municipal facilities','Healthcare','Residential equipment'],
    'process':[('Identify what leaves','Clarify equipment quantity, type, and site conditions.'),('Plan extraction','Account for access, disassembly, and movement path.'),('Remove equipment','Complete the equipment-focused extraction scope.'),('Route the next phase','Connect to relocation, sourcing, replacement, or installation if needed.')],
    'images':['facility-before.webp','equipment-moving.webp'],
    'related':[('Relocation','/services/equipment-relocation/'),('Equipment Sourcing','/services/equipment-sourcing/'),('Installation','/services/equipment-installation/')]
}
}


def service_page(slug, d):
    feats=''.join(f'''<div class="feature-row"><div class="feature-row__num">{i:02d}</div><div class="feature-row__name">{t}</div><div class="feature-row__desc">{desc}</div></div>''' for i,(t,desc) in enumerate(d['features'],1))
    aud=''.join(f'''<div class="audience-item"><strong>{a}</strong><span>Fitness-equipment support scaled to the environment.</span></div>''' for a in d['audiences'])
    proc=''.join(f'''<div class="process-step"><div class="process-step__num">{i:02d}</div><h3>{t}</h3><p>{desc}</p></div>''' for i,(t,desc) in enumerate(d['process'],1))
    related=''.join(f'''<a class="related-link" href="{url}"><span>Related</span><strong>{name}</strong></a>''' for name,url in d['related'])
    hero_btn=f'''<div class="btn-row"><a class="btn btn--primary" href="/request-quote/">{d['cta']}</a><a class="btn btn--light" href="tel:+19207653644">Call Priority Fitness</a></div>'''
    mobile_action = '''<div class="sticky-mobile-action"><a href="tel:+19207653644">Call</a><a href="/request-quote/">Request Service</a></div>''' if slug in ['equipment-service-repair','equipment-relocation','equipment-extraction'] else ''
    bclass = 'has-mobile-action' if mobile_action else ''
    content = page_hero(d['eyebrow'],d['title'],d['copy'],d['hero'],hero_btn, position='center') + f'''
<section class="section"><div class="container"><div class="intro-grid reveal"><div><div class="eyebrow">Service overview</div><h2 class="h2">{d['intro_title']}</h2></div><div class="intro-copy"><p>{d['intro'][0]}</p><p>{d['intro'][1]}</p><a class="text-link" href="/request-quote/">{d['cta']}</a></div></div><div class="feature-rows reveal">{feats}</div></div></section>
<section class="section section--dark"><div class="container"><div class="split-heading reveal"><div><div class="eyebrow">How it works</div><h2 class="h2">A clear path from problem to done.</h2></div><p class="lede">The exact scope changes with the equipment and site. The interaction stays simple.</p></div><div class="process-grid reveal">{proc}</div></div></section>
<section class="section"><div class="container"><div class="split-heading reveal"><div><div class="eyebrow">Built for the real environment</div><h2 class="h2">Who this service is for.</h2></div><p class="lede">Residential accessibility and commercial credibility live under the same Priority Fitness identity.</p></div><div class="audience-grid reveal">{aud}</div></div></section>
<section class="section section--mist"><div class="container image-duo reveal"><figure><img src="/assets/images/{d['images'][0]}" alt="Priority Fitness {d['title'].lower()} work" loading="lazy"></figure><figure><img src="/assets/images/{d['images'][1]}" alt="Priority Fitness fitness-equipment project" loading="lazy"></figure></div></section>
{why_priority()}
<section class="section"><div class="container"><div class="eyebrow">Keep moving through the lifecycle</div><h2 class="h2" style="margin-bottom:32px">Related services.</h2><div class="related-services reveal">{related}</div></div></section>
{final_cta()}{mobile_action}'''
    return page(d['title'], content, d['copy'], bclass)

# Residential repair
res_buttons='<div class="btn-row"><a class="btn btn--primary" href="#repair-request">Request Residential Repair</a><a class="btn btn--light" href="tel:+19207653644">Call Priority Fitness</a></div>'
res_hero = '''<section class="page-hero">
  <div class="page-hero__media"><img src="/assets/images/equipment-service.webp" alt="Priority Fitness technician servicing fitness equipment" style="object-position:center 48%" fetchpriority="high"></div>
  <div class="page-hero__overlay"></div>
  <div class="container page-hero__content"><div class="eyebrow">Residential repair · statewide Wisconsin</div><h1>Residential equipment repair.</h1><div class="page-hero__price">$159<small>Residential repair service call</small></div><p>One clear service-call price that includes statewide Wisconsin travel, equipment diagnosis, and approximately one hour of technician labor.</p>''' + res_buttons + '</div></section>'
res_body = res_hero + '''
<section class="section"><div class="container offer-grid"><div class="offer-price reveal"><div class="eyebrow">Simple up front</div><div class="offer-price__value">$159</div><div class="offer-price__label">Residential repair service call</div><p class="price-note">Additional parts are separate. Complex additional labor is separate. Additional work should be approved before proceeding.</p></div><div class="reveal"><div class="eyebrow">Included</div><h2 class="h2" style="margin-bottom:28px">Problem → price → trust → service.</h2><div class="inclusion-list"><div class="inclusion"><div class="inclusion__mark">✓</div><div><strong>Statewide Wisconsin travel</strong><p>Travel for the service call is included in the confirmed $159 offer.</p></div></div><div class="inclusion"><div class="inclusion__mark">✓</div><div><strong>Equipment diagnosis</strong><p>Technician diagnosis of the equipment issue.</p></div></div><div class="inclusion"><div class="inclusion__mark">✓</div><div><strong>Approximately one hour of technician labor</strong><p>The confirmed service-call inclusion before additional approved work.</p></div></div></div><div class="btn-row" style="margin-top:28px"><a class="btn btn--primary" href="#repair-request">Request Residential Repair</a><a class="btn btn--outline" href="tel:+19207653644">Call Priority Fitness</a></div></div></div></section>
<section class="section section--dark"><div class="container"><div class="split-heading reveal"><div><div class="eyebrow">Why trust the service call</div><h2 class="h2">Equipment people, not a generic repair crew.</h2></div><p class="lede">Confirmed Matrix, Precor, and Core certifications, major-brand fitness-equipment experience, statewide coverage, and operator experience through six affiliated gyms.</p></div><div class="stat-pair reveal"><div><div class="stat-big">4.6 ★</div><div class="stat-caption">Google rating</div></div><div><div class="stat-big">No zone fees</div><div class="stat-caption">Flat statewide pricing</div></div></div></div></section>
''' + certification_strip() + '''
<section class="section" id="repair-request"><div class="container contact-grid"><div class="reveal"><div class="eyebrow">Request residential repair</div><h2 class="h2">Tell us what is happening.</h2><p class="lede">Share the equipment and issue so the right service path can start with useful information.</p></div><form class="form-shell reveal" data-front-end-only><div class="form-grid"><div class="field"><label for="rr-name">Name</label><input id="rr-name" name="name" autocomplete="name" required></div><div class="field"><label for="rr-phone">Phone</label><input id="rr-phone" name="phone" autocomplete="tel" required></div><div class="field"><label for="rr-email">Email</label><input id="rr-email" type="email" name="email" autocomplete="email"></div><div class="field"><label for="rr-location">Location</label><input id="rr-location" name="location" placeholder="City or ZIP"></div><div class="field"><label for="rr-brand">Equipment brand</label><input id="rr-brand" name="brand"></div><div class="field"><label for="rr-type">Equipment type</label><input id="rr-type" name="equipment_type" placeholder="Treadmill, bike, strength, etc."></div><div class="field field--full"><label for="rr-issue">What is the equipment doing?</label><textarea id="rr-issue" name="issue"></textarea></div><div class="field field--full"><button class="btn btn--primary" type="submit">Request Residential Repair</button><p class="integration-hook form-note" role="status">This form is in preview mode and is ready for the live submission connection.</p></div></div></form></div></section>
''' + final_cta('Broken equipment should not become a research project.') + '<div class="sticky-mobile-action"><a href="tel:+19207653644">Call</a><a href="#repair-request">Request Service</a></div>'

# Health check placeholder
health_body = page_hero('Planned offer page','$49 Equipment Health Check','The offer page is structured around the confirmed $49 Health Check and $99 Deluxe Tune-Up pricing. Final inclusions can be added once approved.','equipment-service.webp','<div class="btn-row"><a class="btn btn--primary" href="#health-structure">View Offer Structure</a><a class="btn btn--light" href="tel:+19207653644">Call Priority Fitness</a></div>', True) + '''
<section class="section" id="health-structure"><div class="container intro-grid"><div class="reveal"><div class="eyebrow">Offer hierarchy</div><h2 class="h2">$49 health check.<br><span class="red">$99 deluxe tune-up.</span></h2><p class="lede">The price hierarchy and comparison structure are ready for the final approved Health Check and Deluxe Tune-Up inclusions.</p></div><div class="placeholder-panel reveal"><span class="placeholder-label">Awaiting approved inclusions</span><h3>Health Check inclusions</h3><div class="placeholder-lines"><div class="placeholder-line"></div><div class="placeholder-line"></div><div class="placeholder-line"></div></div><hr style="border:0;border-top:1px solid #ddd;margin:30px 0"><h3>Deluxe Tune-Up order bump</h3><div class="placeholder-lines"><div class="placeholder-line"></div><div class="placeholder-line"></div><div class="placeholder-line"></div></div></div></div></section>
''' + certification_strip() + final_cta('Get the equipment checked before a small issue becomes the whole afternoon.')

# Used equipment
used_body = page_hero('Inquiry-based inventory','Used Equipment','Browse current Priority Fitness equipment when inventory is available, then ask about the item directly.','finished-cardio-facility.webp','<div class="btn-row"><a class="btn btn--primary" href="#inventory">Browse Inventory</a><a class="btn btn--light" href="/services/equipment-sourcing/">Need Something Specific?</a></div>', True) + '''
<section class="section" id="inventory"><div class="container"><div class="split-heading reveal"><div><div class="eyebrow">Current inventory</div><h2 class="h2">Browse → view → ask.</h2></div><p class="lede">Inventory changes frequently. If nothing is listed right now, Priority Fitness can still help source what you need.</p></div><div class="filter-bar reveal" aria-label="Inventory filters"><div class="field"><label>Equipment Type</label><select><option>All types</option></select></div><div class="field"><label>Brand</label><select><option>All brands</option></select></div><div class="field"><label>Condition</label><select><option>All conditions</option></select></div><div class="field"><label>Availability</label><select><option>Available + pending</option></select></div></div><div class="empty-state reveal"><div class="empty-state__inner"><div class="eyebrow">Looking for something specific?</div><h2 class="h2">Inventory changes frequently.</h2><p>Looking for something specific? Tell Priority Fitness what you need and route directly into Equipment Sourcing.</p><div class="btn-row" style="justify-content:center"><a class="btn btn--primary" href="/services/equipment-sourcing/">Tell Us What You Need</a><a class="btn btn--outline" href="/request-quote/">Request a Quote</a></div></div></div></div></section>
<section class="section section--dark"><div class="container"><div class="split-heading reveal"><div><div class="eyebrow">Inventory UX rules</div><h2 class="h2">Only real data gets a line.</h2></div><p class="lede">Each equipment listing is designed to show only the details that are actually known, with a direct inquiry path instead of a checkout flow.</p></div><div class="stat-pair reveal"><div><div class="stat-big">Available</div><div class="stat-caption">Active inquiry</div></div><div><div class="stat-big">Pending / Sold</div><div class="stat-caption">Clear status treatment + sourcing route</div></div></div></div></section>
''' + final_cta('Can’t find it in inventory? Start with what you need.')

# Industries
industries_body = page_hero('Residential + commercial','Industries','Priority Fitness serves homes and commercial facilities without splitting the company into two identities.','hero-completed-installation.webp','<div class="btn-row"><a class="btn btn--primary" href="/request-quote/">Tell Us About Your Facility</a><a class="btn btn--light" href="/services/">View Services</a></div>', True) + '''
<section class="section"><div class="container"><div class="split-heading reveal"><div><div class="eyebrow">Built around the equipment</div><h2 class="h2">Different facilities. Same lifecycle.</h2></div><p class="lede">The audience changes. The equipment needs are still sourcing, installation, maintenance, repair, moving, replacement, and removal.</p></div><div class="industry-groups reveal">
<div class="industry-group"><h3>Residential</h3><div class="industry-list"><span>Homes</span><span>Home gyms</span></div></div>
<div class="industry-group"><h3>Fitness + education</h3><div class="industry-list"><span>Commercial gyms</span><span>Schools</span><span>Colleges / Universities</span><span>Community facilities</span></div></div>
<div class="industry-group"><h3>Property + hospitality</h3><div class="industry-list"><span>Hotels</span><span>Apartments / Multifamily</span><span>Senior living</span><span>Corporate wellness</span></div></div>
<div class="industry-group"><h3>Public + healthcare</h3><div class="industry-list"><span>Municipalities</span><span>Healthcare</span><span>Rehabilitation</span><span>Behavioral health / Recovery</span></div></div>
<div class="industry-group"><h3>Industry partners</h3><div class="industry-list"><span>Manufacturers</span><span>Manufacturer representatives</span><span>Service / Dispatch partners</span></div></div>
</div></div></section>
''' + '''
<section class="section section--dark"><div class="container image-duo reveal"><figure><img src="/assets/images/facility-after.webp" alt="Completed fitness facility with strength, cardio, and turf" loading="lazy"></figure><figure><img src="/assets/images/school-racks-after.webp" alt="School weight room rack installation" loading="lazy"></figure></div></section>
''' + why_priority() + final_cta('One machine, one facility, or a statewide equipment need.')

# Sell equipment
sell_body = page_hero('Equipment you no longer need','Sell Your Equipment','Tell Priority Fitness what you have. Submitting equipment does not guarantee that Priority Fitness will purchase it.','moving-delivery.webp','<div class="btn-row"><a class="btn btn--primary" href="#sell-form">Tell Us About It</a><a class="btn btn--light" href="tel:+19207653644">Call Priority Fitness</a></div>', True) + '''
<section class="section" id="sell-form"><div class="container contact-grid"><div class="reveal"><div class="eyebrow">Start with the equipment</div><h2 class="h2">Have equipment you no longer need?</h2><p class="lede">Share the equipment type, quantity, condition, and photos so Priority Fitness can understand what you have.</p></div><form class="form-shell reveal" data-front-end-only><div class="form-grid"><div class="field"><label for="se-name">Name</label><input id="se-name" name="name" required></div><div class="field"><label for="se-company">Company / Facility</label><input id="se-company" name="company"></div><div class="field"><label for="se-phone">Phone</label><input id="se-phone" name="phone" required></div><div class="field"><label for="se-email">Email</label><input id="se-email" type="email" name="email"></div><div class="field"><label for="se-location">Location</label><input id="se-location" name="location"></div><div class="field"><label for="se-type">Equipment Type</label><input id="se-type" name="type"></div><div class="field"><label for="se-brand">Brand</label><input id="se-brand" name="brand"></div><div class="field"><label for="se-model">Model</label><input id="se-model" name="model"></div><div class="field"><label for="se-qty">Quantity</label><input id="se-qty" type="number" min="1" name="quantity"></div><div class="field"><label for="se-condition">Condition</label><select id="se-condition" name="condition"><option value="">Select</option><option>Working</option><option>Needs service</option><option>Unknown</option></select></div><div class="field field--full"><label for="se-photos">Photos</label><input id="se-photos" type="file" name="photos" multiple accept="image/*"></div><div class="field field--full"><label for="se-info">Additional Information</label><textarea id="se-info" name="additional_information"></textarea></div><div class="field field--full"><button class="btn btn--primary" type="submit">Tell Us About This Equipment</button><p class="integration-hook form-note" role="status">This form is in preview mode and is ready for the live submission connection.</p></div></div></form></div></section>
''' + final_cta('Equipment leaving your room can be the start of the next equipment plan.')

# Projects
projects_body = page_hero('Real work only','Projects','Installation, service, relocation, moving, strength, cardio, and removal work from real Priority Fitness projects.','finished-strength-wide.webp','<div class="btn-row"><a class="btn btn--primary" href="#project-gallery">View Projects</a><a class="btn btn--light" href="/request-quote/">Start a Project</a></div>', True) + '''
<section class="section" id="project-gallery"><div class="container"><div class="split-heading reveal"><div><div class="eyebrow">Real work</div><h2 class="h2">The work can speak visually.</h2></div><p class="lede">Browse real Priority Fitness project photography by the kind of equipment work shown.</p></div><div class="filter-tabs reveal" role="group" aria-label="Project filters"><button class="filter-tab is-active" data-filter="all">All</button><button class="filter-tab" data-filter="installations">Installations</button><button class="filter-tab" data-filter="service">Service</button><button class="filter-tab" data-filter="relocation">Relocation</button><button class="filter-tab" data-filter="moves">Moves</button><button class="filter-tab" data-filter="strength">Strength</button><button class="filter-tab" data-filter="cardio">Cardio</button></div><div class="masonry reveal">
<figure class="masonry-item" data-category="installations strength"><img src="/assets/images/purple-strength-room.webp" alt="Completed commercial strength facility"><figcaption>Completed strength room</figcaption></figure>
<figure class="masonry-item" data-category="service cardio"><img src="/assets/images/treadmill-service-corridor.webp" alt="Priority Fitness technicians servicing treadmills"><figcaption>Service · Cardio</figcaption></figure>
<figure class="masonry-item" data-category="installations strength"><img src="/assets/images/hero-installation.webp" alt="Equipment installation in progress"><figcaption>Installation</figcaption></figure>
<figure class="masonry-item" data-category="service cardio"><img src="/assets/images/equipment-service.webp" alt="Technicians servicing cardio equipment"><figcaption>Service · Cardio</figcaption></figure>
<figure class="masonry-item" data-category="installations cardio"><img src="/assets/images/finished-cardio-facility.webp" alt="Completed cardio facility"><figcaption>Completed cardio room</figcaption></figure>
<figure class="masonry-item" data-category="installations strength"><img src="/assets/images/finished-strength-facility.webp" alt="Completed strength facility"><figcaption>Completed strength room</figcaption></figure>
<figure class="masonry-item" data-category="moves relocation"><img src="/assets/images/equipment-moving.webp" alt="Fitness equipment being moved from a truck"><figcaption>Equipment move</figcaption></figure>
<figure class="masonry-item" data-category="installations cardio"><img src="/assets/images/hero-completed-installation.webp" alt="Completed equipment installation"><figcaption>Completed installation</figcaption></figure>
<figure class="masonry-item" data-category="installations"><img src="/assets/images/installation-in-progress.webp" alt="Installation work in progress"><figcaption>Installation in progress</figcaption></figure>
<figure class="masonry-item" data-category="moves relocation"><img src="/assets/images/moving-delivery.webp" alt="Priority Fitness crew moving equipment"><figcaption>Move · Relocation</figcaption></figure>
</div></div></section>
<section class="section section--mist"><div class="container"><div class="split-heading reveal"><div><div class="eyebrow">Before → after</div><h2 class="h2">The room is part of the proof.</h2></div><p class="lede">Two real transformations shown without invented client names, locations, or project claims.</p></div><div class="project-comparisons">
<article class="comparison-pair reveal"><div class="comparison-copy"><span class="comparison-index">01</span><h3>From open room to equipped facility.</h3><p>The same space before equipment and after the fitness room was built out.</p></div><div class="comparison-images"><figure class="comparison-frame"><img src="/assets/images/facility-before.webp" alt="Fitness room before equipment installation" loading="lazy"><figcaption>Before</figcaption></figure><figure class="comparison-frame"><img src="/assets/images/facility-after.webp" alt="Fitness room after equipment installation" loading="lazy"><figcaption>After</figcaption></figure></div></article>
<article class="comparison-pair reveal"><div class="comparison-copy"><span class="comparison-index">02</span><h3>Rack setup, reworked.</h3><p>A school weight-room rack setup before and after the equipment update.</p></div><div class="comparison-images"><figure class="comparison-frame"><img src="/assets/images/school-racks-before.webp" alt="School weight room before rack update" loading="lazy"><figcaption>Before</figcaption></figure><figure class="comparison-frame"><img src="/assets/images/school-racks-after.webp" alt="School weight room after rack update" loading="lazy"><figcaption>After</figcaption></figure></div></article>
</div></div></section>
''' + final_cta('Need your room to become the next proof point?')

# About
about_body = page_hero('Wisconsin-based fitness-equipment specialists','About Priority Fitness','A technician perspective, a facility-operator perspective, and approximately 10 years in the fitness industry.','finished-strength-facility.webp','<div class="btn-row"><a class="btn btn--primary" href="/request-quote/">Work With Priority Fitness</a><a class="btn btn--light" href="/projects/">See the Work</a></div>', True) + '''
<section class="section"><div class="container reveal"><div class="eyebrow">The strategic difference</div><div class="operator-statement"><span class="display-line">We don’t just service gyms.</span><span class="display-line line-2">We run six of them.</span></div></div></section>
<section class="section section--mist"><div class="container story-grid"><div class="story-image reveal"><img src="/assets/images/installation-in-progress.webp" alt="Priority Fitness crew assembling fitness equipment" loading="lazy"></div><div class="story-copy reveal"><div class="eyebrow">Owner · Colton Burt</div><h2 class="h2">Equipment decisions seen from both sides.</h2><p>Priority Fitness combines fitness-equipment service experience with the perspective that comes from operating six affiliated gyms.</p><p>The result is a practical view of what facility operators care about: equipment availability, room flow, serviceability, downtime, placement, replacement, and the next problem that could appear after the current one is solved.</p><div class="hr-red"></div><p>Confirmed proof includes statewide Wisconsin coverage, flat statewide pricing with no zone fees, Matrix / Precor / Core certifications, major-brand service capability, and approximately 10 years in the fitness industry.</p></div></div></section>
''' + certification_strip() + why_priority() + final_cta('From technician work to operator decisions, the equipment stays the priority.')

# Contact
contact_body = page_hero('One front door','Contact Priority Fitness','Residential repair, commercial service, installation, sourcing, used equipment, equipment moving, manufacturer / dispatch, or a general equipment question.','hero-completed-installation.webp','<div class="btn-row"><a class="btn btn--primary" href="#contact-form">Tell Us What You Need</a><a class="btn btn--light" href="tel:+19207653644">920-765-3644</a></div>', True) + '''
<section class="section" id="contact-form"><div class="container contact-grid"><div class="reveal"><div class="eyebrow">Direct contact</div><h2 class="h2">Make the next step obvious.</h2><div class="contact-stack"><div class="contact-row"><span>Phone</span><a href="tel:+19207653644">920-765-3644</a></div><div class="contact-row"><span>Email</span><a href="mailto:support@pf-pros.com">support@pf-pros.com</a></div><div class="contact-row"><span>Street</span><strong>433 S Industrial Park Rd</strong></div><div class="contact-row"><span>Hours</span><strong>8:00 AM–5:00 PM</strong></div><div class="contact-row"><span>Social</span><a href="https://www.facebook.com/priorityfitnesspros" target="_blank" rel="noopener">Facebook ↗</a></div></div></div><form class="form-shell reveal" data-front-end-only><div class="form-grid"><div class="field"><label for="c-name">Name</label><input id="c-name" name="name" required></div><div class="field"><label for="c-company">Company / Facility</label><input id="c-company" name="company"></div><div class="field"><label for="c-phone">Phone</label><input id="c-phone" name="phone" required></div><div class="field"><label for="c-email">Email</label><input id="c-email" type="email" name="email"></div><div class="field field--full"><label for="c-topic">What do you need help with?</label><select id="c-topic" name="topic"><option>Residential Repair</option><option>Commercial Service</option><option>Installation</option><option>Equipment Sourcing</option><option>Used Equipment</option><option>Equipment Moving</option><option>Manufacturer / Dispatch</option><option>General Inquiry</option></select></div><div class="field field--full"><label for="c-message">Tell us about it</label><textarea id="c-message" name="message"></textarea></div><div class="field field--full"><button class="btn btn--primary" type="submit">Send Inquiry</button><p class="integration-hook form-note" role="status">This form is in preview mode and is ready for the live submission connection.</p></div></div></form></div></section>
'''

# Request quote wizard
quote_body = page_hero('Guided request','Request a Quote','Start with what needs to happen to the equipment. The interface gets specific only after the visitor chooses the job.','hero-installation.webp','<div class="btn-row"><a class="btn btn--primary" href="#quote">Start Request</a><a class="btn btn--light" href="tel:+19207653644">Call Priority Fitness</a></div>', True) + '''
<section class="section section--mist" id="quote"><div class="container quote-shell"><aside class="quote-progress reveal"><div class="eyebrow">Guided request</div><h2 class="h2">Tell us the job, not the jargon.</h2><p id="quoteProgressLabel" class="muted">Step 1 of 3</p><div class="quote-progress__track"><div class="quote-progress__bar"></div></div><p class="muted">The request stays short up front and only asks for equipment details after you choose the kind of help you need.</p></aside><form id="quoteWizard" class="form-shell reveal"><input type="hidden" name="request_type"><section class="quote-step is-active"><h2>What do you need help with?</h2><div class="option-grid"><button type="button" class="option-button" data-value="Buy equipment">Buy equipment</button><button type="button" class="option-button" data-value="Find / source equipment">Find / source equipment</button><button type="button" class="option-button" data-value="Install equipment">Install equipment</button><button type="button" class="option-button" data-value="Repair equipment">Repair equipment</button><button type="button" class="option-button" data-value="Maintain equipment">Maintain equipment</button><button type="button" class="option-button" data-value="Move equipment">Move equipment</button><button type="button" class="option-button" data-value="Remove equipment">Remove equipment</button><button type="button" class="option-button" data-value="Replace equipment">Replace equipment</button><button type="button" class="option-button" data-value="Sell equipment">Sell equipment</button><button type="button" class="option-button" data-value="Commercial facility support">Commercial facility support</button><button type="button" class="option-button" data-value="Other">Other</button></div><div class="quote-nav"><button class="btn btn--outline" type="button" data-prev hidden>Back</button><button class="btn btn--primary" type="button" data-next>Continue</button></div></section><section class="quote-step"><h2>Tell us about the equipment.</h2><div class="form-grid"><div class="field"><label for="q-type">Equipment type</label><input id="q-type" name="equipment_type" placeholder="Treadmill, strength, full room, etc."></div><div class="field"><label for="q-brand">Brand, if known</label><input id="q-brand" name="brand"></div><div class="field"><label for="q-qty">Quantity, if known</label><input id="q-qty" name="quantity"></div><div class="field"><label for="q-location">Location</label><input id="q-location" name="location" placeholder="City or ZIP"></div><div class="field field--full"><label for="q-details">What needs to happen?</label><textarea id="q-details" name="details"></textarea></div></div><div class="quote-nav"><button class="btn btn--outline" type="button" data-prev>Back</button><button class="btn btn--primary" type="button" data-next>Continue</button></div></section><section class="quote-step"><h2>How should Priority Fitness reach you?</h2><div class="form-grid"><div class="field"><label for="q-name">Name</label><input id="q-name" name="name" required></div><div class="field"><label for="q-company">Company / Facility</label><input id="q-company" name="company"></div><div class="field"><label for="q-phone">Phone</label><input id="q-phone" name="phone" required></div><div class="field"><label for="q-email">Email</label><input id="q-email" type="email" name="email"></div></div><div class="quote-nav"><button class="btn btn--outline" type="button" data-prev>Back</button><button class="btn btn--primary" type="submit">Submit Request</button></div><p class="integration-hook form-note" role="status">This form is in preview mode and is ready for the live submission connection.</p></section></form></div></section>
'''

# Write pages
pages = {
    'index.html': page('Home', home_body, 'Priority Fitness handles fitness equipment from sourcing and installation through repair, relocation, replacement, and removal.'),
    'services/index.html': page('Services', services_body),
    'residential-repair/index.html': page('Residential Repair', res_body, '$159 residential fitness-equipment repair service call across Wisconsin.', 'has-mobile-action'),
    'equipment-health-check/index.html': page('Equipment Health Check', health_body),
    'used-equipment/index.html': page('Used Equipment', used_body),
    'industries/index.html': page('Industries', industries_body),
    'sell-equipment/index.html': page('Sell Your Equipment', sell_body),
    'projects/index.html': page('Projects', projects_body),
    'about/index.html': page('About', about_body),
    'contact/index.html': page('Contact', contact_body),
    'request-quote/index.html': page('Request a Quote', quote_body),
}
for slug,d in service_data.items():
    pages[f'services/{slug}/index.html'] = service_page(slug,d)

for rel, html in pages.items():
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding='utf-8')

# Add responsive image metadata to generated HTML. Supplied photography remains the source of truth.
try:
    from bs4 import BeautifulSoup
    from PIL import Image
    for rel in pages:
        path = ROOT / rel
        soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
        for img in soup.find_all('img'):
            src = img.get('src','')
            if not src.startswith('/assets/images/'):
                continue
            asset = ROOT / src.lstrip('/')
            if not asset.exists():
                continue
            with Image.open(asset) as im:
                w,h = im.size
            if not img.has_attr('width'):
                img['width'] = str(w)
            if not img.has_attr('height'):
                img['height'] = str(h)
            if src.endswith('.webp'):
                stem = src[:-5]
                candidates=[]
                for width in (720,1080):
                    candidate = ROOT / f'{stem.lstrip("/")}-{width}.webp'
                    if candidate.exists():
                        candidates.append(f'{stem}-{width}.webp {width}w')
                candidates.append(f'{src} {w}w')
                img['srcset'] = ', '.join(candidates)
                full_width = bool(img.find_parent(class_=['hero-media','page-hero__media','cta-band__bg']))
                img['sizes'] = '100vw' if full_width else '(max-width: 820px) 100vw, 60vw'
                if not img.has_attr('loading') and img.get('fetchpriority') != 'high':
                    img['loading'] = 'lazy'
        path.write_text(str(soup), encoding='utf-8')
except Exception as exc:
    print(f'Image enhancement skipped: {exc}')

print(f'Built {len(pages)} pages')

import make_portable
make_portable.main()

import seo
for rel in pages:
    path = ROOT / rel
    path.write_text(seo.add_seo_tags(rel, path.read_text(encoding='utf-8')), encoding='utf-8')
