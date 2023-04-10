from google.cloud import storage
import requests
import json

# Define the API endpoint URL and parameters
url = "https://cdec.water.ca.gov/dynamicapp/req/JSONDataServlet"
# Define the list of station IDs
station_ids = ['PTR', 'CCH', 'BRY', '5SI', 'KTT', 'CAU', 'CWD', 'DTV', 'KPI']

# Create a comma-separated string of station IDs
station_ids_str = ",".join(station_ids)

# Update the params dictionary with the new values
params = {
    "Stations": station_ids_str,
    "SensorNums": "2",
    "dur_code": "D",
    "Start": "2023-01-01",
    "End": "2023-01-02"
}

# Send a GET request to the API endpoint and get the JSON response
response = requests.get(url, params=params)
data = json.loads(response.text)

# Set the name of your bucket and the name of the object you want to create
bucket_name = "cali-rainfall-data-analysis"
object_name = "rainfall-data.json"

# Save the JSON response to a file
with open(object_name, "w") as f:
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
