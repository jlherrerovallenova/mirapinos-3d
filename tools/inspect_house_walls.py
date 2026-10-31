import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

print("Analizando muros de viviendas en la urbanización (1100 <= X <= 1260, 640 <= Y <= 830)...")

muro_lines = []
for e in msp:
    if e.dxf.layer in ('MURO', 'TRAMA MUROS', 'EST pilares'):
        if e.dxftype() == 'LINE':
            p1 = (e.dxf.start[0], e.dxf.start[1])
            p2 = (e.dxf.end[0], e.dxf.end[1])
            if (1100 <= p1[0] <= 1260 and 640 <= p1[1] <= 830) or (1100 <= p2[0] <= 1260 and 640 <= p2[1] <= 830):
                muro_lines.append((p1, p2))
        elif e.dxftype() == 'LWPOLYLINE':
            pts = [(p[0], p[1]) for p in e.get_points()]
            if any(1100 <= p[0] <= 1260 and 640 <= p[1] <= 830 for p in pts):
                for i in range(len(pts) - 1):
                    muro_lines.append((pts[i], pts[i+1]))
                if e.closed:
                    muro_lines.append((pts[-1], pts[0]))

print(f"Total segmentos de muro encontrados en las viviendas: {len(muro_lines)}")
