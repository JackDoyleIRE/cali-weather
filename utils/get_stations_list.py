from google.cloud import bigquery

# Create a BigQuery client object.
client = bigquery.Client(project="tranquil-gasket-374723")

# Set the ID of the table containing the weather station information.
table_id = "tranquil-gasket-374723.cali_weather.weather_stations"

# Construct a SQL query to retrieve the weather station IDs.
query = f"""
    SELECT id
    FROM `{table_id}`
"""

# Execute the query and retrieve the results.
query_job = client.query(query)
results = query_job.result()

# Extract the weather station IDs into a Python list.
station_ids = [row.id for row in results]

# Print the list of weather station IDs.
print(station_ids)
