import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

print("Textos en zona urbanización con 18, 19, 20, 27, 28, 29:")
for e in msp:
    if e.dxftype() in ('TEXT', 'MTEXT'):
        ins = e.dxf.insert
        if 1100 <= ins[0] <= 1260 and 640 <= ins[1] <= 830:
            txt = (e.dxf.text if e.dxftype() == 'TEXT' else e.text).strip()
            if txt in ('18', '19', '20', '21', '26', '27', '28', '29', '30'):
                print(f"[{e.dxf.layer}] ({ins[0]:.2f}, {ins[1]:.2f}): '{txt}'")
