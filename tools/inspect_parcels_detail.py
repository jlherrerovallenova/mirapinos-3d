import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

print("Buscando todos los números de parcela y sus coordenadas:")
parcelas = {}
for e in msp:
    if e.dxftype() in ('TEXT', 'MTEXT') and e.dxf.layer == 'numero parcela':
        ins = e.dxf.insert
        txt = (e.dxf.text if e.dxftype() == 'TEXT' else e.text).strip()
        if txt.isdigit():
            num = int(txt)
            if 1 <= num <= 35:
                print(f"Parcela {num:2d} -> X: {ins[0]:.2f}, Y: {ins[1]:.2f}")
                parcelas[num] = (round(ins[0], 2), round(ins[1], 2))

# Also print lines or polylines near 18, 19, 27, 28
print("\nInspeccionando geometrías cerca de 18, 19, 27, 28...")
for num in [18, 19, 27, 28]:
    pos = parcelas[num]
    print(f"\nVecindad de Parcela {num} en {pos}:")
    near_ents = []
    for e in msp:
        if e.dxftype() in ('LINE', 'LWPOLYLINE', 'INSERT'):
            if e.dxftype() == 'LINE':
                pts = [(e.dxf.start[0], e.dxf.start[1]), (e.dxf.end[0], e.dxf.end[1])]
            elif e.dxftype() == 'LWPOLYLINE':
                pts = [(p[0], p[1]) for p in e.get_points()]
            elif e.dxftype() == 'INSERT':
                pts = [(e.dxf.insert[0], e.dxf.insert[1])]
            
            dists = [((p[0]-pos[0])**2 + (p[1]-pos[1])**2)**0.5 for p in pts]
            if min(dists) < 15.0:
                info = f"{e.dxftype()} layer={e.dxf.layer}"
                if e.dxftype() == 'INSERT':
                    info += f" name={e.dxf.name} rot={e.dxf.rotation:.1f}"
                near_ents.append(info)
    print(f"Entidades cercanas ({len(near_ents)}): {near_ents[:8]}")
