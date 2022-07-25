import requests
from bs4 import BeautifulSoup

url="https://www.uniapply.com/schools/schools-in-pune/"
req=requests.get(url)

pasta = BeautifulSoup(req.content,features="html.parser")
listsi=pasta.find_all('section',class_="item-list")
print(len(listsi))


for lists in listsi:
	title = lists.find('div',class_="item-title").text
	classes = lists.find('span',class_="item-val font-weight-semibold").text
	fee = lists.find('span',class_="item-val font-weight-semibold").text
	board = lists.find('span',class_="item-val font-weight-semibold").text
	sf_ratio = lists.find('span',class_="item-val font-weight-semibold").text
	info=[title,classes,fee,board,sf_ratio]
	print(info)

