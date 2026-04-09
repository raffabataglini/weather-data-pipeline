import boto3
import os

def upload_to_s3():
    # cria cliente S3 usando credenciais do ~/.aws/credentials
    s3 = boto3.client("s3")

    bucket_name = "pipeline-dados-raw"  

    # pega arquivos da camada RAW
    files = os.listdir("data/raw")
    files = [f for f in files if f.endswith(".json")]

    if not files:
        print("Nenhum arquivo encontrado em data/raw")
        return

    # pega o mais recente
    latest_file = sorted(files)[-1]
    file_path = f"data/raw/{latest_file}"

    # estrutura padrão de data lake
    s3_key = f"weather/raw/{latest_file}"

    # upload
    s3.upload_file(file_path, bucket_name, s3_key)

    print(f"Arquivo enviado para S3: s3://{bucket_name}/{s3_key}")