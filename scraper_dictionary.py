import requests
from bs4 import BeautifulSoup
import csv

url="https://www.punediary.com/html/pmc_schools.htm"
req=requests.get(url)

pasta = BeautifulSoup(req.content,features="html.parser")
listsi=pasta.find_all("tr",valign="TOP")
print(len(listsi))

school_name=pasta.find_all("td",height=13)
info=[]
i=0
noph=0
while i < (len(school_name)):
	name=school_name[i].text[1:]
	addph=school_name[i+1].text[1:]
	a=addph.find("PHONE :")
	flag=0
	if a==-1:
		flag=1
		a = addph.find("PH :")
	if (a!=-1):
		if flag==0:
			ph=addph[a+8:]
			addph=addph[:(a-1)]
			info.append([name,addph,ph])
		else:
			ph=addph[a+5:]
			addph=addph[:(a-1)]
			info.append([name,addph,ph])
	else:
		ph=-1
		noph=noph+1
		info.append([name,addph,ph])
	
	i+=2

Details=["School Name" , "Address" , "Phone number"]
with open('student.csv', 'w') as f: 
	write = csv.writer(f) 
	write.writerow(Details) 
	write.writerows(info) 


print(noph)

