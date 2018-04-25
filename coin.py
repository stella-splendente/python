#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup
import urllib
import urllib2
import time
import string
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

global last_check
last_check = 0

def dc():
    url='http://gall.dcinside.com/board/lists/?id=bitcoins'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ko-KR,ko;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'gall.dcinside.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }

    r = requests.get(url, headers=headers)

    html = r.text
    soup = BeautifulSoup(html,"lxml")

    links = soup.find_all("tr",{ "class" : "tb" })

    lock = 0
    context = {}
    for link in links:
        if lock == 0:
            notice = link.find_all("td",{ "class" : "t_notice" })
            if notice[0].string.isdigit() == True:
                t_writer = link.find_all("td",{ "class" : "t_writer" })
                user_ip = link.find_all("span",{ "class" : "user_ip" })

                data_num = notice[0].string
                data_subject = link.a.string
                try:
                    data_writer = t_writer[0]['user_name'] + user_ip[0].string
                except BaseException:
                    data_writer = t_writer[0]['user_name'] + "(fix)"

                context['data_num'] = data_num
                context['data_subject'] = data_subject
                context['data_writer'] = data_writer
                lock += 1


    return context

def clear():
    os.system("clear")

if __name__ == "__main__":

    search_text = '가격' #검색할 단어

    context = dc()
    last_check = context['data_num']
    print context['data_num'] + ' / ' + context['data_subject'] + ' / ' + context['data_writer']

    while True:
        context = dc()
        if last_check < context['data_num']:
            last_check = context['data_num']

            if str(context['data_subject']).find(str(search_text)) != -1:
                print context['data_num'] + ' / ' + context['data_subject'] + ' / ' + context['data_writer'] + '<--------- 주의 집중'
            else:
                pass
               # print context['data_num'] + ' / ' + context['data_subject'] + ' / ' + context['data_writer']

        time.sleep(1)