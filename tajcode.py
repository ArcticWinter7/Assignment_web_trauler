import requests
from bs4 import BeautifulSoup
 
tag = "health-fitness"
 
#This finds the total page numbers
def findpagecount():
    page_html = requests.get("https://www.nzdirectory.co.nz/health-fitness.html")
    Soup = BeautifulSoup(page_html.text, 'html.parser')
    NzDirecotryPageNum = Soup.find_all('div', id="page_cat")
 
    for Pagelist in NzDirecotryPageNum:
        Pagedetails = Pagelist.find_all('div', class_ ="pages")
        pagecount = len(Pagedetails)
        NzDirecotryListNum = pagecount
        #print("number of pages = " + str(pagecount))
        #findpagecount.append(Pagedetails)
    return NzDirecotryListNum

 
def NzDirecotry(tag, Pagenumber):
    
    url = f"https://www.nzdirectory.co.nz/{tag}{Pagenumber}.html"
    page_html = requests.get(url)
    Soup = BeautifulSoup(page_html.text, 'html.parser')
    NzDirecotryPage = Soup.find_all('div', class_ ="listing_content")
    NzDirecotryList = []
 
    for Prodcuts in NzDirecotryPage:
        details = Prodcuts.find('p', class_="address")
        #The try is so make is so that 
        try:
            if details is not None:
                print(details.text)
        except:
            pass 
    return NzDirecotryList


Pagenumber = findpagecount()


 
for x in range(0, (Pagenumber)):
    y = ("-" + str(x))
    rfregregf = NzDirecotry(tag, y)
 

'''
def NzDirecotryData(url):
    PageRequest= requests.get(url)
    Soup = BeautifulSoup(PageRequest.text, 'html.parser')
    return Soup
 
def NzDirecotryParse(Soup):
    P1 = []
    results = Soup.find_all('ul', id_="directory_listings")
    for Prodcuts in results:
 
        CompanyName = Prodcuts.find('div', id_="profile_title").text
        Address = Prodcuts.find('p', class_="address").text
        PhoneNumber = int(Prodcuts.find_all('div', class_="").text) 
        P1.append([CompanyName, Address, PhoneNumber])
        print(str(CompanyName) + str(Address) + int(PhoneNumber))
    return P1
    '''