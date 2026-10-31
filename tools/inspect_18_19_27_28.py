import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

print("Analizando los polígonos de 18, 19, 27, 28:")
for e in msp:
    if e.dxf.layer in ('00-DIVISION PARCELAS', '02-BORDILLO-PARCELA') and e.dxftype() == 'LWPOLYLINE' and e.closed:
        pts = [(p[0], p[1]) for p in e.get_points()]
        cx = sum(p[0] for p in pts) / len(pts)
        cy = sum(p[1] for p in pts) / len(pts)
        if 1150 <= cx <= 1195 and 700 <= cy <= 765:
            print(f"Polígono en ({cx:.2f}, {cy:.2f}):")
            for p in pts:
                print(f"   ({p[0]:.2f}, {p[1]:.2f})")
