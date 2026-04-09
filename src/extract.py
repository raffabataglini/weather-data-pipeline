import requests
import json
from datetime import datetime

def extract_weather(city_name, lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m"
    }
    response = requests.get(url, params=params)
    data = response.json()
    data["city"] = city_name 
    return data

def save_raw_data(data):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    city = data["city"].replace(" ", "_").lower()
    file_path = f"data/raw/weather_{city}_{timestamp}.json"
    with open(file_path, "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    data = extract_weather()
    save_raw_data(data)