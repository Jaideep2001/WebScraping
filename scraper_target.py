import requests
from bs4 import BeautifulSoup
import csv


def extract_source(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    source=requests.get(url, headers=headers).text
    return source

def extract_data(source):
     soup=BeautifulSoup(source,features="html.parser")
     names=soup.find_all('div',{'class' : 'card-body'})
     return names

extract_data(extract_source('https://targetstudy.com/school/schools-in-pune.html?recNo=25'))

data=[]

status=0

for i in range(0,1405,25):
	listi=extract_data(extract_source('https://targetstudy.com/school/schools-in-pune.html?recNo='+str(i)))
	print(i)
	if i!=1400:
		listi=listi[:25]
	else:
		listi=listi[:12]
	
	for ele in listi:
		title=ele.find("a").text
		info=ele.find("p",{"class" : "card-subtitle mt-0"}).text
		info=info[13:]
		
		phoneindex = info.find("phone")
		iphoneindex=info.find("phone_iphone")
		
		if iphoneindex != -1:
			phnum=info[iphoneindex+12:]
		else:
			if phoneindex != -1:
				phnum=info[phoneindex+5:]
				
			else:
				phnum=-1
		try:
			phnum=phnum.strip()
		except:
			phnum=phnum
		addr=info[:phoneindex]
		types=ele.find_all("li")
		schooldet=""
		for t in types:
			schooldet=schooldet+t.text+" "
		data.append([title,addr,phnum,schooldet])
	
		


Details=["School Name" , "Address" , "Phone number" , "Details" ]

with open('schools_targetstudy.csv', 'w') as f: 
	write = csv.writer(f)
	write.writerow(Details)
	write.writerows(data)
