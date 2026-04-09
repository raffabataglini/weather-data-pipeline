from src.extract import extract_weather, save_raw_data
from src.transform import transform_data, save_processed_data
from src.load import upload_to_s3
import pandas as pd
import os


def run_pipeline():
    print("🚀 Iniciando pipeline...")

    cities = {
        "Guararema": (-23.41, -46.03),
        "Mogi das Cruzes": (-23.52, -46.18),
        "Jacarei": (-23.30, -45.96),
        "Sao Jose dos Campos": (-23.17, -45.88)
    }

    all_dfs = []

    # EXTRACT + SAVE RAW
    for city, coords in cities.items():
        print(f"📥 Extraindo dados de {city}...")
        data = extract_weather(city, coords[0], coords[1])
        save_raw_data(data)

    # TRANSFORM (todos arquivos RAW)
    print("🔄 Transformando dados...")
    raw_files = os.listdir("data/raw")
    raw_files = [f for f in raw_files if f.endswith(".json")]

    for file in sorted(raw_files)[-len(cities):]:  # pega os últimos 4 arquivos
        file_path = f"data/raw/{file}"
        df = transform_data(file_path)
        all_dfs.append(df)

    # CONSOLIDAÇÃO
    final_df = pd.concat(all_dfs)

    # LOAD LOCAL
    print("💾 Salvando dados processados...")
    save_processed_data(final_df)

    # LOAD CLOUD
    print("☁️ Enviando para S3...")
    upload_to_s3()

    print("✅ Pipeline finalizado!")


if __name__ == "__main__":
    run_pipeline()