"""
Simulación de base de datos JSON

1. Leer el archivo un archivo json, y convertirlo en un objeto Python (lista)
2. Pedir al usuario que introduzca más datos
        "name", "age", "city", "active"
3. Crear un dicccionario con estos datos, agregarlos a la lista
4. Guardar la lista reemplanzando el archivo json.
Usar with, try-except, logging
"""
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

DB_PATH = Path(__file__).parent / "db.json"

def cargar_db(path):
    try:
        if not path.exists():
            logging.info("Archivo JSON no encontrado. Se iniciará una lista vacía.")
            return []
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        logging.error("Error leyendo JSON: %s", e)
        return []

def guardar_db(path, data):
    try:
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logging.info("Base de datos guardada en %s", path)
    except OSError as e:
        logging.error("Error guardando JSON: %s", e)

def ingreso_int(prompt):
    while True:
        try:
            return int(input(prompt + " ").strip())
        except ValueError:
            print("Entrada inválida. Introduce un número entero.")

def ingreso_bool(prompt):
    v = input(prompt + " (y/n) ").strip().lower()
    return v in ("y", "yes", "true", "1")

def main():
    db = cargar_db(DB_PATH)

    name = input("name: ").strip()
    age = ingreso_int("age:")
    city = input("city: ").strip()
    active = ingreso_bool("active:")

    record = {"name": name, "age": age, "city": city, "active": active}
    db.append(record)
    logging.info("Registro agregado: %s", record)

    guardar_db(DB_PATH, db)


main()