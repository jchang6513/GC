import os
import urllib.request
import pandas as pd
from html.parser import HTMLParser
from bs4 import BeautifulSoup

board = 'DC_SALE'
pages = 2

pttUrl = 'https://www.ptt.cc/bbs/'+board+'/index.html'

if os.path.isdir(board) == False:
	os.makedirs(board)

for page in range(pages):
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}  
	req = urllib.request.Request(url=pttUrl, headers=headers)  
	html = urllib.request.urlopen(req).read()
#	response = urllib.request.urlopen(pttUrl)
#	html = response.read()

	soup = BeautifulSoup(html, 'html.parser')
	print(soup)
#	rents = soup.find_all(')
	for rent in rents:
			try:
					print(rent.find('title').string)
			except Exception as e:
					print(e)
