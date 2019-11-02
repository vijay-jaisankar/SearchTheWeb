import bs4
import requests


#This program takes in an absolute URL from the user, and prints the code of that webpage in 'file.txt' , which the user can review.

site=str(input("Enter the ABSOLUTE url:  "))
req=requests.get(site)
obj=bs4.BeautifulSoup(req.content,'html5lib')

file1=open('file.txt','w')
file1.write(obj.prettify())
file1.close()

