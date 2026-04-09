from src.extract import extract_weather, save_raw_data
from src.transform import transform_data, save_processed_data
from src.load import upload_to_s3


def run_pipeline():
    print("🚀 Iniciando pipeline...")

    # Extract
    print("📥 Extraindo dados da API...")
    data = extract_weather()
    save_raw_data(data)

    # Transform
    print("🔄 Transformando dados...")
    df = transform_data()

    # Load (local)
    print("💾 Salvando dados processados...")
    save_processed_data(df)

    # Load (cloud)
    print("☁️ Enviando dados para S3...")
    upload_to_s3()

    print("✅ Pipeline finalizado com sucesso!")


if __name__ == "__main__":
    run_pipeline()