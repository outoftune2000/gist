#!/usr/bin/python3
import pywikibot

person = input('Enter a name : ')

site = pywikibot.Site("en", "wikipedia")
page = pywikibot.Page(site, person)
item = pywikibot.ItemPage.fromPage(page)

item_dict = item.get()
clm_dict = item_dict["claims"]

clm_list = clm_dict["P569"]

for clm in clm_list:
    clm_trgt = clm.getTarget()
    print('Born on ' + str(clm_trgt.day) + '-' + str(clm_trgt.month) + '-' + str(clm_trgt.year))