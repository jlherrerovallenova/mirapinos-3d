import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

print("Buscando polilíneas de la piscina y zonas comunes...")
for e in msp:
    if e.dxftype() == 'LWPOLYLINE':
        pts = [(p[0], p[1]) for p in e.get_points()]
        cx = sum(p[0] for p in pts) / len(pts)
        cy = sum(p[1] for p in pts) / len(pts)
        if 1180 <= cx <= 1230 and 720 <= cy <= 760:
            print(f"[{e.dxf.layer}] Poly en ({cx:.2f}, {cy:.2f}) cerrada={e.closed} pts={len(pts)}")
