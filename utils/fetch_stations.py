import requests
from bs4 import BeautifulSoup
import pandas as pd
import pandas_gbq

def read_stations(url: str, table_name: str) -> pd.DataFrame: 
    '''Returns a dataframe from a website url and html table'''
    url = url
    response = requests.get(url)
    # Parse the HTML content of the response and assign it to a BeautifulSoup object.
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the HTML table element with a specific ID 
    table = soup.find('table', id=table_name)
    df = pd.read_html(str(table))[0]
    return df

def clean_data(dataframe :pd.DataFrame) -> pd.DataFrame:
    '''Returns a clean dataframe, fixing headers and duplicated columns'''
    # assign the first row to be the column headers
    dataframe.columns = dataframe.iloc[0]
    # delete the first row 
    dataframe = dataframe[1:]
    # reset the index 
    dataframe = dataframe.reset_index(drop=True) 

def get_river_names(dataframe :pd.DataFrame)-> pd.DataFrame:
    # create a new column called "RIVER" and initialize it to null
    dataframe['RIVER'] = ''  
    # iterate through the dataframe rows
    current_river = ''
    for i, row in dataframe.iterrows():
    # check if this row contains the river name
        if row['STATION'] == row['ID'] and row['ID'] == row['ELEV(FEET)']:
        # update the current river and set the "RIVER" value for this row
            current_river = row['STATION']
            dataframe.at[i, 'RIVER'] = current_river
        else:
        # if this is not a river row, set the "RIVER" value to the current river
            dataframe.at[i, 'RIVER'] = current_river

url = "https://cdec.water.ca.gov/reportapp/javareports?name=DailyPrecip"

table_name = "REALPRECIP_LIST"

station_data = read_stations(url, table_name)

station_data = clean_data(station_data)

stations_data = get_river_names(station_data)

# Next step writing to bigquery

# bq_table_name = "tranquil-gasket-374723.cali_weather.weather_stations"

# pandas_gbq.to_gbq(station_data, bq_table_name, project_id="tranquil-gasket-374723")