import ezdxf
import math

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

parcelas = {}
for e in msp:
    if e.dxftype() in ('TEXT', 'MTEXT') and e.dxf.layer == 'numero parcela':
        ins = e.dxf.insert
        if 1100 <= ins[0] <= 1260 and 640 <= ins[1] <= 830:
            txt = (e.dxf.text if e.dxftype() == 'TEXT' else e.text).strip()
            if txt.isdigit():
                parcelas[int(txt)] = (ins[0], ins[1])

# Asignar muros a cada parcela por proximidad
muros_por_parcela = {i: [] for i in range(1, 36)}

for e in msp:
    if e.dxf.layer in ('MURO', 'TRAMA MUROS', 'EST pilares'):
        pts = []
        if e.dxftype() == 'LINE':
            pts = [(e.dxf.start[0], e.dxf.start[1]), (e.dxf.end[0], e.dxf.end[1])]
        elif e.dxftype() == 'LWPOLYLINE':
            pts = [(p[0], p[1]) for p in e.get_points()]
        
        if pts and any(1100 <= p[0] <= 1260 and 640 <= p[1] <= 830 for p in pts):
            # Centroide del elemento
            cx = sum(p[0] for p in pts) / len(pts)
            cy = sum(p[1] for p in pts) / len(pts)
            # Buscar parcela más cercana
            closest = min(parcelas.keys(), key=lambda k: (parcelas[k][0]-cx)**2 + (parcelas[k][1]-cy)**2)
            dist = math.sqrt((parcelas[closest][0]-cx)**2 + (parcelas[closest][1]-cy)**2)
            if dist < 20.0: # dentro de radio razonable de la parcela
                muros_por_parcela[closest].append(pts)

print("Distribución de geometría de muros por parcela:")
for num in sorted(muros_por_parcela.keys()):
    print(f"Parcela {num:2d}: {len(muros_por_parcela[num])} elementos constructivos")
