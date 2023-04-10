from google.cloud import bigquery
from google.cloud import storage
import requests
import json

# Create a BigQuery client object.
bq_client = bigquery.Client(project="tranquil-gasket-374723")

# Set the ID of the table containing the weather station information.
table_id = "tranquil-gasket-374723.cali_weather.weather_stations"

# Define the API endpoint URL and parameters
url = "https://cdec.water.ca.gov/dynamicapp/req/JSONDataServlet"

# Set the name of your bucket and the name of the object you want to create
bucket_name = "cali-rainfall-data-analysis"
object_name = "rainfall-data.json"

# Define the date range for the API calls
start_date = "2023-01-01"
end_date = "2023-01-02"

# Construct a SQL query to retrieve the weather station IDs.
query = f"""
    SELECT DISTINCT id
    FROM `{table_id}`
    ORDER BY id
"""

# Execute the query and retrieve the results.
query_job = bq_client.query(query)
results = query_job.result()

# Extract the weather station IDs into a Python list.
station_ids = [row.id for row in results]

# Make API calls with a limit of 50 stations per call
for i in range(0, len(station_ids), 50):
    # Create a comma-separated string of station IDs for this API call
    station_ids_str = ",".join(station_ids[i:i+50])

    # Update the params dictionary with the new values
    params = {
        "Stations": station_ids_str,
        "SensorNums": "2",
        "dur_code": "D",
        "Start": start_date,
        "End": end_date
    }

    # Send a GET request to the API endpoint and get the JSON response
    response = requests.get(url, params=params)

    # Parse the JSON response
    data = json.loads(response.text)

    # Save the JSON response to a file
    with open(object_name, "a") as f:
        for item in data:
            json.dump(item, f)
            f.write('\n')

with open('rainfall-data.json') as f:
    data = f.readlines()

for i, line in enumerate(data):
    json_data = json.loads(line)
    date = json_data["date"]
    obs_date = json_data["obsDate"]
    json_data["date"] = f"{date}:00"
    json_data["obsDate"] = f"{obs_date}:00"
    data[i] = json.dumps(json_data)

with open('rainfall-data.json', 'w') as f:
    for line in data:
        f.write(json.dumps(json.loads(line)) + '\n')

# Upload the file to Google Cloud Storage
storage_client = storage.Client(project="tranquil-gasket-374723")
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(object_name)
blob.upload_from_filename(object_name)

print(f"File {object_name} uploaded to bucket {bucket_name}")
