# !/usr/bin/env python
# -*-coding:utf-8-*-
# date :2021/5/2 19:08
# author:Sabo
# !/usr/bin/env python
# -*-coding:utf-8-*-
# date :2021/5/2 17:19
# author:Sabo
import requests
from bs4 import BeautifulSoup
import os

savePath = r'F:\麻辣烫耙耳朵'

# 通过首页获取每个视频的Url
# 通过单个视频的Url利用you-get进行下载相应的视频

# 网站头加上各个分视频的网址即可得到单个视频的网址，从而即可利用you-get进行下载
signalUrlHead = 'http://show.sctv.com/mlt/'
homePageUrl = 'http://show.sctv.com/mlt/index.shtml'

# 通过首页网址，在首页中提取相关的网址
def getUrls(homePageUrl):
    results = []
    response = requests.get(url = homePageUrl)
    if response.status_code != 200:
        print('Get urls error!')
        return []
    else:
        print('Get urls successfully!')
        response.encoding = 'utf-8'
        txt = response.text
        homePage = BeautifulSoup(txt, 'html.parser')
        childUrls = homePage.find_all('div', attrs={"class":"txt"})
        for index in range(0, childUrls.__len__()):
            link = childUrls[index].find('a').get('href')
            results.append(link)
        return results

# 通过根路径和分路径拼接成完整路径
def catUrl(signalHead, signalLinks):
    results = []
    for index in range(0, signalLinks.__len__()):
        results.append(signalUrlHead+signalLinks[index])
    return results

# 利用os模块调用cmd利用you-get指令下载视频
def download(savePath, vedioName, vedioUrl):
    commond = 'you-get -o {0} -O {1} "{2}"'.format(savePath, vedioName, vedioUrl)
    print(commond)
    os.system(commond)


def getTitles(homePage):
    titles = []
    response = requests.get(url = homePage)
    if response.status_code != 200:
        print('Get titles error!')
        return []
    else:
        print("Get titles successfully!")
        response.encoding = 'utf-8'
        txt = response.text
        mainPage = BeautifulSoup(txt, 'html.parser')
        childTitles = mainPage.find_all('div', attrs={'class':'name'})
        for index in range(0, childTitles.__len__()):
            titles.append(childTitles[index].text.replace(' ', '-') )
        return titles


# 根据域名格式合成所有的域名
# 首页  http://show.sctv.com/mlt/index.shtml
# 第二页 http://show.sctv.com/mlt/index_1.shtml
# 第三页 http://show.sctv.com/mlt/index_2.shtml
# 格式为 http://show.sctv.com/mlt/index_x.shtml

def getAllHomePage(homePageUrl):
    catFlag = 1
    resultHomePageUrl = []
    resultHomePageUrl.append(homePageUrl)
    while(catFlag < 10):
        resultHomePageUrl.append(homePageUrl.replace('.shtml', '_'+catFlag.__str__()+'.shtml'))
        catFlag+=1
    return resultHomePageUrl

if __name__ == '__main__':
    homePages = getAllHomePage(homePageUrl  = homePageUrl)
    for index in range(0, homePages.__len__()):
        # 当前主页面的所有视频标题
        titles = getTitles(homePage=homePages[index])
        # 当前页面下的所有视频独立路径
        signalLinks = getUrls(homePageUrl=homePages[index])
        # 独立路径和主路径完成拼接，得到完整的视频路径
        completeUrls = catUrl(signalHead = signalUrlHead, signalLinks = signalLinks)
        # 批量下载
        for indexDownLoad in range(0, completeUrls.__len__()):
            download(savePath=savePath, vedioName=titles[indexDownLoad], vedioUrl=completeUrls[indexDownLoad])

