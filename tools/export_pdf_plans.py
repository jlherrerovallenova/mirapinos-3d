import pymupdf

files = [
    ("media_1793447696021_e08ae7e6.pdf", "plano_general.png"),
    ("media_1793447717274_8ba7bc15.pdf", "plano_vivienda_1.png"),
    ("media_1793447717302_689a602e.pdf", "plano_vivienda_2.png"),
    ("media_1793447717322_25c84069.pdf", "plano_vivienda_5.png")
]

folder = r"C:\Users\Usuario\.gemini\antigravity\brain\1c211a04-9287-4947-9c98-a6f6f59d32da\.user_uploaded"

for pdf_name, out_name in files:
    doc = pymupdf.open(f"{folder}\\{pdf_name}")
    page = doc[0]
    pix = page.get_pixmap(dpi=150)
    pix.save(out_name)
    print(f"Exportado {out_name} ({pix.width}x{pix.height})")
