# !/usr/bin/env python
# -*-coding:utf-8-*-
# date :2021/4/8 19:17
# author:Sabo
import requests
from bs4 import BeautifulSoup
import os

rootUrl = 'http://show.sctv.com/mlt/index.shtml'
urlTail = '.shtml'
savePath = 'F:/麻辣烫耙耳朵'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'Connection': 'close'
    }

# rootWeb ->
def getTitles(origin):
    signalTags=[]
    result = []
    response = requests.get(origin)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        txt = response.text
        mainPage = BeautifulSoup(txt,'html.parser')
        signalTags = mainPage.find_all('div',attrs={'class':'item-cell'})
        for tag in signalTags:
            ans = tag.find('div',attrs={'class':'name'}).text
            result.append(ans)
    else:
        print('Get title error!')
    return result

def getLinks(origin):
    result = []
    response = requests.get(origin)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        txt = response.text
        linkPage = BeautifulSoup(txt,'html.parser')
        linkTxt = linkPage.find_all('div', attrs={"class": "txt"})
        lenOfTxt = linkTxt.__len__()
        for i in range(0, lenOfTxt):
            link = linkTxt[i].find_all('a')
            href = link[0].get('href')
            result.append(href)
            # print(href)
    else:
        print("Get links error!")

    return result

def catUrl(rootUrl, childUrl):
    return rootUrl.replace('index.shtml',childUrl)

def getSiganlTitle(url):
    response = requests.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        txt = response.text
        mainPage = BeautifulSoup(txt, 'html.parser')
        signalTag = mainPage.find_all('div', attrs={'class': 'videoTitle container turn-off'})
        tagtext = signalTag[0].text
        vedioName = tagtext.strip()
        return vedioName

    else:
        print('Get signal title error!')

def download(savePath, vedioName, vedioUrl):
    commond = 'you-get -o {0} -O {1} "{2}"'.format(savePath, vedioName, vedioUrl)
    print(commond)
    os.system(commond)

def downloadHomePage():
    # get homePage vedios
    origin = 'http://show.sctv.com/mlt/index.shtml'
    titles = getTitles(origin)
    # 获取标题并用做视频的名字
    # print(titles)
    if len(titles) >= 1:
        for title in titles:
            print(title)
    else:
        print("No tags in list!")

    # Get this page links~
    vedioLink = getLinks(origin)
    # endUrls = []
    for i in range(0, vedioLink.__len__()):
        signalLink = vedioLink[i]
        lenOfSignalLink = signalLink.__len__()
        url = catUrl(rootUrl=rootUrl, childUrl=signalLink[2:lenOfSignalLink])
        print(url)
        vedioUrl = url
        vedioName = getSiganlTitle(url)
        # vedioName = vedioStr.strip()
        print(vedioName)
        download(savePath, vedioName, vedioUrl)

def downloadOthers(url):
    origin = url
    for i in range(1, 6):
        print('i={}'.format(i))
        a = 1
        if i >= 1:

            print('a={}'.format(a))
            origin = url.replace(a.__str__(),i.__str__())
        i = i + 1
        print('origin:{}'.format(origin))
        titles = getTitles(origin)
        # 获取标题并用做视频的名字
        # print(titles)
        if len(titles) >= 1:
            for title in titles:
                print(title)
        else:
            print("No tags in list!")

        # Get this page links~
        vedioLink = getLinks(origin)
        # endUrls = []
        for i in range(0, vedioLink.__len__()):
            signalLink = vedioLink[i]
            lenOfSignalLink = signalLink.__len__()
            url = catUrl(rootUrl=rootUrl, childUrl=signalLink[2:lenOfSignalLink])
            print(url)
            vedioUrl = url
            vedioName = getSiganlTitle(url)
            # vedioName = vedioStr.strip()
            print(vedioName)
            download(savePath, vedioName, vedioUrl)

def main():
    # origin = 'http://show.sctv.com/mlt/index_1.shtml'
    # downloadHomePage()
    # downloadOthers(origin)
    root = 'http://show.sctv.com/mlt/index'
    urlTail = '.shtml'
    originUrl = ''
    rootUrls = []
    for i in range(0, 10):
        if i is not 0:
            originUrl = root+'_'+i.__str__()+urlTail
        else:
            originUrl = root + urlTail
        rootUrls.append(originUrl)
    print(rootUrls)

if __name__ == '__main__':
    main()