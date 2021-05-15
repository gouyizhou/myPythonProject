# !/usr/bin/env python
# -*-coding:utf-8-*-
# date :2021/4/16 12:57
# author:Sabo
import os
import requests
from bs4 import BeautifulSoup

savePath = 'F:/麻辣烫耙耳朵'
root = 'http://show.sctv.com/mlt/index'
urlTail = '.shtml'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'Connection': 'close'
    }

def getRootUrls(printFlag):
    originUrl = ''
    rootUrls = []
    for i in range(0, 10):
        if i is not 0:
            originUrl = root + '_' + i.__str__() + urlTail
        else:
            originUrl = root + urlTail
        rootUrls.append(originUrl)
    if printFlag is True:
     print(rootUrls)
    return rootUrls

def getLinksPerRootUrl(rootUrl, printFlag):
    # response = requests.get(url = rootUrl,  header = headers)
    response = requests.get(url = rootUrl)
    if response.status_code != 200:
        print('Get response error!')
        return ''
    else:
        response.encoding = 'utf-8'
        txt = response.text
        mainLink = BeautifulSoup(txt, 'html.parser')
        childLinks = []
        mainLink_txt = mainLink.find_all('div', attrs={"class": "txt"})
        for i in range(0, mainLink_txt.__len__()):
            link = mainLink_txt[i].find_next('a')
            href = link.get('href')
            childLinks.append(href)
        if printFlag == True:
            print(childLinks)
        return childLinks

def catUrl(catFlag, signalLinks):
    root = 'http://show.sctv.com/mlt'
    result = []
    for index in range(0, signalLinks.__len__()):
        if catFlag == 0:
            result.append(root+signalLinks[index][1:])
        else:
            result.append(root + catFlag.__str__() + signalLinks[index][1:])
    return result

def urlTitles(rootUrl):
    titles = []
    # response = requests.get(url=rootUrl, header = headers)
    response = requests.get(url=rootUrl)

    if response.status_code != 200:
        print('Get titles error!')
        return ''
    response.encoding ='utf-8'
    txt = response.text
    mainPage = BeautifulSoup(txt, 'html.parser')
    nameLinks = mainPage.find_all('div', attrs={'class':'name'})
    for index in range(0, nameLinks.__len__()):
        titles.append(nameLinks[index].text)
    return titles

def download(savePath, titles, links):
    for index in range(0, titles.__len__()):
        commond = 'you-get -o {0} -O {1} "{2}"'.format(savePath, titles[index], links[index])
        print(commond)
        os.system(commond)

def main():
    RootUrls = getRootUrls(printFlag = False)
    catFlag = 0
    for RootUrl in RootUrls:
        links = getLinksPerRootUrl(rootUrl=RootUrl, printFlag=False)
        titles = urlTitles(rootUrl=RootUrl)
        dstUrls = catUrl(catFlag = catFlag, signalLinks=links)
        download(savePath=savePath, titles=titles, links=dstUrls)
        # catFlag+=1

if __name__ == '__main__':
    main()