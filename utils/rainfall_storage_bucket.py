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
object_name = "rainfall-data"

# Create a client object for Cloud Storage
client = storage.Client()

# Get a reference to the bucket
bucket = client.bucket(bucket_name)

# Create a Blob object for the new object
blob = bucket.blob(object_name)

# Convert the JSON object to a string
json_object = data
json_string = json.dumps(json_object)

# Upload the JSON string to the Cloud Storage bucket
blob.upload_from_string(json_string, content_type="application/json")

