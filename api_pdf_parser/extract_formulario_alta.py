# Script base para convertir PDF a CSV
import pdfplumber
import pandas as pd

def extraer_datos_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        texto = ""
        for pagina in pdf.pages:
            texto += pagina.extract_text() + "\n"

    # Procesamiento ficticio: este bloque se adapta al contenido real
    datos = {
        "Nombre": ["Ejemplo"],
        "CUIT": ["20-12345678-9"],
        "Email": ["ejemplo@cliente.com"]
    }
    df = pd.DataFrame(datos)
    csv_path = pdf_path.replace(".pdf", ".csv")
    df.to_csv(csv_path, index=False)
    return csv_path
