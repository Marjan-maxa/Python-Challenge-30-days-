import requests
from bs4 import BeautifulSoup
url="https://www.daraz.com.bd/tea/?up_id=225151210&clickTrackInfo=ctr--0.0___matchType--20___description--25%2525%2B%25E0%25A6%25AC%25E0%25A6%25A8%25E0%25A7%258D%25E0%25A6%25A7___seedItemMatchType--c2i___bucket--0___spm_id--category.hp___seedItemScore--0.0___abId--379344___score--0.1___pvid--3852356c-1669-4578-ab1c-be1343e31466___refer--___appId--7253___seedItemId--225151210___scm--1007.17253.379344.0___objType--category___categoryId--7241___cvr--0.0___timestamp--1793301045895&from=hp_categories&item_id=225151210&version=v2&q=%E0%A6%9A%E0%A6%BE&params=%7B%22catIdLv1%22%3A%223752%22%2C%22pvid%22%3A%223852356c-1669-4578-ab1c-be1343e31466%22%2C%22src%22%3A%22ald%22%2C%22categoryName%22%3A%22%25E0%25A6%259A%25E0%25A6%25BE%22%2C%22categoryId%22%3A%227241%22%7D&src=hp_categories&spm=a2a0e.tm80335411.categoriesPC.d_2_7241"
response=requests.get(url,timeout=10)
response.raise_for_status()
obj=BeautifulSoup(response.text,"html.parser")
print("Page Title :",obj.title.get_text(strip=True))
print("Page Text :",obj.text)
headings = obj.find_all(["h1", "h2", "h3"])

for heading in headings:
    print(heading.get_text(strip=True))