import json
import math

CX = 1190.0
CY = 740.0

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Coordinates corrected from DXF parcel polygons and the official Sector 10 Mirapinos plan:
# Parcela 18 & 19: Pareado central frente a la piscina (orientado hacia el jardín/piscina)
# Polígono 18: ~ (1165.5, 755.0) -> x: -24.5, y: 15.0, rot: 299 (o 119)
# Polígono 19: ~ (1160.0, 745.0) -> x: -30.0, y: 5.0, rot: 299

# Parcela 27 & 28: Pareado central inferior frente al vial y piscina
# Polígono 27: (1176.37, 718.50) -> x: 1176.37 - 1190 = -13.63, y: 718.50 - 740 = -21.5, rot: 282.3
# Polígono 28: (1178.83, 707.27) -> x: 1178.83 - 1190 = -11.17, y: 707.27 - 740 = -32.73, rot: 282.3

# Let's inspect current units
for u in data['units']:
    num = u['numero']
    if num == 18:
        u['x'] = round(1165.5 - CX, 2)  # -24.5
        u['y'] = round(755.0 - CY, 2)   # 15.0
        u['rot'] = 119.0
        u['orientacion'] = 'Sureste / Piscina'
    elif num == 19:
        u['x'] = round(1160.0 - CX, 2)  # -30.0
        u['y'] = round(745.0 - CY, 2)   # 5.0
        u['rot'] = 119.0
        u['orientacion'] = 'Sureste / Piscina'
    elif num == 27:
        u['x'] = round(1176.37 - CX, 2) # -13.63
        u['y'] = round(718.50 - CY, 2)  # -21.50
        u['rot'] = 102.3
        u['orientacion'] = 'Sur / Piscina'
    elif num == 28:
        u['x'] = round(1178.83 - CX, 2) # -11.17
        u['y'] = round(707.27 - CY, 2)  # -32.73
        u['rot'] = 102.3
        u['orientacion'] = 'Sur / Piscina'

# Add common area elements (Piscina comunitaria, pista deportiva, zona de juegos)
data['amenities'] = {
    'piscina': {
        'x': round(1202.0 - CX, 2), # 12.0
        'y': round(745.0 - CY, 2),  # 5.0
        'ancho': 18.0,
        'largo': 8.0,
        'profundidad': 1.6,
        'solarium_ancho': 28.0,
        'solarium_largo': 18.0,
        'rot': 25.0
    },
    'pista_deportiva': {
        'x': round(1238.0 - CX, 2), # 48.0
        'y': round(765.0 - CY, 2),  # 25.0
        'ancho': 22.0,
        'largo': 12.0,
        'rot': 35.0
    }
}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("data.json actualizado con posiciones corregidas y amenities!")
