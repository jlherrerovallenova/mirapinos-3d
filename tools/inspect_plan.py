import ezdxf
from collections import Counter

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

print("--- TEXTOS EN CAPAS DE PARCELA ---")
target_layers = {'numero parcela', 'superficie parcelas', 'CARPIN-text'}

for e in msp:
    if e.dxftype() in ('TEXT', 'MTEXT') and e.dxf.layer in target_layers:
        txt = e.dxf.text if e.dxftype() == 'TEXT' else e.text
        ins = e.dxf.insert
        print(f"[{e.dxf.layer}] ({ins[0]:.1f}, {ins[1]:.1f}): {txt.strip()}")

print("\n--- BLOQUES INSERTADOS ---")
block_counts = Counter(e.dxf.name for e in msp if e.dxftype() == 'INSERT')
for name, c in block_counts.most_common(25):
    print(f"Bloque {name}: {c} instancias")
