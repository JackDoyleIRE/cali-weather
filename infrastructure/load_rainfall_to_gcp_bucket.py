from google.cloud import bigquery
from google.cloud import storage
import requests
import json
from typing import List, Dict, Any

# Define constants
PROJECT_ID = "tranquil-gasket-374723"
TABLE_ID = "tranquil-gasket-374723.cali_weather.weather_stations"
URL = "https://cdec.water.ca.gov/dynamicapp/req/JSONDataServlet"
BUCKET_NAME = "cali-rainfall-data-analysis"
OBJECT_NAME = "rainfall-data.json"
START_DATE = "2020-01-01"
END_DATE = "2023-04-01"

def bq_client() -> bigquery.Client:
    return bigquery.Client(project=PROJECT_ID)

def storage_client() -> storage.Client:
    return storage.Client(project=PROJECT_ID)

def get_station_ids(client: bigquery.Client) -> List[str]:
    query = f"""
        SELECT DISTINCT id
        FROM `{TABLE_ID}`
        ORDER BY id
    """
    query_job = client.query(query)
    results = query_job.result()
    return [row.id for row in results]

def fetch_data(station_ids_str: str) -> Dict[str, Any]:
    params = {
        "Stations": station_ids_str,
        "SensorNums": "2",
        "dur_code": "D",
        "Start": START_DATE,
        "End": END_DATE
    }
    response = requests.get(URL, params=params)
    return json.loads(response.text)

def store_data(data: Dict[str, Any], filename: str) -> None:
    with open(filename, "a") as f:
        for item in data:
            json.dump(item, f)
            f.write('\n')

def process_data(filename: str) -> None:
    with open(filename) as f:
        data = f.readlines()
    processed_data = [process_line(line) for line in data]
    with open(filename, 'w') as f:
        for line in processed_data:
            f.write(line + '\n')

def process_line(line: str) -> str:
    json_data = json.loads(line)
    date = json_data["date"]
    obs_date = json_data["obsDate"]
    json_data["date"] = f"{date}:00"
    json_data["obsDate"] = f"{obs_date}:00"
    return json.dumps(json_data)

def upload_file(client: storage.Client, bucket_name: str, object_name: str, filename: str) -> None:
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(filename)
    print(f"File {object_name} uploaded to bucket {bucket_name}")

def main() -> None:
    try:
        bq = bq_client()
        print("BigQuery client created successfully.")
    except Exception as e:
        print(f"Error creating BigQuery client: {e}")
        return

    try:
        storage = storage_client()
        print("Storage client created successfully.")
    except Exception as e:
        print(f"Error creating Storage client: {e}")
        return

    try:
        station_ids = get_station_ids(bq)
        print("Weather station IDs retrieved successfully.")
    except Exception as e:
        print(f"Error retrieving weather station IDs: {e}")
        return

    for i in range(0, len(station_ids), 50):
        station_ids_str = ",".join(station_ids[i:i+50])

        try:
            data = fetch_data(station_ids_str)
            print(f"Data fetched successfully for stations {station_ids_str}.")
        except Exception as e:
            print(f"Error fetching data for stations {station_ids_str}: {e}")
            continue

        try:
            store_data(data, OBJECT_NAME)
            print(f"Data stored successfully for stations {station_ids_str}.")
        except Exception as e:
            print(f"Error storing data for stations {station_ids_str}: {e}")
            continue

    try:
        process_data(OBJECT_NAME)
        print("Data processing completed successfully.")
    except Exception as e:
        print(f"Error processing data: {e}")
        return

    try:
        upload_file(storage, BUCKET_NAME, OBJECT_NAME, OBJECT_NAME)
        print("Data uploaded successfully to Google Cloud Storage.")
    except Exception as e:
        print(f"Error uploading data to Google Cloud Storage: {e}")

if __name__ == "__main__":
    main()

