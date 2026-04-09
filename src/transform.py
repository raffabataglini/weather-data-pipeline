import json
import pandas as pd
import os

def get_latest_file():
    files = os.listdir("data/raw")
    files = [f for f in files if f.endswith(".json")]
    latest_file = sorted(files)[-1]
    return f"data/raw/{latest_file}"


def transform_data():
    file_path = get_latest_file()

    with open(file_path, "r") as f:
        data = json.load(f)

    # extrair dados relevantes
    times = data["hourly"]["time"]
    temperatures = data["hourly"]["temperature_2m"]

    df = pd.DataFrame({
        "datetime": times,
        "temperature": temperatures
    })

    # conversão de tipo
    df["datetime"] = pd.to_datetime(df["datetime"])

    return df


def save_processed_data(df):
    os.makedirs("data/processed", exist_ok=True)

    file_path = "data/processed/weather.csv"

    df.to_csv(file_path, index=False)

    print(f"Dados processados salvos em: {file_path}")


if __name__ == "__main__":
    df = transform_data()
    save_processed_data(df)