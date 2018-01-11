import requests
import csv
import time
from bs4 import BeautifulSoup


def get_content(url, data = None):

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0)'}

    rep = requests.get(url, headers = header)
    rep.encoding = 'utf-8'
    return rep.text


def get_data(html_text):
    final = [['序号', '开标时间', '项目名称', '开标地点', '采购单位']]
    bs = BeautifulSoup(html_text, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body  # 获取body部分
    data = body.find('div', {'class': 'list_r_con2'})  # 找到今日开标表格部分

    table = data.find_all('table')  # 获取所有开标数据
    i = 1
    for item in table:  # 对每个开标数据的内容进行遍
        temp = []
        kb = item.find_all('td')
        print(i, ',',  kb[3].string, ',', kb[1].string,
              ',', kb[5].string, ',', kb[7].string)

        temp.append(i)
        temp.append(kb[3].string)  # 添加到temp中
        temp.append(kb[1].string)
        temp.append(kb[5].string)
        temp.append(kb[7].string)

        final.append(temp)  # 将temp加到final中
        i = i + 1
    return final


def write_data(data, name):
    file_name = name
    with open(file_name, 'w', errors = 'ignore', encoding = 'utf-8-sig', newline = '') as f :
        f_csv = csv.writer(f)
        f_csv.writerows(data)


if __name__ == '__main__':
    url = 'http://www.ccgp-qinghai.gov.cn/html/jrkb/jrkb_more.html'
    html = get_content(url)
    result = get_data(html)
    kbdate = time.strftime('%Y-%m-%d', time.localtime(time.time())) # 取得当前日期
    write_data(result, 'kaibiao' + kbdate + '.csv') # 生成开标项目文档
