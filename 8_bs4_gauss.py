import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=799793"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# titles = soup.find_all("td",attrs={"class":"title"})
# for title in titles:
#     print(title.a.get_text())
#     print("https://comic.naver.com"+ title.a["href"])
total_rates = 0
cartoons = soup.find_all("div",attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.strong.get_text()
    total_rates += float(rate)
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))