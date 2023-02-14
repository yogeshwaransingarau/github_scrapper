import nltk
from bs4 import BeautifulSoup
import requests

inp = input("Enter the author: ")
url=("https://github.com/" + inp + "?tab=repositories")
req=requests.get(url)
soup=BeautifulSoup(req.text,'html.parser')
res=soup.find_all(class_="wb-break-all")

# tokens=nltk.word_tokenize(res)
for i in res:
    print(i.text)
