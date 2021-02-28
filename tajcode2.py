import requests
from bs4 import BeautifulSoup
 
tag = "health-fitness"
 
#This finds the total page numbers
def findpagecount(tag):
    page_html = requests.get(f"https://www.nzdirectory.co.nz/{tag}.html")
    Soup = BeautifulSoup(page_html.text, 'html.parser')
    NzDirecotryPageNum = Soup.find_all('div', id="page_cat")
    NzDirecotryListNum = []

    for Pagelist in NzDirecotryPageNum:
        Pagedetails = Pagelist.find_all('div', class_ ="pages")
        pagecount = len(Pagedetails)
        NzDirecotryListNum = pagecount
    return NzDirecotryListNum
 
Pagenumber = findpagecount(tag)

def NzDirecotry(tag, _Pagenumber):
    
 
    if pagenum == 0:
        url = f"https://www.nzdirectory.co.nz/{tag}.html"
    else:
        url = f"https://www.nzdirectory.co.nz/{tag}-{_Pagenumber}.html"
 
    page_html = requests.get(url)
    Soup = BeautifulSoup(page_html.text,'html.parser')
    details = Soup.find_all('p', class_ ="address")
    NzDirecotryList = []
    i = 0
 
    for Prodcuts in details:
        #The try is so make is so that 
        try:
            #Geths the Hole P tag and turns it into a string
            AddressString = details[i]
            StrPtag = str(AddressString)
 
            #Removing Front P HTML TAG
            FindFrontTag =StrPtag.index(">")
            RemoveFront = StrPtag[FindFrontTag:]
 
            #Removing Back P HTML TAG
            FindBackTag =RemoveFront.index("<")
            RemoveBack = RemoveFront[:FindBackTag]
 
            #String With no P HTML TAGS
            NoTags = RemoveBack
 
            #taking the Companys Name out of the STRING
            CompanyNameSnip = NoTags.index(",")
            CompanyName = NoTags[1:CompanyNameSnip]
 
            #Taking the Phone numbe from the +
            PhoneNumberSnip = NoTags.index("+")
            PhoneNumber = NoTags[PhoneNumberSnip:]
 
            #Taking the Address from between Address and Phone number
            Address = NoTags[CompanyNameSnip + 2:PhoneNumberSnip]
 
            NzDirecotryList = ("Name:" + CompanyName + "\n" + "Address: " + Address + "\n" + "PhoneNumber: " + PhoneNumber + "\n")
            print(NzDirecotryList)
 
            i = i + 1
        except:
        
            i = i + 1
            pass
 
for x in range(1, Pagenumber):
    pagenum = x
    NzDirecotry(tag, pagenum)