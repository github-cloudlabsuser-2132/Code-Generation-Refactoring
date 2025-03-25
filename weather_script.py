import requests

def obtener_clima(ciudad):
    # Reemplaza 'YOUR_API_KEY' con tu clave de API de OpenWeatherMap
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es&units=metric"

    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            print(f"Clima en {ciudad}:")
            print(f"Temperatura: {datos['main']['temp']}°C")
            print(f"Sensación térmica: {datos['main']['feels_like']}°C")
            print(f"Humedad: {datos['main']['humidity']}%")
            print(f"Descripción: {datos['weather'][0]['description']}")
        else:
            print(f"Error al obtener los datos: {respuesta.status_code} - {respuesta.json().get('message', 'Error desconocido')}")
    except Exception as e:
        print(f"Hubo un error al conectarse a la API: {e}")

if __name__ == "__main__":
    ciudad = input("Ingresa el nombre de la ciudad: ")
    obtener_clima(ciudad)