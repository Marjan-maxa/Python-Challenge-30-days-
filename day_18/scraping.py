from bs4 import BeautifulSoup
html = """
<html>
<body>
    <h1>Book Store</h1>
    <p class="book">Python Basics - 500 Tk</p>
    <p class="book">Learn Django - 700 Tk</p>
    <p class="book">AI with Python - 900 Tk</p>
</body>
</html>
"""
obj=BeautifulSoup(html,"html.parser")
title=obj.find('h1')
books=obj.find_all('p',class_="book")
print(title.get_text())
for book in books:
    print("Book are :", book.get_text())