#You must have bs4 and requests installed; else perform: pip3 install bs4 and pip3 install requests
from bs4 import BeautifulSoup
import requests
import smtplib
import time


URL = "https://www.amazon.in/Test-Exclusive-633/dp/B07HGH82LT/ref=lp_17033333031_1_3?s=electronics&ie=UTF8&qid=1573365313&sr=1-3"#Change link for new product; amazon.in seems to be a little inconsistent when it comes to tags- so asking the user to input URL can have unforeseen consequences. 

"""

For everyone who has problems using amazon.com: .com makes the html code with javascript. You can trick them with using 2 soups. Load soup1 like in the code below. Then load soup2 with soup1.prettify(). Then you have got soup2 loaded correctly and you can run the code without any further hassles.

soup1 = BeautifulSoup(page.content, "html5lib")

soup2 = BeautifulSoup(soup1.prettify(), "html5lib")

title = soup2.find(id= "productTitle")

"""


header = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/78.0.3904.70 Chrome/78.0.3904.70 Safari/537.36'#Could be different, a simple google search would suffice.
}
def check_price(budget):
    page=requests.get(URL,headers=header)

    soup= BeautifulSoup(page.content,'html5lib')#You may change parser as per your interests(e.g speed, etc.)

    title = soup.find(id="productTitle").get_text()#Check your amazon site for the tag which displays Product Name

    price = soup.find(id="priceblock_ourprice").get_text()#Check your amazon site for the tag which dispays Product Price
    new_price =(price[2:-3])
    l=[]
    for i in new_price:
        if(i!='.' and i!=','):
            l.append(int(i))
    string=''
    for i in l:
        string+=str(i)
    final_price=int(string)

    if final_price<budget:
        send_mail()
    else:
        print(title,"is over your budget of",str(budget))
        print('We will send you an e-mail if the price drops, in 86400 seconds')#You may change the time Duration as per your wish


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)#Change both parameters if Outlook/Yahoo is used
    server.ehlo()
    server.starttls()
    server.ehlo()
    #server.login('***ENTER E-MAIL ID***','***ENTER PASSWORD***') - Please enter details(2-step verification/OTP is preferred) and then remove # at the start of this line.
 
    subject = 'Price is Below '+str(budget)#Change these as per your mailing patterns.
    body = 'Check the amazon link!https://www.amazon.in/Test-Exclusive-633/dp/B07HGH82LT/ref=lp_17033333031_1_3?s=electronics&ie=UTF8&qid=1573365313&sr=1-3'#Change the link as per your 'URL'

    msg = "Subject:"+str(subject)+"\n\n"+str(body)
    server.sendmail(
        #'***SENDER'S E-MAIL ID***' - Please enter details and remove # at the start of this line.(PLEASE DO NOT REMOVE THE COMMA AT THE END OF THE LINE),
        #'***RECEIVER'S E-MAIL ID***'- Please enter details and remove # at the startof this line.(PLEASE DO NOT REMOVE THE COMMA AT THE END OF THE LINE),
        msg
    )
    print("E-mail has been sent.")

    server.quit()#DO NOT OMIT THIS LINE.

 
budget=int(input("Enter your budget(in INR):    "))#You may put a default argument, if you wish, in check_price([int]); you may also change currency into your corresponding country's currency.

while(True):
    check_price(budget)
    time.sleep(86400)#Change time as per your wish; NOT TOO LOW- we don't want to bombard Amazon's servers.


