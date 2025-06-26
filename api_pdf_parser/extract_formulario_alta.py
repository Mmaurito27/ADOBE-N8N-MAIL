import base64
import os
import tempfile

from flask import Flask, jsonify, request
import pdfplumber
import pandas as pd

from helpers import parser

app = Flask(__name__)


@app.route("/convertir_pdf", methods=["POST"])
def convertir_pdf():
    data = request.get_json(force=True)
    nombre_archivo = data.get("nombre_archivo", "temp.pdf")
    contenido_b64 = data.get("contenido_base64")
    if not contenido_b64:
        return jsonify({"error": "contenido_base64 requerido"}), 400

    # Guardar PDF temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        pdf_path = temp_pdf.name
        temp_pdf.write(base64.b64decode(contenido_b64))

    # Extraer texto del PDF
    texto_extraido = ""
    with pdfplumber.open(pdf_path) as pdf:
        for pagina in pdf.pages:
            page_text = pagina.extract_text() or ""
            texto_extraido += page_text + "\n"

    # Parsear campos
    nombre = parser.parse_nombre(texto_extraido)
    cuit = parser.parse_cuit(texto_extraido)
    email = parser.parse_email(texto_extraido)

    # Generar CSV con pandas
    df = pd.DataFrame({"Nombre": [nombre], "CUIT": [cuit], "Email": [email]})
    csv_content = df.to_csv(index=False)

    # Borrar el archivo temporal
    os.remove(pdf_path)

    return jsonify({
        "texto_extraido": texto_extraido,
        "csv": csv_content
    })


if __name__ == "__main__":
    app.run(debug=True)

