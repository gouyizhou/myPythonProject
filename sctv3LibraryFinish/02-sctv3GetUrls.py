# !/usr/bin/env python
# -*-coding:utf-8-*-
# date :2021/4/8 16:40
# author:Sabo
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

def getTitle(title):
    title = title.__str__()
    title = title.strip()
    indexBegin = title.find('>')
    lastBegin = title.find('<', indexBegin)
    title = title.__str__()
    ans = title[indexBegin + 1: lastBegin]
    ans = ans.strip()
    # print(ans)
    title = ans
    return title


def getUrls(origin):
    dstLinks = []
    response = requests.get(url=origin)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        txt = response.text
        mainpage = BeautifulSoup(txt, 'html.parser')
        urlLinks = mainpage.find_all('div', attrs={"class": "item-cell"})
        lenOfLinks = urlLinks.__len__()
        i = 0
        for i in range(0, lenOfLinks):
            aTag = urlLinks[i].find_all('a')
            url = aTag[0].get('href')
            # print(aTag[0].get('href'))
            ans = origin.replace('index.shtml', url)
            dstLinks.append(ans)
            # print(ans)
    else:
        print('Error!')
    return dstLinks

def getTitleTwo(web):
    # link = urlLinks[i].find('div',attrs={'class':'txt'}).find_next('a').text
    # link = link.__str__()
    # print(link.strip())
    # indexOfEnd = link.find('）')
    # print(indexOfEnd)
    # print(link[0:indexOfEnd+1])
    # print(len(link))
    pass

def get_title(url):
    response = requests.get(url=url, headers=headers, verify=False)

if __name__ == '__main__':
    origin = 'http://show.sctv.com/mlt/index.shtml'
    Links = getUrls(origin)
    for i in Links:
        print(i)


