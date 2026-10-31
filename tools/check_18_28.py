import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

print("Textos con 18, 19, 20, 27, 28, 29, etc:")
for e in msp:
    if e.dxftype() in ('TEXT', 'MTEXT'):
        ins = e.dxf.insert
        txt = (e.dxf.text if e.dxftype() == 'TEXT' else e.text).strip()
        if any(k in txt for k in ['18', '19', '20', '26', '27', '28', '29', 'FASE 1']):
            print(f"[{e.dxf.layer}] ({ins[0]:.2f}, {ins[1]:.2f}): '{txt}'")
