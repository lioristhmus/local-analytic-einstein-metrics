"""Source hygiene checks; these do not validate mathematical claims."""
import collections
import hashlib
import json
from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
base=root/'paper'
s=(base/'manuscript.md').read_text()
errors=[]
ids=re.findall(r'<div id="([^"]+)">',s)+re.findall(r'\{#([^}]+)\}',s)
errors += ['Duplicate ID '+k for k,n in collections.Counter(ids).items() if n>1]
for target in re.findall(r'\]\(#([^)]*)\)',s):
    if target not in ids: errors.append('Unresolved link '+target)
link_prose=re.sub(r'\$\$.*?\$\$','',s,flags=re.S)
link_prose=re.sub(r'\$[^$\n]*\$','',link_prose)
for target in re.findall(r'\]\(([^)#][^)]*)\)',link_prose):
    if not re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',target):
        if not (base/target.split('#',1)[0]).is_file():
            errors.append('Missing companion file '+target)
keys=set(re.findall(r'@[A-Za-z]+\{([^,]+),',(base/'references.bib').read_text()))
citations=re.findall(r'(?<![\w])@([A-Za-z][\w:-]+)',s)
for k in citations:
    if k not in keys and k not in ids: errors.append('Unresolved citation '+k)
for pat in [r'\\\[',r'\\\(',r'\\tag\{',r'(?m)^#{1,5} (?:Theorem|Lemma|Proposition|Definition) ']:
    if re.search(pat,s): errors.append('Forbidden syntax '+pat)
display=[i for i,line in enumerate(s.splitlines()) if line.startswith('$$')]
if len(display)%2: errors.append('Odd display fence count')
lines=s.splitlines()
for i,line in enumerate(lines):
    if line.startswith('<div id=') and (i+1>=len(lines) or lines[i+1].strip()):
        errors.append('Anchor without following blank line '+str(i+1))
proofs=len(re.findall(r'\*(?:Proof|Alternative proof)\.\*',s))
if proofs!=s.count('∎'): errors.append('Proof/end count mismatch')
numbers=re.findall(r'^\*\*(?:Definition|Theorem|Proposition|Lemma|Corollary|Example|Remark) ([A-Z0-9]+)\.(\d+)',s,re.M)
groups=collections.defaultdict(list)
for sec,n in numbers: groups[sec].append(int(n))
for sec,ns in groups.items():
    if ns!=list(range(1,len(ns)+1)): errors.append('Environment numbering '+sec+': '+str(ns))
if re.search(r'/Users/|/private/|research_codex/|contact-optical-einstein-v',s):
    errors.append('Internal path or drafting provenance in manuscript')
prose_without_citations=re.sub(r'\[-?@[^\]]+\]','',s)
# Recognize textual bibliography citations and their locators in this revision.
textual_cite_pattern = r'@(?:' + '|'.join(re.escape(k) for k in keys) + r')[ \t]+\[[^\]\n]*\]'
prose_without_citations=re.sub(textual_cite_pattern, '', prose_without_citations)
if re.search(r'gg-|Theorem 3\.3|Lemma B\.3|Appendix [C-L]',prose_without_citations):
    errors.append('Stale source reference')
report={'status':'PASS' if not errors else 'FAIL','errors':errors,
        'ids':len(ids),'bibliography_keys':len(keys),'proofs':proofs,
        'displays':len(display)//2,'environment_counts':{k:len(v) for k,v in groups.items()},
        'source_sha256':hashlib.sha256(s.encode()).hexdigest(),
        'scope':'source syntax and references; not mathematical verification'}
(root/'build').mkdir(exist_ok=True)
(root/'build'/'preflight.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
raise SystemExit(bool(errors))
