import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')

modelos = ['OLIVO 1', 'OLIVO 2', 'ALZADOS ARCE 1', 'ALZADOS ARCE 2', 'ALZADOS ARCE 3', 'Cooliving 1']
print("Buscando bloques de modelos principales...")
for b in doc.blocks:
    if any(m.lower() in b.name.lower() for m in ['olivo', 'arce', 'cooliving', 'baja', 'alta', 'vivienda']):
        print(f"Bloque '{b.name}': {len(b)} entidades")
