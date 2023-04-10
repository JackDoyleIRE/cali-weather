from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client(project="tranquil-gasket-374723")

# Set table_id to the ID of the table to create.
table_id = "tranquil-gasket-374723.cali_weather.rainfall_data"

job_config = bigquery.LoadJobConfig(
    
    schema = [
    bigquery.SchemaField("stationId", "STRING"),
    bigquery.SchemaField("durCode", "STRING"),
    bigquery.SchemaField("SENSOR_NUM", "INTEGER"),
    bigquery.SchemaField("sensorType", "STRING"),
    bigquery.SchemaField("date", "DATETIME"),
    bigquery.SchemaField("obsDate", "DATETIME"),
    bigquery.SchemaField("value", "FLOAT"),
    bigquery.SchemaField("dataFlag", "STRING"),
    bigquery.SchemaField("units", "STRING"),
], 

    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,

)
uri = "gs://cali-rainfall-data-analysis/rainfall-data.json"

load_job = client.load_table_from_uri(
    uri,
    table_id,
    job_config=job_config,
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

if load_job.errors:
    print("Errors encountered while loading data:")
    for error in load_job.errors:
        print(error['message'])

destination_table = client.get_table(table_id)
print("Loaded {} rows.".format(destination_table.num_rows))