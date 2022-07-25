import requests
from bs4 import BeautifulSoup
import csv

info=[]

status=0

for i in range(1,8):
	url="https://www.indiastudychannel.com/schools/search.aspx?city=pune&stateid=24&PageNumber="+str(i)
	req=requests.get(url)

	pasta = BeautifulSoup(req.content,features="html.parser")
	listsi=pasta.find_all("p",class_="top-school-name-txt")
	for lists in listsi:
		suburl=lists.find('a')['href']
		suburl="https://www.indiastudychannel.com"+suburl
		req2=requests.get(suburl)
		chai=BeautifulSoup(req2.content,features="html.parser")
		
		schoolname=chai.find('span',{"id" : "ContentPlaceHolder1_lblSchoolName"}).text
		schooladd=chai.find('span',{"id" : "ContentPlaceHolder1_lblAddress"}).text
		schoolph=chai.find('span',{"id" : "ContentPlaceHolder1_lblPhoneNumber1"}).text
		schoolmail=chai.find('span',{"id" : "ContentPlaceHolder1_lblEmail"}).text
		schoolwebsite=chai.find('span',{"id" : "ContentPlaceHolder1_lblHomePage"}).text
		schoolboard=chai.find('span',{"id" : "ContentPlaceHolder1_lblUniversity"}).text
		
		info.append([schoolname,schooladd,schoolph,schoolmail,schoolwebsite,schoolboard])
		
		status=status+1
		print(status)
		
		
Details=["School Name" , "Address" , "Phone number" , "Mail" , "Website" , "Board"]

with open('schools_indiastudy_final.csv', 'w') as f: 
	write = csv.writer(f)
	write.writerow(Details)
	write.writerows(info)

		
