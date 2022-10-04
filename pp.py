from urllib import response
import requests
from bs4 import BeautifulSoup

USER_NAME = 'donny.rivera@jumpplus.com'
PASSWORD = 'R1v3r413'
URL = 'https://gsx2.apple.com/settings/permissions'

response = requests.get(URL, auth=('USER_NAME', 'PASSWORD'))
soup = BeautifulSoup(response.text, 'lxml')
#tables = soup.find_all('div', class_='ag-cell-value')
print(soup)