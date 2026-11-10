#!/usr/bin/env python3
"""Check generated pages and local navigation without third-party packages."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links=[]; self.ids=set(); self.h1=0; self.current=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1': self.h1+=1
        if 'id' in a:
            assert a['id'] not in self.ids, f'Duplicate ID: {a["id"]}'
            self.ids.add(a['id'])
        if a.get('aria-current')=='page': self.current+=1
        for attr in ['href','src']:
            if attr in a: self.links.append(a[attr])

paths=['index.html','research/index.html','publications/index.html']
pages={}
for name in paths:
    parser=Page();parser.feed((ROOT/name).read_text());pages[(ROOT/name).resolve()]=parser
    assert parser.h1==1, f'{name}: expected one main heading'
    assert parser.current==1, f'{name}: expected active navigation'
count=0
for path,p in pages.items():
    for link in p.links:
        u=urlsplit(link)
        if u.scheme or u.netloc: continue
        target=(path.parent/unquote(u.path)).resolve() if u.path else path
        if target.is_dir(): target=target/'index.html'
        assert target.is_relative_to(ROOT), f'Link leaves site: {link}'
        assert target.exists(), f'{path.name}: broken link {link}'
        if u.fragment and target in pages:
            assert u.fragment in pages[target].ids, f'Missing anchor {link}'
        count+=1
papers=json.loads((ROOT/'_data/publications.json').read_text())
assert len({p['url'] for p in papers})==len(papers),'Duplicate publications'
for p in papers:
    assert p['status'] in ['published','preprint']
    assert p['url'].startswith('https://')
    assert p['url']!='https://doi.org/10.1029/20'
assert (ROOT/'.nojekyll').exists()
assert not (ROOT/'_config.yml').exists(),'Obsolete Jekyll config remains'
print(f'PASS: {len(pages)} pages, {count} local links/anchors, {len(papers)} unique papers')
