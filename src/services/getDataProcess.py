from google.cloud import bigquery
import os
from dotenv import load_dotenv
from google.oauth2 import service_account
from src.services.getPostcode import get_postcodes1
from google.api_core.exceptions import NotFound


load_dotenv()

credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
database_name = os.getenv('DATABASE_NAME')
table_db = os.getenv('TABLE_DB')
table_result = os.getenv('TABLE_RESULT')
project_id = os.getenv('PROJECT_NAME')
table_new= os.getenv('TABLE_RESULT')

if not credentials_path:
    raise EnvironmentError("Credentials path not found in GOOGLE_APPLICATION_CREDENTIALS environment variable")

credentials = service_account.Credentials.from_service_account_file(credentials_path)

bigquery_client = bigquery.Client(credentials=credentials)


def insert_data_to_bigquery(table_result, data):
    table_ref = bigquery_client.dataset(database_name).table(table_result)
    try:
        table = bigquery_client.get_table(table_ref)
    except NotFound:
        schema = [
            bigquery.SchemaField("id", "INTEGER"),
            bigquery.SchemaField("lat", "FLOAT"),
            bigquery.SchemaField("lon", "FLOAT"),
            bigquery.SchemaField("postcode", "STRING")
        ]
        table = bigquery.Table(table_ref, schema=schema)
        table = bigquery_client.create_table(table)

    rows_to_insert = [data]
    errors = bigquery_client.insert_rows(table, rows_to_insert)

    if errors == []:
        print("Data successfully inserted into BigQuery.")
    else:
        print("Error inserting data into BigQuery:", errors)

def read_root(start, end):
    query = f"SELECT * FROM `{database_name}.{table_db}` WHERE id BETWEEN {start} AND {end}"
    query_job = bigquery_client.query(query)
    rows = query_job.result()
    results = [dict(row) for row in rows]

    postcode_results = []

    for result in results:
        lat = result['lat']
        lon = result['lon']
        postcode = get_postcodes1(lat, lon)
        result['postcode'] = postcode
        postcode_results.append(result)

    for result in postcode_results:
        insert_data_to_bigquery(table_new, result)

    return {"message": "Process completed successfully."}