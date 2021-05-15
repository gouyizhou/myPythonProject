import requests
import re

def parse_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        result = response.text
        print(result)
    else:
        print("地址解析出错")


url = "https://blog.csdn.net/CSDNsabo/article/details/104778542"
parse_url(url)