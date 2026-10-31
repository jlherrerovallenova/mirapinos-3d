import ezdxf
import json
import math

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

# Center of urbanización in the drawing
CX = 1190.0
CY = 740.0

# 1. Extraer las 35 parcelas con sus centros
parcelas = {}
for e in msp:
    if e.dxftype() in ('TEXT', 'MTEXT') and e.dxf.layer == 'numero parcela':
        ins = e.dxf.insert
        if 1100 <= ins[0] <= 1260 and 640 <= ins[1] <= 830:
            txt = (e.dxf.text if e.dxftype() == 'TEXT' else e.text).strip()
            if txt.isdigit():
                num = int(txt)
                parcelas[num] = {
                    'num': num,
                    'x': round(ins[0] - CX, 2),
                    'y': round(ins[1] - CY, 2)
                }

# 2. Configurar tipologías y modelos según el proyecto
# 1 a 6: Olivo 1
# 7 a 13: Olivo 2
# 14 a 35: Arce (Arce 1, Arce 2, Arce 3)
units = []

# Mapeo de superficies y precios orientativos del proyecto Mirapinos
# Modelo Olivo: ~145 m² constr, 4 dorm, 3 baños (2+1), precio orientativo 336.000 € - 365.000 €
# Modelo Arce: ~187 m² constr, 4 dorm, 3 baños (2+1), precio orientativo 410.000 € - 450.000 €

# Superficies de parcela aproximadas (430 m² - 760 m²)
parcela_sup = {
    1: 501.96, 2: 433.44, 3: 433.44, 4: 433.44, 5: 433.44, 6: 475.97,
    7: 499.30, 8: 433.44, 9: 433.44, 10: 433.44, 11: 433.44, 12: 433.44, 13: 552.73,
    14: 757.46, 15: 433.44, 16: 433.44, 17: 543.03, 18: 433.44, 19: 433.44, 20: 529.90,
    21: 433.44, 22: 433.44, 23: 433.44, 24: 433.44, 25: 433.44, 26: 529.90, 27: 433.44,
    28: 433.44, 29: 767.87, 30: 433.44, 31: 433.44, 32: 433.44, 33: 433.44, 34: 433.44, 35: 610.00
}

# Estados iniciales (para dar dinamismo comercial con libres, reservadas y vendidas)
estados_sample = {
    1: 'LIBRE', 2: 'RESERVADA', 3: 'LIBRE', 4: 'VENDIDA', 5: 'LIBRE', 6: 'LIBRE',
    7: 'LIBRE', 8: 'LIBRE', 9: 'RESERVADA', 10: 'LIBRE', 11: 'VENDIDA', 12: 'LIBRE', 13: 'LIBRE',
    14: 'LIBRE', 15: 'RESERVADA', 16: 'LIBRE', 17: 'LIBRE', 18: 'LIBRE', 19: 'VENDIDA', 20: 'LIBRE',
    21: 'LIBRE', 22: 'LIBRE', 23: 'RESERVADA', 24: 'LIBRE', 25: 'LIBRE', 26: 'VENDIDA', 27: 'LIBRE',
    28: 'LIBRE', 29: 'LIBRE', 30: 'RESERVADA', 31: 'LIBRE', 32: 'LIBRE', 33: 'LIBRE', 34: 'VENDIDA', 35: 'LIBRE'
}

for num in range(1, 36):
    p = parcelas.get(num, {'x': 0, 'y': 0})
    if num <= 6:
        tipologia = 'Olivo 1'
        m2_c = 145.20
        m2_u = 122.50
        precio = 336000 + (num * 2500)
        dorm = 4
        banos = 3
    elif num <= 13:
        tipologia = 'Olivo 2'
        m2_c = 148.50
        m2_u = 125.10
        precio = 345000 + ((num - 6) * 2000)
        dorm = 4
        banos = 3
    else:
        tipologia = 'Arce'
        m2_c = 186.75
        m2_u = 158.40
        precio = 410000 + ((num - 13) * 1800)
        dorm = 4
        banos = 3

    sup_parcela = parcela_sup.get(num, 450.0)
    estado = estados_sample.get(num, 'LIBRE')

    # Estimación de orientación según posición en el plano
    if num <= 6:
        orientacion = 'Sur / Suroeste'
        rot = 25.0
    elif num <= 13:
        orientacion = 'Norte / Noroeste'
        rot = 192.0
    elif 14 <= num <= 20:
        orientacion = 'Sur / Sureste'
        rot = 205.0
    elif 21 <= num <= 26:
        orientacion = 'Oeste'
        rot = 115.0
    else:
        orientacion = 'Sur / Sureste'
        rot = 12.0

    units.append({
        'id': f"P-{num:02d}",
        'numero': num,
        'nombre': f"Chalet Parcela {num}",
        'tipologia': tipologia,
        'estado': estado,
        'precio': precio,
        'sup_parcela': sup_parcela,
        'sup_construida': m2_c,
        'sup_util': m2_u,
        'dormitorios': dorm,
        'banos': banos,
        'plantas': 2,
        'orientacion': orientacion,
        'x': p['x'],
        'y': p['y'],
        'rot': rot,
        'ancho': 12.0 if 'Arce' in tipologia else 10.5,
        'fondo': 11.0 if 'Arce' in tipologia else 9.8,
        'altura': 6.8
    })

# 3. Extraer líneas de contorno de viales, calzadas, zonas comunes y parcelario
print("Extrayendo líneas de trazado urbanístico...")
lines_urba = []
for e in msp:
    if e.dxf.layer in ('00-DIVISION PARCELAS', '02-BORDILLO-PARCELA', 'Parcelas modificadas', '00-TRAMA CALZADA', '00-TRAMA ACERADO', '00-PARQUE', 'ARBOLADO'):
        if e.dxftype() == 'LINE':
            p1 = (round(e.dxf.start[0] - CX, 2), round(e.dxf.start[1] - CY, 2))
            p2 = (round(e.dxf.end[0] - CX, 2), round(e.dxf.end[1] - CY, 2))
            if -120 <= p1[0] <= 120 and -120 <= p1[1] <= 120:
                lines_urba.append({'layer': e.dxf.layer, 'pts': [p1, p2]})
        elif e.dxftype() == 'LWPOLYLINE':
            pts = [(round(p[0] - CX, 2), round(p[1] - CY, 2)) for p in e.get_points()]
            if any(-120 <= p[0] <= 120 and -120 <= p[1] <= 120 for p in pts):
                lines_urba.append({'layer': e.dxf.layer, 'pts': pts, 'closed': e.closed})

print(f"Líneas de trazado urbanístico extraídas: {len(lines_urba)}")

# 4. Guardar archivo data_mirapinos.json
data_mirapinos = {
    'promocion': {
        'nombre': 'Finca Mirapinos',
        'subtitulo': 'Viviendas Unifamiliares de Autor en Simancas',
        'ubicacion': 'Camino Viejo de Simancas (Valladolid)',
        'total_viviendas': len(units),
        'modelos': [
            {
                'nombre': 'Modelo Olivo',
                'superficie': '145 m²',
                'dormitorios': 4,
                'banos': '2 baños + 1 aseo',
                'descripcion': 'Diseñado en dos plantas con máxima luz natural, cocina integrada, porche cubierto y alta eficiencia con aerotermia.'
            },
            {
                'nombre': 'Modelo Arce',
                'superficie': '187 m²',
                'dormitorios': 4,
                'banos': '2 baños + 1 aseo',
                'descripcion': 'Gran amplitud de espacios, doble orientación, suite principal con vestidor y terraza solárium privada.'
            }
        ]
    },
    'units': units,
    'urbanizacion_lines': lines_urba
}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data_mirapinos, f, indent=2, ensure_ascii=False)

print("¡data.json para Mirapinos generado con éxito!")
