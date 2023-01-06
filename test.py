from requests import get
from bs4 import BeautifulSoup

base_url = "https://www.naver.com/"

response = get(f"{base_url}")
print(response.status_code)
if response.status_code == 200:
    soup = BeautifulSoup(response.text,"html.parser")
    print(soup.find_all("section",class_="jobs"))