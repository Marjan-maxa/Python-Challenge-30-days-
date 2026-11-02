# Challenge - 1

from bs4 import BeautifulSoup
html="""<html>
<body>
    <h1>Book Store</h1>
    <h1>Family Planning</h1>
</body>
</html>
"""
obj=BeautifulSoup(html,"html.parser")

f_heding=obj.find('h1')
print("First Heading :",f_heding.get_text())













#Challenge -- 2




from bs4 import BeautifulSoup

html="""<html>
<body>
    <p class="book">Python Basics - 500 Tk</p>
    <p class="book">Learn Django - 700 Tk</p>
    <p class="book">AI with Python - 900 Tk</p>
    <div class="product">
    <h2>Laptop</h2>
    <p>Price: 50000 BDT</p>
</div>

<div class="product">
    <h2>Mobile</h2>
    <p>Price: 20000 BDT</p>
</div>

<div class="product">
    <h2>Headphone</h2>
    <p>Price: 1500 BDT</p>
</div>

</body>
</html>
"""
obje=BeautifulSoup(html,"html.parser")
print("All Praragarah :")
para_all=obje.find_all('p',class_="book")
for para in para_all:
    print(para.get_text())







# Challenge -- 3

from bs4 import BeautifulSoup
html="""<html>
<body>
    <p class="book">Python Basics - 500 Tk</p>
    <p class="book">Learn Django - 700 Tk</p>
    <p class="book">AI with Python - 900 Tk</p>
    <div class="product">
    <h2>Laptop</h2>
    <p>Price: 50000 BDT</p>
</div>

<div class="product">
    <h2>Mobile</h2>
    <p>Price: 20000 BDT</p>
</div>

<div class="product">
    <h2>Headphone</h2>
    <p>Price: 1500 BDT</p>
</div>

</body>
</html>
"""
obje=BeautifulSoup(html,"html.parser")
print("All Elements are :")
products=obje.find_all(class_="product")
for para in products:
    print(para.get_text())





#Challenge -- 4

import requests
from bs4 import BeautifulSoup


html="""<html>
<body>
<a href="https://www.google.com">Google</a>

<a href="https://www.youtube.com">YouTube</a>

<a href="https://www.facebook.com">Facebook</a>
</body>
</html>
"""


obj=BeautifulSoup(html,"html.parser")



link=obj.find_all("a")   
for links in link:
    if links:
        print("Link Name :",links.get_text(strip=True))
        print(links.get("href"))





# challenge -- 5

import requests
from bs4 import BeautifulSoup

url="https://meet.google.com/home?authuser=0"

try:
    response=requests.get(url,timeout=10)
    
    
    #http eror check
    response.raise_for_status()
    
    #status code print
    print("Status Code :",response.status_code)
    
    # html parse
    obj=BeautifulSoup(response.text,"html.parser")
    
    print("Page Title :",obj.title.get_text())
except requests.exceptions.ConnectionError:
    print("Network Error : Unable to connect the network!") 
except requests.exceptions.HTTPError as e:
    print("HTTP Error  :",e)    
except requests.exceptions.Timeout:
    print("Network Error : Request TimeOut!")    
except requests.exceptions.RequestException as e:
    print("Request Error :",e)

















#Challenge -- 6



from bs4 import BeautifulSoup

html = """
<html>
<body>
   
    <p class="book">Python Basics - 500 Tk</p>
    <p class="book">Learn Django - 700 Tk</p>
    <p class="book">AI with Python - 900 Tk</p>
</body>
</html>
"""


try:
    obj=BeautifulSoup(html,"html.parser")
    heading=obj.find('h1')
    if heading:
        print("Heading h1 :",obj.h1.get_text())
    else:
        print("h1 tag was not found!")    
        
        
except ValueError as e:
    print("System crashesd!")  
    
    
    











# Home Work 

from bs4 import BeautifulSoup


html="""
<html>
<body>
<head>
    <title>My Online Book Store</title>
</head>

    <h1>Welcome to My Book Store</h1>

    <div class="book">
        <h2>Python Programming</h2>
        <p>Price: 500 BDT</p>
        <a href="https://www.halvorsen.blog/documents/programming/python/resources/Python%20Programming.pdf">View Book</a>
    </div>

    <div class="book">
        <h2>Java Programming</h2>
        <p>Price: 600 BDT</p>
        <a href="https://www.sietk.org/downloads/javabook.pdf">View Book</a>
    </div>

    <div class="book">
        <h2>Web Development</h2>
        <p>Price: 450 BDT</p>
        <a href="https://www.scribd.com/document/704035343/Chapter-1-Introduction-to-Web-Development">View Book</a>
    </div>

    <div class="book">
        <h2>Data Science</h2>
        <p>Price: 700 BDT</p>
        <a href="https://people.smp.uq.edu.au/DirkKroese/DSML/DSML.pdf">View Book</a>
    </div>

    <div class="book">
        <h2>Machine Learning</h2>
        <p>Price: 800 BDT</p>
        <a href="https://people.smp.uq.edu.au/DirkKroese/DSML/DSML.pdf">View Book</a>
    </div>

</body>
        
</html>
"""          


obj=BeautifulSoup(html,"html.parser")       
print("Website Title :",obj.title.get_text(strip=True))   


print("Books name and Price :")
print("---------------------------")

books=obj.find_all(class_="book")
        
if books:
    for book in books:
        print("Book :",book.find('h2').get_text(strip=True))
        print("Price :",book.find('p').get_text(strip=True))
else :
    print("No Book Found!")        
          
       
# link

link=obj.find_all('a')
if link:
    for li in link:
        print("Text :",li.get_text(strip=True))
        print("Link :",li.get("href"))    
              
else :
    print("No link Found !")              