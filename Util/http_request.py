import requests
from bs4 import BeautifulSoup

ROOT_PATH: str = "https://x.com/"
URI_PATH: str = "g1"
HEADERS: dict = {"user-agent": "Mozilla/5.0"}
response = requests.get(f"{ROOT_PATH}{URI_PATH}", headers=HEADERS)


soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())

spans = soup.find_all('span')

for span in spans:
    print(span)