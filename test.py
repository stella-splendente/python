#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup
import urllib
import urllib2
import time
import string
import sys
import os
import pygame

def dc():
	url='http://gall.dcinside.com/board/lists/?id=bitcoins'
	req = requests.get(url)
	html = urllib.urlopen(url)
	soup = BeautifulSoup(html, "lxml")

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

	link = soup.find_all("td", { "class" : "t_subject"})
	status = req.status_code

	r = requests.get(url, headers=headers)
	#is_ok = req.ok

	print "====비트코인 갤러리(디시인사이드)크롤링해서 돈벌자====="
	print "ㅣ                  서버 상태 : ", status,"                 ㅣ"
	print "ㅣ[+] : 2XX_정상, 4XX_Client_Error, 5XX_Server_Error  ㅣ"
	print "ㅣ  http://gall.dcinside.com/board/lists/?id=bitcoins ㅣ"
	print "======================================================="

	html = r.text

	soup = BeautifulSoup(html,"lxml")
	link = soup.find_all("td",{ "class" : "t_subject" })
	for m in link:
		if(m.find("a", {"class":"icon_pic_n"})):
			post_num = m.parent.find("td", {"class" : "t_notice"}).string
        	#post_title = m.a.string
        #print "글제목 = ", post_title
		#post_title=m.a.string
		#print "\n"+"post_title = " + post_title
		#print (m.a.string)
		if(m.find("a", {"class":"icon_notice"})):
			pass
		else :
			print "[+]"+(m.a.string)

def clear():
	os.system("clear")


if __name__ == "__main__":
	while True :
		dc()
		time.sleep(2)
		clear()
		

