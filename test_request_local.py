import base64
import json
import requests


PDF_PATH = 'samples/alta_cliente.pdf'
ENDPOINT = 'http://localhost:5000/convertir_pdf'


def main() -> None:
    with open(PDF_PATH, 'rb') as f:
        contenido_b64 = base64.b64encode(f.read()).decode('utf-8')

    payload = {
        'nombre_archivo': 'alta_cliente.pdf',
        'contenido_base64': contenido_b64,
    }

    resp = requests.post(ENDPOINT, json=payload)
    try:
        data = resp.json()
    except Exception:
        print('Respuesta no es JSON:', resp.text)
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()

