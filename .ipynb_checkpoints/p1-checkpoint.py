import requests
from bs4 import BeautifulSoup

res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.select('.news-item'))

for news in soup.select('.news-item'):
    if len(news.select('h2')) > 0:
        h = news.select('h2')[0].text
        date = news.select('.time')[0].text
        a = news.select('a')[0]['href']
        print(date, h, a)
