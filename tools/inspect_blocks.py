import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

print("Buscando bloques de viviendas...")
blocks = [b for b in doc.blocks if not b.name.startswith('*')]
for b in blocks:
    print(f"Bloque: {b.name} ({len(b)} entidades)")

print("\nBuscando referencias a bloques insertados en la urbanización...")
for e in msp:
    if e.dxftype() == 'INSERT':
        ins = e.dxf.insert
        if 1100 <= ins[0] <= 1260 and 640 <= ins[1] <= 830:
            print(f"INSERT '{e.dxf.name}' en ({ins[0]:.1f}, {ins[1]:.1f}), escala=({e.dxf.xscale:.1f}, {e.dxf.yscale:.1f}), rot={e.dxf.rotation:.1f}")
