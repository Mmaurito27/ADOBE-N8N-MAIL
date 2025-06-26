from datetime import datetime
import csv
import os


def registrar_conversion(nombre_archivo: str, estado: str) -> None:
    """Registrar conversion en logs/conversiones.log."""
    log_dir = os.path.join(os.path.dirname(__file__))
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "conversiones.log")
    file_exists = os.path.exists(log_path)
    with open(log_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["timestamp", "nombre_archivo", "estado"])
        writer.writerow([datetime.now().isoformat(), nombre_archivo, estado])

