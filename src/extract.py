import requests
import json
from datetime import datetime

def extract_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    
    params = {
        "latitude": -23.55,
        "longitude": -46.63,
        "hourly": "temperature_2m"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data


def save_raw_data(data):

    # timestamp para versionamento
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = f"data/raw/weather_{timestamp}.json"

    with open(file_path, "w") as f:
        json.dump(data, f)

    print(f"Dados salvos em: {file_path}")


if __name__ == "__main__":
    data = extract_weather()
    save_raw_data(data)