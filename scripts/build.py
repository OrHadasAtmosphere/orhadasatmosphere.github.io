#!/usr/bin/env python3
"""Build this GitHub Pages site using only Python's standard library."""
import json
from pathlib import Path
from html import escape as e
ROOT = Path(__file__).resolve().parents[1]
PAPERS = json.loads((ROOT/'_data/publications.json').read_text())
SCHOLAR = 'https://scholar.google.com/citations?user=gYHd_jcAAAAJ&sortby=pubdate'

def paper(p):
    authors = e(p['authors']).replace('Or Hadas','<strong>Or Hadas</strong>')
    note = f'<p class="paper-note">{e(p["note"])}</p>' if p.get('note') else ''
    return f'<article class="paper"><p class="eyebrow">{p["year"]} · {e(p["citation"])}</p><h3><a href="{e(p["url"],quote=True)}">{e(p["title"])} <span aria-hidden="true">↗</span></a></h3><p class="authors">{authors}</p>{note}</article>'

def page(title,body,active,prefix):
    nav = ''.join(f'<a href="{prefix}{path}"'+(' aria-current="page"' if active==name else '')+f'>{name}</a>' for name,path in [('About',''),('Research','research/'),('Publications','publications/')])
    canonical='https://orhadasatmosphere.github.io/'+('' if active=='About' else active.lower()+'/')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} · Or Hadas</title><meta name="description" content="Or Hadas, Hess Postdoctoral Fellow at Princeton University. Research on atmospheric dynamics, midlatitude storms, clouds, and climate.">
<meta name="theme-color" content="#f7f5ef"><link rel="canonical" href="{canonical}"><meta property="og:title" content="{e(title)} · Or Hadas"><meta property="og:type" content="website"><meta property="og:url" content="{canonical}"><meta property="og:description" content="Atmospheric dynamics, storms, clouds, and climate. Hess Postdoctoral Fellow at Princeton University.">
<link rel="icon" href="{prefix}assets/img/mark.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/css/custom.css"></head>
<body><a class="skip" href="#main">Skip to content</a><header class="site-header"><a class="wordmark" href="{prefix}">Or Hadas<span>Atmospheric scientist</span></a><nav aria-label="Main navigation">{nav}<a class="cv-link" href="{prefix}assets/files/CV_Or_Hadas.pdf">CV ↗</a></nav></header>
<main id="main">{body}</main><footer><div><strong>Or Hadas</strong><p>Department of Geosciences · Princeton University</p></div><div class="footer-links"><button class="email-reveal" type="button" data-contact>Reveal email ↗</button><noscript>Email: oh0815 [at] princeton [dot] edu</noscript><a href="{SCHOLAR}">Google Scholar ↗</a><a href="https://orcid.org/0000-0001-9360-2999">ORCID ↗</a><a href="https://www.linkedin.com/in/or-hadas-214048193/">LinkedIn ↗</a></div></footer><script src="{prefix}assets/js/contact.js" defer></script></body></html>'''

HOME = '''<section class="hero"><div class="hero-copy"><p class="eyebrow">Princeton University · Department of Geosciences</p><h1>Weather and climate across scales</h1><p class="lead">I’m Or Hadas, an atmospheric scientist studying how climate emerges from interactions across scales and among its different components.</p><p>I am a <strong>Hess Postdoctoral Fellow at Princeton University</strong>, working with <strong>Prof. Stephan Fueglistaler</strong>. I completed my PhD at the Weizmann Institute of Science with Prof. Yohai Kaspi.</p><div class="actions"><a class="button" href="research/">Explore my research ↗</a><a class="text-link" href="publications/">View publications →</a></div></div><figure class="portrait"><img src="assets/img/20176F053.jpg" alt="Or Hadas" width="720" height="900" fetchpriority="high"></figure></section>'''
HOME += '<section class="section"><div class="section-heading"><div><p class="eyebrow">Latest work</p><h2>Recent preprints</h2></div><a class="text-link" href="publications/">All publications →</a></div>'+''.join(paper(p) for p in PAPERS if p['status']=='preprint')+'</section>'
HOME += '<section class="contact-band"><h2>Get in touch</h2><button class="email-reveal" type="button" data-contact>Reveal email ↗</button></section>'

RESEARCH = '''<section class="page-heading"><p class="eyebrow">Research</p><h1>How does it all connect?</h1><p class="lead">The climate system emerges from interactions among components, each with its own spatial and temporal scales and distinct dynamical behavior. I want to understand how it all fits together.</p></section>'''
themes = [
    (
        'Jets & storms',
        'Eddy–mean flow interaction, one storm at a time',
        'I study how jet streams and individual storms interact to shape the midlatitude climate. Following storms through their life cycles offers a way to connect their growth and evolution to the large-scale flow, and to understand how storm-track patterns emerge from individual weather systems.',
        'Machine learning provides a complementary way to ask how much of storm behavior is set by the climate background, and how much depends on the evolving synoptic flow. I use it to investigate the physical controls on storm variability and predictability.'
    ),
    (
        'Global energy balance, storms & clouds',
        'Storms bridge global climate and kilometer-scale clouds',
        'Midlatitude clouds play a crucial role in Earth’s energy budget. I study their two-way interaction with atmospheric circulation: how storms regulate cloudiness, and how cloud radiative effects feed back on storm tracks.',
        ''
    ),
    (
        'Atmosphere & ocean',
        'Midlatitude climate through storm–ocean coupling',
        'Midlatitude storms and the ocean are locked in a two-way energetic coupling: oceanic temperature gradients fuel storms, while storms reshape those gradients by driving ocean circulation and mixing.',
        'I aim to understand how this tightly coupled system evolves to shape the climate we observe, and how it may change in the future.'
    )
]
# Use the shared publication records so titles and statuses stay consistent.
related_paper_urls = {
    'Jets & storms': [
        'https://www.nature.com/articles/s41467-026-71784-3',
        'https://doi.org/10.1029/2024AV001555',
        'https://doi.org/10.1175/JAS-D-20-0289.1',
        'https://doi.org/10.1029/2025GL118496',
        'https://doi.org/10.1029/2025GL118886',
    ],
    'Global energy balance, storms & clouds': [
        'https://doi.org/10.1073/pnas.2208778120',
        'https://arxiv.org/abs/2607.02213',
        'https://doi.org/10.22541/essoar.15005264/v1',
    ],
    'Atmosphere & ocean': ['https://arxiv.org/abs/2609.16671'],
}
papers_by_url = {p['url']: p for p in PAPERS}

def research_links(urls):
    items = []
    for url in urls:
        p = papers_by_url[url]
        status = f" · {p['status']}" if p['status'] != 'published' else ''
        items.append(
            f'<li><a href="{e(url, quote=True)}">{e(p["title"])}</a>'
            f' <span>({p["year"]}{e(status)})</span></li>'
        )
    return '<div class="related-papers"><p class="eyebrow">Related papers</p><ul>' + ''.join(items) + '</ul></div>'

for i, (eyebrow, title, p1, p2) in enumerate(themes, 1):
    paragraphs = ''.join(f'<p>{e(text)}</p>' for text in (p1, p2) if text)
    RESEARCH += (
        f'<section class="theme"><span class="theme-number">{i:02}</span><div>'
        f'<p class="eyebrow">{e(eyebrow)}</p><h2>{e(title)}</h2>'
        f'{paragraphs}{research_links(related_paper_urls[eyebrow])}</div></section>'
    )

PUBLICATIONS=f'<section class="page-heading"><p class="eyebrow">Publications</p><h1>Papers &amp; preprints.</h1><p class="lead">Atmospheric dynamics, storm predictability, and the coupled climate system.</p><a class="text-link" href="{SCHOLAR}">Google Scholar profile ↗</a></section>'
for status,label in [('preprint','Preprints'),('published','Peer-reviewed publications'),('report','Reports')]:
    selected=sorted((p for p in PAPERS if p['status']==status),key=lambda p:p['year'],reverse=True)
    PUBLICATIONS += f'<section class="publication-group"><div class="section-heading"><h2>{label}</h2></div>'+''.join(paper(p) for p in selected)+'</section>'
for path,title,body,active,prefix in [('index.html','Atmospheric scientist',HOME,'About','./'),('research/index.html','Research',RESEARCH,'Research','../'),('publications/index.html','Publications',PUBLICATIONS,'Publications','../')]:
    target=ROOT/path
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(page(title,body,active,prefix))
    print('Built',path)

# Help crawlers discover the public pages; omit artificial modification dates.
site_url = 'https://orhadasatmosphere.github.io/'
urls = [site_url + path for path in ['', 'research/', 'publications/']]
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(f'  <url><loc>{e(url)}</loc></url>\n' for url in urls)
    + '</urlset>\n')
(ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: ' + site_url + 'sitemap.xml\n')
