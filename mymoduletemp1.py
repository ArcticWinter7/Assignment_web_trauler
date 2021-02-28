import requests
from bs4 import BeautifulSoup

sitenumber = 1
site = ""
categorylist = ["automotives", "advertising", "building-tools"]
sitelength = findpagecount(categorylist) 
categoriesdone = 0
done = 0
currentcategory = ""
currentpagenumber = 0

def findpagecount(tag):
    page_html = requests.get(f"https://www.nzdirectory.co.nz/{tag}.html")
    Soup = BeautifulSoup(page_html.text, 'html.parser')
    NzDirecotryPageNum = Soup.find_all('div', id="page_cat")
    NzDirecotryListNum = []
    return nzli


def incrimentpage(category,pagenumber):
    global currentpagenumber
    if pagenumber == 0:
        newpage = f"https://www.nzdirectory.co.nz/{category}.html"
    else:
        newpage = f"https://www.nzdirectory.co.nz/{category}-{pagenumber}.html"
    currentpagenumber = pagenumber + 1
    return newpage

def choosecategory(catlist, catsdone):
    currentcat = catlist[catsdone]
    return currentcat
    print("not done yet")


for x in categorylist:

    currentcategory = choosecategory(categorylist, categoriesdone)
    currentpagenumber = 0
    print("Current category: " + currentcategory + "\n")
    for sitenumber in sitelength:
        site = incrimentpage(currentcategory,currentpagenumber)
        i = 0
        page_html = requests.get(site)
        html_soup = BeautifulSoup(page_html.text, 'html.parser')
        items = html_soup.find_all("p", class_="address")

        for taj in items: #for every of that p tag

            try:
                # take the bs4 variable and string it
                focused_string = items[i]
                focus_string = str(focused_string)

                # find point of actual string
                stringsniparea1 = focus_string.index(">")
                stringsnipped1 = focus_string[stringsniparea1:]

                stringsniparea2 = stringsnipped1.index("<")
                stringsnipped2 = stringsnipped1[:stringsniparea2]

                # the string free of paragraph tags
                cleanstring = stringsnipped2

                # snipping the business name
                business_name_snip_area = cleanstring.index(",")
                business_name = cleanstring[1:business_name_snip_area]

                # snipping phone number
                phone_number_snip_area = cleanstring.index("+")
                phone_number = cleanstring[phone_number_snip_area:]

                # snipping the address
                address = cleanstring[business_name_snip_area + 2:phone_number_snip_area]

                # combining and displaying string
                displaystring = ("Business name: " + business_name + "\n" + "Address: " + address + "\n" + "Phone number: " + phone_number + "\n")
                print(displaystring)

                i = i + 1
            except:
                i = i + 1
    categoriesdone = categoriesdone + 1
