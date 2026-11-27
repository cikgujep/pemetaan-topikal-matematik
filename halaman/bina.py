#!/usr/bin/env python3
"""Membina peta_topikal.html (fail tunggal, data dibenamkan) daripada CSV dalam folder induk.
Jalankan:  python bina.py
"""
import csv, json, os, sys

AKAR = os.path.dirname(os.path.abspath(__file__))
INDUK = os.path.dirname(AKAR)

def baca(nama):
    with open(os.path.join(INDUK, nama), encoding='utf-8-sig', newline='') as fh:
        return list(csv.DictReader(fh))

COLS = ['M1', 'M2', 'M3', 'M4', 'AM4', 'M5', 'AM5']
fail_inventori = ['inventori_M1.csv', 'inventori_M2_M3.csv', 'inventori_M4_M5.csv', 'inventori_AM4_AM5.csv']

inv, files = [], []
for f in fail_inventori:
    r = baca(f); inv += r; files.append({'nama': f, 'baris': len(r)})
kel = baca('kelompok_topikal.csv'); files.append({'nama': 'kelompok_topikal.csv', 'baris': len(kel)})
mxr = baca('matriks_topikal.csv'); files.append({'nama': 'matriks_topikal.csv', 'baris': len(mxr)})
p4 = baca('pautan_AM4.csv'); p5 = baca('pautan_AM5.csv')
files.append({'nama': 'pautan_AM4.csv', 'baris': len(p4)})
files.append({'nama': 'pautan_AM5.csv', 'baris': len(p5)})

if len(inv) != 603:
    sys.exit('Amaran: inventori mempunyai %d baris, dijangka 603.' % len(inv))
for r in kel + mxr:
    if 'bidang' not in r:
        sys.exit('Lajur bidang tiada dalam kelompok_topikal.csv atau matriks_topikal.csv.')

mx = []
for r in mxr:
    cells = {c: [s.strip().split()[0] for s in r[c].split(';') if s.strip()] for c in COLS}
    mx.append({'kelompok': r['kelompok'], 'rantaian': r['rantaian'], 'bidang': r['bidang'], 'cells': cells})

dk = {'st': [], 'sp': []}
if os.path.exists(os.path.join(INDUK, 'kelompok_DK27_M1.csv')):
    dk['st'] = baca('kelompok_DK27_M1.csv'); dk['sp'] = baca('inventori_DK27_M1.csv')
    files.append({'nama': 'kelompok_DK27_M1.csv', 'baris': len(dk['st'])})
    files.append({'nama': 'inventori_DK27_M1.csv', 'baris': len(dk['sp'])})
    if os.path.exists(os.path.join(INDUK, 'pautan_warisan_DK27.csv')):
        dk['waris'] = baca('pautan_warisan_DK27.csv')
        files.append({'nama': 'pautan_warisan_DK27.csv', 'baris': len(dk['waris'])})
data = {'inv': inv, 'kel': kel, 'mx': mx, 'pautan': p4 + p5, 'dk': dk, 'meta': {'files': files}}
js = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
js = js.replace('</', '<\\/').replace('<!--', '<\\!--').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')

with open(os.path.join(AKAR, 'templat.html'), encoding='utf-8') as fh:
    t = fh.read()
assert '__DATA__' in t, 'Penanda __DATA__ tiada dalam templat.html'
out = os.path.join(AKAR, 'peta_topikal.html')
with open(out, 'w', encoding='utf-8') as fh:
    fh.write(t.replace('__DATA__', js))
tp = os.path.join(AKAR, 'templat_pembentangan.html')
if os.path.exists(tp):
    with open(tp, encoding='utf-8') as fh:
        t2 = fh.read()
    assert '__DATA__' in t2, 'Penanda __DATA__ tiada dalam templat_pembentangan.html'
    with open(os.path.join(AKAR, 'pembentangan.html'), 'w', encoding='utf-8') as fh:
        fh.write(t2.replace('__DATA__', js))
    print('Siap: pembentangan.html')

# ===== Hab: Panduan + Peta Topikal + Pembentangan dalam satu fail =====
import base64, html as _h, re as _re
th = os.path.join(AKAR, 'templat_hub.html')
if os.path.exists(th):
    with open(th, encoding='utf-8') as fh:
        hub = fh.read()
    TTm = {'M1': 1, 'M2': 2, 'M3': 3, 'M4': 4, 'AM4': 4, 'M5': 5, 'AM5': 5}
    pall = p4 + p5
    spid = {r['id_nod'] for r in inv}
    def sko(i):
        m = _re.match(r'^(.*-B\d+)-SP(\d+\.\d+)\.\d+$', i)
        return m.group(1) + '-SK' + m.group(2) if m else None
    mula, jeda = [], 0
    for r in mx:
        mine = {s for c in COLS for s in r['cells'][c]}
        mprim = sum(len(r['cells'][c]) for c in COLS if c[0] == 'M')
        anch = [l for l in pall if sko(l['nod_sasaran']) in mine and l['nod_sumber'] in spid and not l['nod_sumber'].startswith('AM')
                and l['kekuatan'] == 'kuat' and l['jenis'] in ('SAMBUNGAN', 'GENERALISASI', 'NOTASI')]
        if mprim == 0 and not anch: mula.append(r['rantaian'].split(' ')[0])
        occ = sorted({TTm[c] for c in COLS if r['cells'][c]})
        if any(b - a > 1 for a, b in zip(occ, occ[1:])): jeda += 1
    from collections import Counter, OrderedDict
    jc = Counter(l['jenis'] for l in pall)
    kel_g = OrderedDict()
    for r in mx: kel_g.setdefault(r['kelompok'], []).append(r)
    kt = []
    for i, (kname, rows) in enumerate(kel_g.items()):
        hue = (i * 24) % 360
        li = ''.join('<li><span><code>' + _h.escape(r['rantaian'].split(' ')[0]) + '</code> ' + _h.escape(r['rantaian'].split(' ', 1)[1] if ' ' in r['rantaian'] else '') +
                      '</span><em>' + _h.escape(r['bidang']) + ' &middot; ' + str(sum(len(r['cells'][c]) for c in COLS)) + ' SK</em></li>' for r in rows)
        kt.append('<div class="kg" style="background:hsla(%d,60%%,55%%,.10)"><h4>%s</h4><ul>%s</ul></div>' % (hue, _h.escape(kname), li))
    rep = {
        '__S_SP__': str(len(inv)), '__S_SK__': str(len(kel)), '__S_KEL__': str(len(kel_g)), '__S_BEN__': str(len(mx)),
        '__S_BID__': str(len({r['bidang'] for r in mx})), '__S_PAU__': str(len(pall)),
        '__S_DKSP__': str(len(dk['sp'])), '__S_DKST__': str(len(dk['st'])),
        '__J_SAMBUNGAN__': str(jc['SAMBUNGAN']), '__J_GENERALISASI__': str(jc['GENERALISASI']), '__J_ALAT__': str(jc['ALAT']),
        '__J_NOTASI__': str(jc['NOTASI']), '__J_TIADA__': str(jc['TIADA PRASYARAT']),
        '__M_MULA__': str(len(mula)), '__M_MULALIST__': ', '.join(mula), '__M_JEDA__': str(jeda),
        '__H_Y__': str(sum(1 for r in inv if r['perlu_semak_visual'] == 'Y')), '__H_LOW__': str(sum(1 for l in pall if l['keyakinan'] == 'rendah')),
        '__KTABLE__': ''.join(kt),
    }
    for k, v in rep.items():
        assert k in hub, k
        hub = hub.replace(k, v)
    with open(out, encoding='utf-8') as fh: peta_html = fh.read()
    with open(os.path.join(AKAR, 'pembentangan.html'), encoding='utf-8') as fh: pers_html = fh.read()
    hub = hub.replace('__B64_PETA__', base64.b64encode(peta_html.encode('utf-8')).decode('ascii'))
    hub = hub.replace('__B64_PEMB__', base64.b64encode(pers_html.encode('utf-8')).decode('ascii'))
    with open(os.path.join(AKAR, 'pemetaan_topikal.html'), 'w', encoding='utf-8') as fh:
        fh.write(hub)
    print('Siap: pemetaan_topikal.html (Panduan, Peta Topikal, Pembentangan; Mula baharu %d, Jeda %d)' % (len(mula), jeda))
print('Siap:', out, '(%d SP, %d SK, %d rantaian konsep, %d pautan)' % (len(inv), len(kel), len(mx), len(p4) + len(p5)))
