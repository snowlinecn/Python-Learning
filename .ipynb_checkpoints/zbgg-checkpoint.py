import requests
import re
from lxml import etree

class ZbSpider(object):
    def __init__(self):
        self.url = "http://www.ccgp-qinghai.gov.cn/jilin/zbxxController.form?"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) \
Gecko/20100101 Firefox/63.0"}
        self.page = 0
        
    def start_request(self):
        lx = input("请输入公告类型（1.省级 2.州市县级）：")
        pg = input("请输入爬取页数：")
        for self.page in range(int(pg)):
            page = self.page + 1
            print("正在爬取中标公告第【%d】页...-----------------------------" % page)
            html = requests.get(self.url+"declarationType=W"+"&type="+lx+"&pageNo="+
str(self.page), headers=self.headers).content.decode()
            self.zbxx(html)
        '''
        # 废流标公告信息
        self.page = 0
        for self.page in range(int(pg)):
            print("正在爬取废流标公告第【%d】页...---------------------------" % self.page)
            html = requests.get(self.url+"declarationType=F"+"&type="+lx+"&pageNo="+
str(self.page), headers=self.headers).content.decode()
            self.zbxx(html)
        '''
    
    #中标公告信息获取
    def zbxx(self, html):
        #stitle = re.findall(r'title="(.*?)"', html)    #公告标题
        surl = re.findall(r'" href="(.*?)">', html)
        for su in surl:
            #实际公告页面在框架内，去除框架页多余字符，合成实际url
            sggurl = su.replace('ftl/jilin/noticeDetail.jsp?htmlURL=','')
            print(sggurl)
            sgg = requests.get(sggurl, headers=self.headers).content
            s = etree.HTML(sgg)
            name = s.xpath('/html/body/div/table/tbody/tr[2]/td[2]/p/span/text()')
            date = s.xpath('/html/body/div/table/tbody/tr[8]/td[2]/p/span/text()')
            man = s.xpath('/html/body/div/table/tbody/tr[13]/td[2]/p/span/text()')
            print('【'+date[0]+'】',name[0],'【'+man[0]+'】')
    
if __name__ == "__main__":
    zb = ZbSpider()
    zb.start_request()