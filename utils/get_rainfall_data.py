import requests
import json
from google.cloud import bigquery


# Define the API endpoint URL and parameters
uri = "gs://cali-rainfall-data-analysis"

# Send a GET request to the API endpoint and get the JSON response
response = requests.get(url, params=params)
data = json.loads(response.text)

# Set up a BigQuery client and define the target table
project_id = "tranquil-gasket-374723" # Replace with your project ID
client = bigquery.Client(project=project_id)
table_id = "tranquil-gasket-374723.cali_weather.rainfall_data"

# Define the schema of the target table


job_config = bigquery.LoadJobConfig(
    
    schema = [
    bigquery.SchemaField("stationId", "STRING"),
    bigquery.SchemaField("durCode", "STRING"),
    bigquery.SchemaField("SENSOR_NUM", "INTEGER"),
    bigquery.SchemaField("sensorType", "STRING"),
    bigquery.SchemaField("date", "TIMESTAMP"),
    bigquery.SchemaField("obsDate", "TIMESTAMP"),
    bigquery.SchemaField("value", "FLOAT"),
    bigquery.SchemaField("dataFlag", "STRING"),
    bigquery.SchemaField("units", "STRING"),
],

    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,

)



load_job = client.load_table_from_uri(

    url,

    table_id,

    job_config=job_config,

)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)

print("Loaded {} rows.".format(destination_table.num_rows))