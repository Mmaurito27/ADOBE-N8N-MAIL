import base64
import os
import tempfile

from flask import Flask, jsonify, request
import pdfplumber
import pandas as pd

from helpers import parser
from utils.validaciones import (
    validar_base64,
    validar_claves_obligatorias,
    validar_extension_pdf,
)

app = Flask(__name__)


@app.route("/convertir_pdf", methods=["POST"])
def convertir_pdf():
    data = request.get_json(force=True)

    valido, error = validar_claves_obligatorias(data)
    if not valido:
        return jsonify({"error": error}), 400

    nombre_archivo = data.get("nombre_archivo")
    contenido_b64 = data.get("contenido_base64")

    valido, error = validar_extension_pdf(nombre_archivo)
    if not valido:
        return jsonify({"error": error}), 400

    valido, error = validar_base64(contenido_b64)
    if not valido:
        return jsonify({"error": error}), 400

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

