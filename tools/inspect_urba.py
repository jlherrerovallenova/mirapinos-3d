import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

print("Analizando capas URBA, CESPED, 00-PARQUE, 00-TRAMA*...")

for layer in ['URBA', 'CESPED', '00-PARQUE', '00-TRAMA CALZADA', '00-TRAMA ACERADO', '00-TRAMA ELP']:
    ents = [e for e in msp if e.dxf.layer == layer]
    polys = [e for e in ents if e.dxftype() in ('LWPOLYLINE', 'HATCH')]
    lines = [e for e in ents if e.dxftype() == 'LINE']
    print(f"Capa {layer}: {len(ents)} entidades (polys={len(polys)}, lines={len(lines)})")
    for p in polys[:3]:
        if p.dxftype() == 'LWPOLYLINE':
            pts = [(round(pt[0], 1), round(pt[1], 1)) for pt in p.get_points()]
            print(f"   Poly (cerrada={p.closed}, pts={len(pts)}): {pts[:4]}...")
