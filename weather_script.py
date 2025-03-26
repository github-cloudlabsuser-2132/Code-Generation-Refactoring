import requests

def get_weather(city, api_key, country_code=None):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    query = f"{city},{country_code}" if country_code else city
    params = {
        "q": query,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }
        return weather
    else:
        return {"error": f"Unable to fetch weather data. HTTP Status Code: {response.status_code}"}

def main():
    api_key = "your_openweathermap_api_key"  # Replace with your OpenWeatherMap API key
    print("Weather Data")
    print("1. Enter a city")
    print("2. Get weather for Argentina")
    choice = input("Choose an option (1/2): ")

    if choice == "1":
        city = input("Enter the city name: ")
        weather_data = get_weather(city, api_key)
    elif choice == "2":
        city = input("Enter the city name in Argentina: ")
        weather_data = get_weather(city, api_key, country_code="AR")
    else:
        print("Invalid choice")
        return

    if "error" in weather_data:
        print(weather_data["error"])
    else:
        print(f"Weather in {weather_data['city']}:")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Description: {weather_data['description']}")
        print(f"Humidity: {weather_data['humidity']}%")

if __name__ == "__main__":
    main()
