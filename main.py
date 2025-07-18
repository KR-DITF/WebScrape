import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import re
import time

# ImdbSite = "https://www.imdb.com/chart/top/"

# MovieList = []


# driver = webdriver.Firefox()
# driver.get(ImdbSite)
# time.sleep(2)


# for i in range(0,250):
#     MovieTitles = driver.find_element(By.CLASS_NAME, "ipc-title__text ipc-title__text--reduced")
#     MovieList.append(MovieTitles)

# driver.quit()

# for i in MovieList:
#     print(i)

url = 'https://bechdeltest.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
if (Bechdel = soup.find_all(alt="[[3]]")):
    Titles = soup.find_all(id=re.compile('movie-'))


for ti in Titles:
    print(ti.get_text())