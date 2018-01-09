import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.qhu.edu.cn')
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')

soup = soup.select('.articleList_rt01a')


for news in soup:
    if len(news.select('.Date')) > 0:
        h = news.select('li')[0].text
        date = news.select('.Date')[0].text
        a = news.select('a')[0]['href']
        print(date, h, a)
