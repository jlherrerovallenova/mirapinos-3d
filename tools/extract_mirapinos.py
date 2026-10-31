import ezdxf
import json
import math

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

# Parcel numbers are located around X: 1100-1260, Y: 640-830
print("Buscando polilíneas y geometrías alrededor de la urbanización...")

# 1. Encontrar textos de parcelas (1 a 35)
parcelas_info = {}
for e in msp:
    if e.dxftype() in ('TEXT', 'MTEXT') and e.dxf.layer == 'numero parcela':
        txt = (e.dxf.text if e.dxftype() == 'TEXT' else e.text).strip()
        if txt.isdigit():
            num = int(txt)
            if 1 <= num <= 35:
                parcelas_info[num] = {
                    'num': num,
                    'x': e.dxf.insert[0],
                    'y': e.dxf.insert[1]
                }

print(f"Parcelas encontradas con número: {len(parcelas_info)} de 35")
for num in sorted(parcelas_info.keys()):
    p = parcelas_info[num]
    print(f"Parcela {num:2d} -> X: {p['x']:.2f}, Y: {p['y']:.2f}")

# Layers to inspect for boundary lines: '00-DIVISION PARCELAS', '02-BORDILLO-PARCELA', 'Parcelas modificadas', '02-DIBUJO-BASE'
layers_geom = ['00-DIVISION PARCELAS', '02-BORDILLO-PARCELA', 'Parcelas modificadas', '00-TRAMA CALZADA', '00-TRAMA ACERADO', 'CESPED']
for l in layers_geom:
    ents = [e for e in msp if e.dxf.layer == l]
    print(f"Capa '{l}': {len(ents)} entidades")
