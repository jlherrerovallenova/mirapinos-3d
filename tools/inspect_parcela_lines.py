import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

print("Analizando polilíneas cerradas y divisiones en '00-DIVISION PARCELAS' y '02-BORDILLO-PARCELA':")

for layer in ['00-DIVISION PARCELAS', '02-BORDILLO-PARCELA', 'Parcelas modificadas']:
    print(f"\n--- Layer {layer} ---")
    for e in msp:
        if e.dxf.layer == layer:
            if e.dxftype() == 'LWPOLYLINE':
                pts = [(round(p[0], 2), round(p[1], 2)) for p in e.get_points()]
                closed = e.closed
                print(f"LWPOLYLINE (cerrada={closed}, pts={len(pts)}): {pts[:3]}...{pts[-1:]}")
            elif e.dxftype() == 'LINE':
                p1 = (round(e.dxf.start[0], 2), round(e.dxf.start[1], 2))
                p2 = (round(e.dxf.end[0], 2), round(e.dxf.end[1], 2))
                print(f"LINE: {p1} -> {p2}")
