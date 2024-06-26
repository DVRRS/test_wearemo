from fastapi.responses import JSONResponse
import pandas as pd
from google.cloud import storage, bigquery
from io import BytesIO
import os
from dotenv import load_dotenv
from google.oauth2 import service_account

load_dotenv()

credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
database_name = os.getenv('DATABASE_NAME')
table_db = os.getenv('TABLE_DB')

if not credentials_path:
    raise EnvironmentError("Credentials path not found in GOOGLE_APPLICATION_CREDENTIALS environment variable")

credentials = service_account.Credentials.from_service_account_file(credentials_path)
storage_client = storage.Client(credentials=credentials)
bigquery_client = bigquery.Client(credentials=credentials)

def clean_and_convert_to_float(value):
    if pd.isna(value):
        return None
    cleaned_value = value.replace("'", "")
    if cleaned_value.lower() == 'nan':
        return None
    return float(cleaned_value.replace(',', '.'))

def read_csv(bucket, blob):
    bucket = storage_client.bucket(bucket)
    blob = bucket.blob(blob)

    byte_stream = BytesIO()
    blob.download_to_file(byte_stream)
    byte_stream.seek(0)

    df = pd.read_csv(byte_stream, sep='|')

    df['lat'] = df['lat'].apply(clean_and_convert_to_float)
    df['lon'] = df['lon'].apply(clean_and_convert_to_float)

    df = df.dropna()

    df['id'] = range(1, len(df) + 1)

    total_records = len(df)
    total_records = int(total_records)

    if total_records > 0:
        
        dataset_ref = bigquery_client.dataset(database_name)
        table_ref = dataset_ref.table(table_db)

        job_config = bigquery.LoadJobConfig()
        job_config.write_disposition = bigquery.WriteDisposition.WRITE_TRUNCATE
        job_config.source_format = bigquery.SourceFormat.PARQUET
        job_config.autodetect = True

        job = bigquery_client.load_table_from_dataframe(df, table_ref, job_config=job_config)
        job.result()

        table = bigquery_client.get_table(table_ref)
        num_rows = table.num_rows

        return JSONResponse(content={"total_records": total_records, "rows_uploaded_to_bq": num_rows})
    else:
        return JSONResponse(content={"message": "No rows with null values ​​were loaded."}) 
