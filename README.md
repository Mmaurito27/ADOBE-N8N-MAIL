# ADOBE+N8N+MAIL

Sistema automático para:
- Leer correos con formularios PDF de alta al cliente.
- Convertir esos formularios a `.csv`.
- Utilizar flujos n8n conectados a una API Python.

## Estructura

- `api_pdf_parser/`: Scripts en Python para extraer info del PDF.
- `n8n_flows/`: Flujos exportados de n8n.
- `samples/`: Archivos de prueba PDF + CSV.

## Requisitos

- Python 3.10+
- n8n corriendo localmente o en servidor.
