from google.cloud import storage
import requests
import json

# Define the API endpoint URL and parameters
url = "https://cdec.water.ca.gov/dynamicapp/req/JSONDataServlet"
params = {"Stations": "SDF", "SensorNums": "2", "dur_code": "D", "Start": "2023-01-01", "End": "2023-01-02"}

# Send a GET request to the API endpoint and get the JSON response
response = requests.get(url, params=params)
data = json.loads(response.text)

# Set the name of your bucket and the name of the object you want to create
bucket_name = "cali-rainfall-data-analysis"
object_name = "rainfall-data.json"

# Save the JSON response to a file
with open(object_name, "w") as f:
    json.dump(data, f)

# Upload the file to Google Cloud Storage
storage_client = storage.Client(project="tranquil-gasket-374723")
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(object_name)
blob.upload_from_filename(object_name)

print(f"File {object_name} uploaded to bucket {bucket_name}")
