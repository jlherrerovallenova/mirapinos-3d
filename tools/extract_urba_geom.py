import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

# Bounding box of the urbanizacion
# Center: (1190, 740)
CX = 1190.0
CY = 740.0

print("Analizando límites y polilíneas de la urbanización...")
# Let's collect road polygons ('00-TRAMA CALZADA'), sidewalk polygons ('00-TRAMA ACERADO'), green spaces ('CESPED', '00-TRAMA ELP', '00-PARQUE')
calzadas = []
aceras = []
zonas_verdes = []

for e in msp:
    if e.dxftype() == 'LWPOLYLINE':
        pts = [[round(p[0] - CX, 2), round(p[1] - CY, 2)] for p in e.get_points()]
        if e.dxf.layer == '00-TRAMA CALZADA':
            calzadas.append(pts)
        elif e.dxf.layer == '00-TRAMA ACERADO':
            aceras.append(pts)
        elif e.dxf.layer in ('CESPED', '00-TRAMA ELP'):
            zonas_verdes.append(pts)

print(f"Calzadas extraídas: {len(calzadas)}")
print(f"Aceras extraídas: {len(aceras)}")
print(f"Zonas verdes extraídas: {len(zonas_verdes)}")
