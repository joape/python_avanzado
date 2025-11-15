"""
A partir del código anterior solicitar al usuario una ciudad, (y país si es necesario)
ver datos de la API https://openweathermap.org/api/geocoding-api
Usar funciones
"""

from pprint import pprint
import requests


API_KEY = "0192c56b53f3118e7e26f50005474a62"


def obtener_coordenadas(ciudad: str, pais: str = "") -> tuple[float, float] | None:
    """Devuelve latitud y longitud de una ciudad usando la API de geocodificación."""
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={ciudad},{pais}&appid={API_KEY}&limit=1"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos:
            lat = datos[0]["lat"]
            lon = datos[0]["lon"]
            return lat, lon
        else:
            print("❌ No se encontraron resultados para esa ciudad.")
    else:
        print("❌ Error al conectar con la API.")
    return None


def obtener_clima(lat: float, lon: float) -> None:
    """Consulta la API del clima y muestra los datos principales."""
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=es"
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos = respuesta.json()
        pprint(datos)  # Muestra todo el JSON para inspeccionar (puede quitarse)
        temp = datos["main"]["temp"]
        descripcion = datos["weather"][0]["description"]
        nombre_ciudad = datos["name"]
        print()
        print(f" En {nombre_ciudad}, la temperatura es {temp}°C — {descripcion}.")
    else:
        print("❌ No se pudo obtener la información del clima.")


def main() -> None:
    print("=== Consulta del clima 🌦️ ===")
    ciudad = input("Ingrese la ciudad: ").strip()
    pais = input("Ingrese el país (opcional, ej. 'UY', 'AR', 'ES'): ").strip()

    coordenadas = obtener_coordenadas(ciudad, pais)
    if coordenadas:
        lat, lon = coordenadas
        obtener_clima(lat, lon)
    else:
        print("No se pudo obtener la ubicación.")

   
   

main()
