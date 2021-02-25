import requests
from bs4 import BeautifulSoup

sitenumber = 1
site = ""
sitelength = [1,2,3,4,5,6,7,8,9]



def choosesite(sitenumber):
    global site
    sitenumber
    if sitenumber == 1:
        site = "https://www.nzdirectory.co.nz/automotives.html"
    elif sitenumber == 2:
        site = "https://www.nzdirectory.co.nz/automotives-2.html"
    elif sitenumber == 3:
        site = "https://www.nzdirectory.co.nz/automotives-3.html"
    elif sitenumber == 4:
        site = "https://www.nzdirectory.co.nz/automotives-4.html"
    elif sitenumber == 5:
        site = "https://www.nzdirectory.co.nz/automotives-5.html"
    elif sitenumber == 6:
        site = "https://www.nzdirectory.co.nz/automotives-6.html"
    elif sitenumber == 7:
        site = "https://www.nzdirectory.co.nz/automotives-7.html"
    elif sitenumber == 8:
        site = "https://www.nzdirectory.co.nz/automotives-8.html"
    elif sitenumber == 9:
        site = "https://www.nzdirectory.co.nz/automotives-9.html"
    return site





for sitenumber in sitelength:
    site = choosesite(sitenumber)
    i = 0
    page_html = requests.get(site)
    html_soup = BeautifulSoup(page_html.text, 'html.parser')
    items = html_soup.find_all("p", class_="address")

    for cactus in items: #for every of that p tag

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
