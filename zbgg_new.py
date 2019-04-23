#查询中标公告

import requests
import re
import json
import html

class ZbSpider(object):
    
    url = "http://www.ccgp-qinghai.gov.cn/es-articles/es-article/_search"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) \
Gecko/20100101 Firefox/63.0", "Content-Type": "application/json"}
    # Payload查询参数json
    payloadData = {
        "from": 0,
        "size": 1,
        "query": {
            "bool": {
                "must": [
                    {
                        "term": {
                            "siteId": {
                                "value": "38",
                                "boost": 1
                            }
                        }
                    },
                    {
                        "wildcard": {
                            "path": {
                                "wildcard": "*6zcyannouncement46*",
                                "boost": 1
                            }
                        }
                    }
                ],
                "adjust_pure_negative": True,
                "boost": 1,
                "should": []
            }
        },
        "sort": [
            {
                "publishDate": {
                    "order": "desc"
                }
            },
            {
                "_id": {
                    "order": "desc"
                }
            }
        ],
        "_source": {
            "includes": [
                "title",
                "articleId",
                "siteId",
                "cover",
                "url",
                "pathName",
                "publishDate",
                "attachmentUrl",
                "districtName",
                "gpCatalogName"
            ],
            "excludes": [
                "content"
            ]
        }
    }        
    zbgg_addrs = []
    
    def __init__(self, dfrom, dsize):
        self.payloadData['from'] = dfrom # 中标公告列表起始位置
        self.payloadData['size'] = dsize # 总数
 
    # 获取中标公告列表   
    def zbgg_list(self): 
        html = requests.post(self.url, data=json.dumps(self.payloadData), headers=self.headers)
        d = json.loads(html.content.decode())
        size = self.payloadData['size']
        for i in range(size):
            self.zbgg_addrs.append("http://www.ccgp-qinghai.gov.cn"+d[ 'hits']['hits'][i]['_source']['url']) # 获取中标公告页面地址
            # d[ 'hits']['hits'][i]['_source']['title'] 中标公告标题，
            # d[ 'hits']['hits'][i]['_source']['url'] 中标公告页面路径

    # 打印中标公告信息    
    def zbgg_print(self): 
        for zbgg_adddr in self.zbgg_addrs:
            html_text = requests.get(zbgg_adddr, headers=header, timeout=10).content.decode()
            html_text = html.unescape(html_text)
            phzj = []
            pbzj = re.findall(r'code-85005\\">(.*?)<', html_text) # 匹配评审专家名单
            if pbzj == [] :
                pbzj = re.findall(r'名单：(.*?)十', html_text) # 匹配不规范页面中的评审专家名单
                pattern = re.compile(u"[\u4e00-\u9fa5、（）]") # 提取专家名单，保留汉字和"、（）"等符号，去除多余字符
                pbzj[0] = "".join(pattern.findall(pbzj[0])) # 连接成专家名单字符串
            cjrq = re.findall(r'code-94002\\">(.*?)<', html_text) # 匹配成交日期
            xmmc = re.findall(r'code-00003\\">(.*?)<', html_text) # 匹配项目名称
            xmbh = re.findall(r'code-00004\\">(.*?)<', html_text) # 匹配项目编号
            print(cjrq[0], ",", xmbh[0], ",", xmmc[0], ",", pbzj[0])
    
if __name__ == "__main__":
    zb = ZbSpider(0,50)
    zb.zbgg_list()
    zb.zbgg_print()