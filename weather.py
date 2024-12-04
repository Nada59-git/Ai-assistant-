
import requests
import config

def Weather(city):
    api_key = config.OPENWEATHER_API_KEY  # Replace this with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Build query parameters
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # Fetch temperature in Celsius
        "lang": "en"  # Language for weather description
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Check if the response contains valid data
        if response.status_code == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            location = data["name"]
            country = data["sys"]["country"]
            return f"Weather in {location}, {country}: {temp}°C, {description.capitalize()}"
        elif response.status_code == 404:
            return "City not found. Please check the spelling and try again."
        else:
            return "Error retrieving weather data. Please try again later."

    except Exception as e:
        return f"An error occurred: {str(e)}"

