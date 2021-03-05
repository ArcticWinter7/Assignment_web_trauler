import requests
from bs4 import BeautifulSoup

def module1(_entercategories):

    sitenumber = 1
    site = ""
    categorylist = _entercategories
    categoriesdone = 0
    done = 0
    currentcategory = ""
    currentpagenumber = 0
    exitdisplaystring = ""
    namelist = []
    addresslist = []
    contactlist = []


    def findpagecount(tag):
        page_html = requests.get(f"https://www.nzdirectory.co.nz/{tag}.html")
        Soup = BeautifulSoup(page_html.text, 'html.parser')
        NzDirecotryPageNum = Soup.find_all('div', class_="pages")
        NzDirecotryListNum = []
        _pagecount = len(NzDirecotryListNum)
        return NzDirecotryPageNum


    def incrimentpage(category,pagenumber):
        if pagenumber == 0:
            newpage = f"https://www.nzdirectory.co.nz/{category}.html"
        else:
            newpage = f"https://www.nzdirectory.co.nz/{category}-{pagenumber}.html"
        newcurrentpagenumber = pagenumber + 1
        return newpage,newcurrentpagenumber

    def choosecategory(catlist, catsdone):
        currentcat = catlist[catsdone]
        return currentcat
        print("not done yet")


    for x in categorylist:

        currentcategory = choosecategory(categorylist, categoriesdone)
        sitelength = findpagecount(currentcategory) 
        currentpagenumber = 0
        # print("Current category: " + currentcategory + "\n")
        currentcategorytemp = ("Current category: " + currentcategory + "\n")

        exitdisplaystring = exitdisplaystring + currentcategorytemp

        for y in sitelength:
            site,currentpagenumber = incrimentpage(currentcategory,currentpagenumber)
            i = 0
            page_html = requests.get(site)
            html_soup = BeautifulSoup(page_html.text, 'html.parser')
            items = html_soup.find_all("p", class_="address")

            for z in items: #for every of that p tag

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
                    # print(displaystring)
                    exitdisplaystring = exitdisplaystring + displaystring
                    namelist.append(business_name)
                    addresslist.append(address)
                    contactlist.append(phone_number)

                    i = i + 1
                except Exception as e:
                    print(e)
                    i = i + 1
                    print(e)
        categoriesdone = categoriesdone + 1
    return namelist,addresslist,contactlist

# def start():
#     entercategories = ["automotives","advertising"]
#     print(module1(entercategories))

# start()
