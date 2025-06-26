import base64
from typing import Any, Tuple


def validar_base64(contenido_base64: Any) -> Tuple[bool, str]:
    """Valida que una cadena sea base64."""
    if not isinstance(contenido_base64, str):
        return False, "contenido_base64 debe ser una cadena"
    try:
        base64.b64decode(contenido_base64, validate=True)
        return True, ""
    except Exception:
        return False, "contenido_base64 no es una cadena base64 válida"


def validar_extension_pdf(nombre_archivo: Any) -> Tuple[bool, str]:
    """Valida que el nombre del archivo termine con .pdf."""
    if not isinstance(nombre_archivo, str):
        return False, "nombre_archivo debe ser una cadena"
    if nombre_archivo.lower().endswith(".pdf"):
        return True, ""
    return False, "nombre_archivo debe tener extensión .pdf"


def validar_claves_obligatorias(data: Any) -> Tuple[bool, str]:
    """Valida que existan las claves requeridas en el JSON."""
    if not isinstance(data, dict):
        return False, "Se esperaba un objeto JSON"
    obligatorias = ["nombre_archivo", "contenido_base64"]
    faltantes = [c for c in obligatorias if c not in data]
    if faltantes:
        return False, f"Faltan claves obligatorias: {', '.join(faltantes)}"
    return True, ""
