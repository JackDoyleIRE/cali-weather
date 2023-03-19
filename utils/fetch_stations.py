import requests
from bs4 import BeautifulSoup
import pandas as pd

def read_stations(url: str, table_name: str) -> pd.DataFrame: 
    url = url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', id="REALPRECIP_LIST")
    df = pd.read_html(str(table))[0]
    return df

url = "https://cdec.water.ca.gov/reportapp/javareports?name=DailyPrecip"

table_name = "REALPRECIP_LIST"

station_data = read_stations(url, table_name)

print(station_data.head())

