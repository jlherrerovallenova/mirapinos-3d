import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

print("Analizando geometrías en el sector (1100 <= X <= 1260, 640 <= Y <= 830)...")
layer_counts = {}
for e in msp:
    # Check bounding or point
    pts = []
    if e.dxftype() == 'LWPOLYLINE':
        pts = [(p[0], p[1]) for p in e.get_points()]
    elif e.dxftype() == 'LINE':
        pts = [(e.dxf.start[0], e.dxf.start[1]), (e.dxf.end[0], e.dxf.end[1])]
    
    if pts:
        # Check if any point is in bounding box
        in_box = any(1100 <= p[0] <= 1260 and 640 <= p[1] <= 830 for p in pts)
        if in_box:
            layer_counts[e.dxf.layer] = layer_counts.get(e.dxf.layer, 0) + 1

print("Capas con geometrías en la urbanización:")
for l, c in sorted(layer_counts.items(), key=lambda x: x[1], reverse=True)[:30]:
    print(f"  - {l}: {c} elementos")
