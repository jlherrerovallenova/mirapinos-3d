import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

print("Buscando polilíneas y tramas de parcelas, viales y zonas verdes...")
calz_hatch = [e for e in msp if e.dxftype() == 'HATCH' and 'CALZADA' in e.dxf.layer]
acer_hatch = [e for e in msp if e.dxftype() == 'HATCH' and 'ACERADO' in e.dxf.layer]
print(f"Hatch calzada: {len(calz_hatch)}, Hatch acera: {len(acer_hatch)}")

bordillos = [e for e in msp if 'bordillo' in e.dxf.layer.lower() or 'BORDILLO' in e.dxf.layer]
print(f"Bordillos totales: {len(bordillos)}")

# Parcel division lines
div_parcelas = [e for e in msp if e.dxf.layer in ('00-DIVISION PARCELAS', '02-BORDILLO-PARCELA', 'Parcelas modificadas')]
print(f"Líneas de división de parcelas: {len(div_parcelas)}")
