import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

parcelas = {}
for e in msp:
    if e.dxftype() in ('TEXT', 'MTEXT') and e.dxf.layer == 'numero parcela':
        ins = e.dxf.insert
        if 1100 <= ins[0] <= 1260 and 640 <= ins[1] <= 830:
            txt = (e.dxf.text if e.dxftype() == 'TEXT' else e.text).strip()
            if txt.isdigit():
                num = int(txt)
                parcelas[num] = (round(ins[0], 2), round(ins[1], 2))

print(f"Total parcelas encontradas en zona urbanización: {len(parcelas)}")
for num in sorted(parcelas.keys()):
    print(f"Parcela {num:2d}: {parcelas[num]}")
