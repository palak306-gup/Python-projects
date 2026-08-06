import requests

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def fetch_weather(self, city_name):
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": "metric"
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            return {
                "City": data["name"],
                "Temp": f"{data['main']['temp']}°C",
                "Condition": data["weather"][0]["description"].title()
            }
        except requests.exceptions.RequestException as e:
            return {"Error": f"Failed to fetch data: {e}"}

# Usage
# fetcher = WeatherFetcher("YOUR_API_KEY")
# print(fetcher.fetch_weather("Bilaspur"))
