import os
import re
import requests

word = input("请输入要搜索的图片：")
if not os.path.exists('c:/Temp/' + word):
    os.mkdir('c:/Temp/' + word)

url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592\
&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1540822430688_R&pv=&ic=0&nc=1&z=&se=1\
&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=" + word

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) \
Gecko/20100101 Firefox/63.0"}

r = requests.get(url, headers=header, timeout=3)
r.encoding = "utf-8"
r = r.text

img_list = re.findall('"objURL":"(.*?)",', r)
# print(img_list)

for img in img_list:
    print(img)
    end = re.search('(.jpg|.png|.gif|.jpeg)$', img)
    if end == None:
        img = img +'.jpg'

    path = re.sub('\?|\/', '', img[-10:])

    try:
        with open('c:/Temp/' + word +'/{}'.format(path), 'ab') as f:
            ret = requests.get(img, headers=header, timeout=3)
            f.write(ret.content)
    except Exception:
        pass
