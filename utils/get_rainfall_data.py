import requests
import json
from google.cloud import bigquery

# Define the API endpoint URL and parameters
url = "https://cdec.water.ca.gov/dynamicapp/req/JSONDataServlet"
params = {"Stations": "SDF", "SensorNums": "2", "dur_code": "D", "Start": "2023-01-01", "End": "2023-01-02"}

# Send a GET request to the API endpoint and get the JSON response
response = requests.get(url, params=params)
data = json.loads(response.text)

# Set up a BigQuery client and define the target table
client = bigquery.Client()
table_id = "tranquil-gasket-374723.cali_weather.rainfall_data"

# Define the schema of the target table
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
]

# Insert the JSON data into the target table
rows_to_insert = [tuple(d.values()) for d in data]
errors = client.insert_rows(table_id, rows_to_insert, schema=schema)

if errors == []:
    print("Data inserted successfully.")
else:
    print("Errors encountered:", errors)
