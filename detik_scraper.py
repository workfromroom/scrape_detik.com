import requests
from bs4 import BeautifulSoup

html_doc = requests.get("https://www.detik.com/terpopuler")

soup = BeautifulSoup(html_doc.text,"html.parser")

populer_area = soup.find(attrs={"class":"grid-row list-content"})

title = populer_area.findAll(attrs={"class":"media__text"})

image = populer_area.findAll(attrs={"class":"media__image"})

for i in image:
    print(i.find('a').find("img"))