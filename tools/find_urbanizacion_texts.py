import ezdxf

doc = ezdxf.readfile('Plano Juan.dxf')
msp = doc.modelspace()

# Search for any text or entity mentioning 14, 17, 27, 28 with X > 1000
print("Buscando textos en la zona urbanización (X: 1100 a 1260, Y: 640 a 830)...")
for e in msp:
    if e.dxftype() in ('TEXT', 'MTEXT'):
        ins = e.dxf.insert
        if 1100 <= ins[0] <= 1260 and 640 <= ins[1] <= 830:
            txt = (e.dxf.text if e.dxftype() == 'TEXT' else e.text).strip()
            print(f"[{e.dxf.layer}] ({ins[0]:.1f}, {ins[1]:.1f}): '{txt}'")
