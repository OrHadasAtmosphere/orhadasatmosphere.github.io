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
<main id="main">{body}</main><footer><div><strong>Or Hadas</strong><p>Department of Geosciences · Princeton University</p></div><div class="footer-links"><a href="mailto:hadas.or11@gmail.com">Email ↗</a><a href="{SCHOLAR}">Google Scholar ↗</a><a href="https://orcid.org/0000-0001-9360-2999">ORCID ↗</a><a href="https://github.com/OrHadasAtmosphere">GitHub ↗</a></div><p class="footer-note">Storms. Clouds. Climate.</p></footer></body></html>'''

HOME = '''<section class="hero"><div class="hero-copy"><p class="eyebrow">Princeton University · Geosciences</p><h1>From individual storms<br>to the climate system.</h1><p class="lead">I’m Or Hadas, an atmospheric scientist studying how storms, clouds, and large-scale circulation shape our climate.</p><p>I am a <strong>Hess Postdoctoral Fellow at Princeton University</strong>, working with <strong>Stephan Fueglistaler</strong>. I completed my PhD at the Weizmann Institute of Science with Yohai Kaspi.</p><div class="actions"><a class="button" href="research/">Explore my research ↗</a><a class="text-link" href="publications/">View publications →</a></div></div><figure class="portrait"><img src="assets/img/20176F053.jpg" alt="Or Hadas" width="720" height="900" fetchpriority="high"><figcaption>Or Hadas <span>Atmospheric dynamics &amp; climate</span></figcaption></figure></section>
<section class="section research-intro"><div><p class="eyebrow">A connected perspective</p><h2>Weather and climate,<br>across scales.</h2></div><div><p class="lead small">What connects the life cycle of a single storm to the behavior of the climate system?</p><p>I combine theory, idealized models, reanalysis data, observations, and machine learning to understand the mechanisms behind midlatitude climate—from jet streams and storm growth to clouds, radiation, and the ocean.</p><a class="text-link" href="research/">Research themes →</a></div></section>'''
HOME += '<section class="section"><div class="section-heading"><div><p class="eyebrow">Latest work</p><h2>Recent preprints</h2></div><a class="text-link" href="publications/">All publications →</a></div>'+''.join(paper(p) for p in PAPERS if p['status']=='preprint')+'</section>'
HOME += '<section class="contact-band"><p class="eyebrow">Get in touch</p><h2>Let’s talk atmospheric science.</h2><a href="mailto:hadas.or11@gmail.com">hadas.or11@gmail.com ↗</a></section>'

RESEARCH = '''<section class="page-heading"><p class="eyebrow">Research</p><h1>Understanding the atmosphere<br>through its storms.</h1><p class="lead">Physical mechanisms, individual weather systems, and the climate they create together.</p></section>'''
themes = [
('Storms & jets','Fundamentals of midlatitude dynamics', 'I study how baroclinic instability, jet structure, and eddy–mean flow interactions govern storm growth. Following individual storms helps connect their energy conversion and propagation to the time-averaged circulation.', 'My work explores why stronger jets do not always produce stronger storms, and how a storm’s path through its environment controls its development.', 'Stronger jet, weaker storms','https://doi.org/10.1038/s41467-026-71784-3'),
('Clouds & radiation','Cloud–circulation coupling','Storms organize clouds, and clouds modify the energy budget that sustains atmospheric circulation. I investigate how this coupling shapes planetary albedo, temperature gradients, and the seasonal cycle of storm tracks.','I combine observations, idealized simulations, and theoretical models to understand feedbacks among storms, clouds, and the ocean.','Cloud radiative effects reinforce storm tracks','https://arxiv.org/abs/2607.02213'),
('Machine learning & predictability','Separating climate from weather','How much does the climate background tell us about an individual storm? I use machine learning alongside physical diagnostics to distinguish the influence of climatic conditions from synoptic variability.','This approach helps quantify the predictability of storm intensity and trajectories, and clarifies the challenges of attributing individual weather events to climate change.','Quantifying climate’s influence on storm activity','https://doi.org/10.1029/2025GL118496'),
('Atmosphere & ocean','Storm-driven ocean responses','Extratropical storms transfer energy to the ocean through wind stress. My recent work examines near-inertial wave generation from a storm-centered perspective, linking storm structure, propagation, and life cycle to the ocean’s response.','','Midlatitude near-inertial wave generation','https://arxiv.org/abs/2609.16671')]
for i,(eyebrow,title,p1,p2,label,url) in enumerate(themes,1):
    RESEARCH += f'<section class="theme"><span class="theme-number">{i:02}</span><div><p class="eyebrow">{e(eyebrow)}</p><h2>{e(title)}</h2><p>{e(p1)}</p>'+ (f'<p>{e(p2)}</p>' if p2 else '') + f'<a class="text-link" href="{url}">Read: {e(label)} ↗</a></div></section>'

PUBLICATIONS=f'<section class="page-heading"><p class="eyebrow">Publications</p><h1>Papers &amp; preprints.</h1><p class="lead">Atmospheric dynamics, storm predictability, and the coupled climate system.</p><a class="text-link" href="{SCHOLAR}">Google Scholar profile ↗</a></section>'
for status,label in [('preprint','Preprints'),('published','Peer-reviewed publications')]:
    selected=sorted((p for p in PAPERS if p['status']==status),key=lambda p:p['year'],reverse=True)
    PUBLICATIONS += f'<section class="publication-group"><div class="section-heading"><h2>{label}</h2><span class="count">{len(selected):02}</span></div>'+''.join(paper(p) for p in selected)+'</section>'
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
