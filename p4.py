import requests
page = requests.get("http://www.qhce.gov.cn/student/student!index.action?sly=shouye")
page.encoding = 'UTF-8'
print(page.url)
print(page.status_code)
print(page.headers)
print(page.text)
