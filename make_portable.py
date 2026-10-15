"""Rewrite root-relative URLs in the built HTML to relative ones.

The site is authored with root-relative URLs (/assets/..., /about/), which only
resolve when served from a web server root. After this pass every page works
from any web server, at the domain root or in a subfolder:

- /assets/css/styles.css  ->  ../assets/css/styles.css
- /about/                 ->  ../about/
- icons.svg sprite is inlined, because browsers block external <use> refs on file://

Safe to run repeatedly. build.py calls it automatically after generating pages.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SKIP_DIRS = {'templates', '__pycache__', '.git', 'node_modules'}

ATTR_RE = re.compile(r'(\s(?:href|src|data-image|data-url)=")(/(?!/)[^"]*)"')
SRCSET_RE = re.compile(r'(\ssrcset=")([^"]*)"')
USE_RE = re.compile(r'href="(?:[./]*)assets/icons\.svg(#[^"]+)"')
SPRITE_MARKER = 'id="pf-icon-sprite"'


def rel_url(url, prefix):
    # Page links keep their clean folder form (../about/), not ../about/index.html
    path, sep, frag = url.partition('#')
    path = path.lstrip('/')
    out = prefix + path
    if out == '':
        out = './'
    return out + (sep + frag if sep else '')


def sprite_markup():
    svg = (ROOT / 'assets' / 'icons.svg').read_text(encoding='utf-8')
    return svg.replace('<svg ', f'<svg {SPRITE_MARKER} aria-hidden="true" style="display:none" ', 1)


def convert(html, prefix):
    html = ATTR_RE.sub(lambda m: f'{m.group(1)}{rel_url(m.group(2), prefix)}"', html)

    def fix_srcset(m):
        parts = []
        for item in m.group(2).split(','):
            bits = item.strip().split(None, 1)
            if bits and bits[0].startswith('/') and not bits[0].startswith('//'):
                bits[0] = rel_url(bits[0], prefix)
            parts.append(' '.join(bits))
        return f'{m.group(1)}{", ".join(parts)}"'
    html = SRCSET_RE.sub(fix_srcset, html)

    if USE_RE.search(html):
        html = USE_RE.sub(r'href="\1"', html)
        if SPRITE_MARKER not in html:
            html = re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + '\n' + sprite_markup(), html, count=1)
    return html


def main():
    count = 0
    for path in ROOT.rglob('*.html'):
        rel = path.relative_to(ROOT)
        if SKIP_DIRS.intersection(rel.parts):
            continue
        prefix = '../' * (len(rel.parts) - 1)
        original = path.read_text(encoding='utf-8')
        updated = convert(original, prefix)
        if updated != original:
            path.write_text(updated, encoding='utf-8')
            count += 1
    print(f'Portable URLs applied to {count} pages')


if __name__ == '__main__':
    main()
