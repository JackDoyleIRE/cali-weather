import requests
from bs4 import BeautifulSoup

url = "https://cdec.water.ca.gov/reportapp/javareports?name=DailyPrecip"

response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', id="REALPRECIP_LIST")

print(table)

