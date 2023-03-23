import requests
from bs4 import BeautifulSoup
import pandas as pd
# import pandas_gbq

def read_stations(url: str, table_name: str) -> pd.DataFrame: 
    '''Returns a dataframe from a website url and html table'''
    url = url
    response = requests.get(url)
    # Parse the HTML content of the response and assign it to a BeautifulSoup object.
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the HTML table element with a specific ID 
    table = soup.find('table', id=table_name)
    dataframe = pd.read_html(str(table))[0]
    return dataframe

def clean_data(dataframe :pd.DataFrame) -> pd.DataFrame:
    '''Returns a clean dataframe, fixing headers and duplicated columns'''
    # assign the first row to be the column headers
    dataframe.columns = ["STATION", "ID", "ELEVATION FT", "LATITUDE", "LONGITUDE", "COUNTY", "OPERATOR AGENCY"]
    # convert all columns to the string data type
    dataframe = dataframe.astype(str)
    return dataframe

def get_river_names(dataframe :pd.DataFrame)-> pd.DataFrame:
    dataframe['RIVER'] = ''
    current_river = ''
    for i, row in dataframe.iterrows():
        if row['STATION'] == row['ID'] and row['ID'] == row['ELEVATION FT']:
            current_river = row['STATION']
        dataframe.at[i, 'RIVER'] = current_river
    
    dataframe = dataframe[dataframe['STATION'] != dataframe['ID']]
   
    return dataframe


url = "https://cdec.water.ca.gov/reportapp/javareports?name=DailyPrecip"

table_name = "REALPRECIP_LIST"

station_data = read_stations(url, table_name)

station_data = clean_data(station_data)

station_data = get_river_names(station_data)

print(station_data.head())

print(station_data.info())

station_data.to_csv('station_data.csv')

# Next step writing to bigquery

# bq_table_name = "tranquil-gasket-374723.cali_weather.weather_stations"

# pandas_gbq.to_gbq(station_data, bq_table_name, project_id="tranquil-gasket-374723")