# !/usr/bin/env python
# -*-coding:utf-8-*-
# date :2021/3/2 14:10
# author:Sabo
import requests
import re
regex_title = 'title=.*"'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

def get_title(url):
    response = requests.get(url=url, headers=headers, verify=False)
    # 爬取成功
    if response.status_code == 200:
        response.encoding = 'utf-8'
        # print(response)
        text = response.text
        print(text)
        title_List = re.compile(regex_title).findall(text)
        len = title_List.__len__()
        i = 0
        while i < len:
            # 单个标题的长度
            len_title = title_List[i].__len__()
            # 正则表达式开头的长度
            len_begin = "title=.*".__len__()
            # 下标从0 开始，-1才是目的字符串的首个下标
            title_Signal = title_List[i][len_begin-1:len_title-1]
            print(title_Signal)
            f.write(title_Signal)
            f.write('\r\n')
            i += 1
    else:
        print("爬取出错！")


if __name__ == '__main__':
    f = open('title.txt', 'a')
    url = "http://show.sctv.com/mlt/index_1.shtml"
    # 翻页操作
    try:
        i = 1
        htmlIndex = 2
        while htmlIndex < 10:
            print('*'*20+"第",i,'页','*'*20)
            get_title(url)
            htmlIndex = i + 1
            # 替换网址
            url = url.replace(i.__str__(),htmlIndex.__str__())
            # 每次i加1翻页
            i += 1
        f.close()
    except:
        print("Error！")

    finally:
        print('End!', "*" * 42)