import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

print("Buscando textos 14, 17, 27, 28 con X entre 1100 y 1260...")
for e in msp:
    if e.dxftype() in ('TEXT', 'MTEXT'):
        ins = e.dxf.insert
        txt = (e.dxf.text if e.dxftype() == 'TEXT' else e.text).strip()
        if txt in ('14', '17', '27', '28'):
            print(f"[{e.dxf.layer}] ({ins[0]:.2f}, {ins[1]:.2f}): '{txt}'")
