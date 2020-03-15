import csv
import requests
import time
from lxml import etree


def get_html(url, data=None):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0;\
rv:11.0) like Gecko'}
    try:
        rep = requests.get(url, headers=header, timeout=10)
        rep.raise_for_status()  #如果响应状态不是200，引发HTTPError异常
        rep.encoding = rep.apparent_encoding  #从内容分析出的响应内容编码方式
        return rep.text
    except:
        return None


def get_item(html):
    data = etree.HTML(html)
    date_list = data.xpath('//tr[1]/td[@width="155"]/text()')   #取得开标日期
    name_list = data.xpath('//tr[1]/td[@width="295"]/text()')   #取得项目名称
    address_list =data.xpath('//tr[2]/td[@width="295"]/text()') #取得开标地址
    item=[]
    for date, name, address in zip(date_list, name_list, address_list):
        item.append([date, name, address])
    return item


def write_item(data, file_name):
    with open(file_name, 'w', errors='ignore', encoding='utf-8-sig', newline=''
) as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)


if __name__ == '__main__':
    url = 'http://www.ccgp-qinghai.gov.cn/html/jrkb/jrkb_more.html'
    html = get_html(url)
    if html is not None:
        item = get_item(html)
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 取得当前日期
        write_item(item, 'item' + date + '.csv')  # 写入CSV文件
    else:
        print("网站错误！")