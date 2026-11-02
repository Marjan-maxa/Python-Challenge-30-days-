from bs4 import BeautifulSoup
import csv
html=open("book.html",encoding="utf-8").read()
obj=BeautifulSoup(html,"html.parser")
book=obj.find_all(class_="book")
print("---------------------")
print("Books Details :")
print("---------------------")
for books in book:
    if books:
        print("Name :",books.find("h2").get_text(strip=True))
        print("Price :",books.find("p").get_text(strip=True))
    else:
        print("Books Not Found !")  
        
        
with open("books.csv","+a",newline="") as file:
    writer=csv.writer(file)
    
    writer.writerow(["Book Name","Price"]) 
    for books in book:
        name=books.find("h2").get_text(strip=True)
        price=books.find("p").get_text(strip=True)
        
        writer.writerow([name,price])
        
print("CSV file Created!")        