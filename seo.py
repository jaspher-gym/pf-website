"""Add SEO head tags (canonical, Open Graph, Twitter, JSON-LD) to a built page.

Titles and descriptions are read from the page itself, so editing them in
build.py is enough to update the social previews too. URLs are absolute, so
make_portable.py leaves them untouched.

build.py calls add_seo_tags() for every page. Safe to run repeatedly.
"""
from html import escape, unescape
import json
import re

SITE = 'https://pf-pros.com'
SHARE_IMAGE = (f'{SITE}/assets/images/hero-installation-1080.webp', 1080, 613)

ORGANIZATION = {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    'name': 'Priority Fitness',
    'url': f'{SITE}/',
    'logo': f'{SITE}/assets/images/priority-fitness-logo.png',
    'image': SHARE_IMAGE[0],
    'telephone': '+1-920-765-3644',
    'email': 'support@pf-pros.com',
    'sameAs': [
        'https://www.facebook.com/priorityfitnesspros',
        'https://www.google.com/search?kgmid=/g/11jtz8fwsj',
    ],
}

TITLE_RE = re.compile(r'<title>(.*?)</title>', re.S)
DESC_RE = re.compile(r'<meta (?:content="([^"]*)" name="description"|name="description" content="([^"]*)")')


def canonical_url(rel):
    """'about/index.html' -> 'https://pf-pros.com/about/'"""
    path = rel.replace('\\', '/')
    path = path[:-len('index.html')] if path.endswith('index.html') else path
    return f'{SITE}/{path}'


def seo_tags(rel, html):
    title = unescape(TITLE_RE.search(html).group(1).strip())
    m = DESC_RE.search(html)
    desc = unescape(m.group(1) or m.group(2)) if m else ''
    url = canonical_url(rel)
    img, w, h = SHARE_IMAGE
    a = lambda s: escape(s, quote=True)
    tags = [
        f'<link href="{url}" rel="canonical"/>',
        '<meta content="website" property="og:type"/>',
        '<meta content="Priority Fitness" property="og:site_name"/>',
        f'<meta content="{url}" property="og:url"/>',
        f'<meta content="{a(title)}" property="og:title"/>',
        f'<meta content="{a(desc)}" property="og:description"/>',
        f'<meta content="{img}" property="og:image"/>',
        f'<meta content="{w}" property="og:image:width"/>',
        f'<meta content="{h}" property="og:image:height"/>',
        '<meta content="summary_large_image" name="twitter:card"/>',
    ]
    if url == f'{SITE}/':
        tags.append('<script type="application/ld+json">' + json.dumps(ORGANIZATION, separators=(',', ':')) + '</script>')
    return '\n'.join(tags)


def add_seo_tags(rel, html):
    if 'rel="canonical"' in html:
        return html
    return html.replace('</head>', seo_tags(rel, html) + '\n</head>', 1)
