# Finca Mirapinos · Urbanización 3D Interactiva

Web interactiva de la promoción **Finca Mirapinos** (35 chalets unifamiliares con parcelas individuales en Simancas, Valladolid): urbanización 3D interactiva con disponibilidad en tiempo real, ficha individual de cada chalet, orientación solar, desglose de calidades y cuota orientativa de hipoteca.

## 🚀 Contenido

| Archivo / Carpeta | Qué es |
|---|---|
| `index.html` | La aplicación completa (HTML5 + CSS3 + JavaScript / Three.js desde CDN) |
| `data.json` | Trazado urbanístico, geometrías y datos de las 35 parcelas (estado, superficie de parcela, metros construidos, dormitorios, precios) |
| `tools/` | Scripts en Python para procesar el plano DXF de arquitectura y regenerar los datos urbanísticos |
| `netlify.toml` | Configuración para despliegue automático en Netlify |

## 📐 Cambiar la disponibilidad o los precios

Los estados y precios se actualizan en `data.json` dentro de la lista `units`:

```json
{
  "id": "P-01",
  "numero": 1,
  "nombre": "Chalet Parcela 1",
  "tipologia": "Olivo 1",
  "estado": "LIBRE",
  "precio": 338500,
  "sup_parcela": 501.96
}
```

El campo `estado` admite `LIBRE`, `RESERVADA` o `VENDIDA`.

## 💻 Probar en local

Cualquier servidor estático sirve:

```bash
python -m http.server 8080
# y abrir en el navegador http://localhost:8080
```
