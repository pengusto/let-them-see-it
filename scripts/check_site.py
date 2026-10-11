"""Check static site references with Python's standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
root = Path(__file__).resolve().parents[1] / 'site'
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(); self.path=path; self.ids=set(); self.refs=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, (self.path, 'duplicate id')
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs: self.refs.append(attrs[key])
        if tag=='img': assert attrs.get('alt'), (self.path, 'missing alt')
pages={}
for path in root.glob('*.html'):
    parser=Page(path); parser.feed(path.read_text()); pages[path.resolve()]=parser
count=0
for path, page in pages.items():
    for ref in page.refs:
        url=urlsplit(ref)
        if url.scheme or url.netloc: continue
        target=(path.parent / unquote(url.path)).resolve() if url.path else path
        if target.is_dir(): target=target/'index.html'
        assert target.is_relative_to(root.resolve()), (path, ref)
        assert target.is_file(), (path, ref)
        if url.fragment: assert url.fragment in pages[target].ids, (path, ref)
        count+=1
assert len(pages)==3
print(f'PASS: {len(pages)} HTML pages, {count} local references, image alt text')
