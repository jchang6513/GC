import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

board = 'DC_SALE'
pages = 2
dates = pd.date_range(start='20180810',end='20180812')
pttUrl = 'https://www.ptt.cc'
boardUrl = pttUrl+'/bbs/'+board+'/index.html'

if os.path.isdir(board) == False:
	os.makedirs(board)

Mdate = dates.max()

while Mdate > dates.min():
	r = requests.get(boardUrl)
	r.encoding = 'utf-8'
	soup = BeautifulSoup(r.text, 'html.parser')
	pUrl = soup.find("div",{"id":"action-bar-container"}).find("div",{"class":"btn-group btn-group-paging"}).find_next().find_next().get("href")
	boardUrl = pttUrl+pUrl
	rents = soup.find_all("div",{"class":"r-ent"})
	top = 1
	for rent in rents:	
		try:			
			titleUrl = pttUrl+rent.find("div",{"class":"title"}).find("a").get("href")
			r = requests.get(titleUrl)
			r.encoding = 'utf-8'
			soup = BeautifulSoup(r.text, 'html.parser')
			main = soup.find("div",{"id":"main-content"})
			author = main.find_next("div",{"class":"article-metaline"}).find("span",{"class":"article-meta-value"}).string
			title  = main.find_next("div",{"class":"article-metaline"}).find_next("div",{"class":"article-metaline"}).find("span",{"class":"article-meta-value"}).string
			date   = pd.to_datetime(main.find_next("div",{"class":"article-metaline"}).find_next("div",{"class":"article-metaline"}).find_next("div",{"class":"article-metaline"}).find("span",{"class":"article-meta-value"}).string)			
			content = main.get_text()
#			print(author,title,date)	
			if top == 1:
				Mdate = pd.to_datetime(date.strftime('%Y%m%d'))
				top = 0
			if pd.to_datetime(date.strftime('%Y%m%d')) > Mdate:
				Mdate = pd.to_datetime(date.strftime('%Y%m%d'))
			print(date,Mdate,dates.min(),dates.max())
			if date > dates.min() and pd.to_datetime(date.strftime('%Y%m%d')) <= dates.max():
				if os.path.isdir(os.path.join(board,date.strftime('%Y%m%d'))) == False:
					os.makedirs(os.path.join(board,date.strftime('%Y%m%d')))
				text_file = open(os.path.join(board,date.strftime('%Y%m%d'),titleUrl[31:-5]+'.txt'), "w")
				text_file.write(author+'\n')
				text_file.write(title+'\n')
				text_file.write(date.strftime('%c')+'\n\n')
				text_file.write(content)			
				text_file.close()
		except:
			print('0.0')