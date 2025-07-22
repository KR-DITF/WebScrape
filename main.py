import requests
from bs4 import BeautifulSoup
import re


import time

## pārgāju no IMDB uz Rotten Tomatoes

ImdbSite = 'https://editorial.rottentomatoes.com/guide/best-movies-of-all-time/'


MovieList = []
BechdelList = []

PageImdb = requests.get(ImdbSite)
ImdbSoup = BeautifulSoup(PageImdb.content, 'html.parser')

ImdbMovie = ImdbSoup.find_all('a', class_ = 'title')


for Im in ImdbMovie:
    raw_title = Im.get_text(strip = True)
    clean_title = re.sub(r'^\d+\.\s*', '', raw_title)
    MovieList.append(clean_title)


## ŠĪ DAĻA STRĀDĀ

url = 'https://bechdeltest.com/?list=all'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

Bechdel = soup.find_all('div', class_='movie')

Titles = soup.find_all(id=re.compile('movie-'))


for ti in Bechdel:
    ti_tag = ti.find(id = re.compile('movie-'))
    img = ti.find('img')
    rating = img['alt'] if img else 'N/A'

    if ti_tag and rating == '[[3]]':
        # print(f"{ti_tag.text.strip()} rating: {rating}")
        

        for i in MovieList:
            # print(i, ti_tag.text.strip())
            if ti_tag.text.strip() == i:
                BechdelList.append(ti_tag.text.strip())
                break


## Filmu saraksts ar daudzumu
print(BechdelList, len(BechdelList))

