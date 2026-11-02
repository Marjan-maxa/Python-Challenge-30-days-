import requests
from bs4 import BeautifulSoup
url="https://diu.ac/about-us"
response=requests.get(url,timeout=12)
response.raise_for_status()
obj=BeautifulSoup(response.text,"html.parser")
print(obj.title.get_text())
first=obj.find("p")
print(first.get_text())

print("Headings are :")
print("----------------------")
heading_find=obj.find_all(['h1','h2','h3','h4','h5','h6','h7','h8'])
for heading in heading_find:
    print(heading.get_text())
    
print("---------------------------------------") 



link=obj.find_all("a")   
for links in link:
    if links:
        print("Link Name :",links.get_text(strip=True))
        print(links.get("href"))