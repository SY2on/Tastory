import requests
from bs4 import BeautifulSoup
import json

startpg = 1
endpg = 1000
FinialBookDataList = []
TitleList = []
#BookDataDict = {'title':"", 'bookcover':"",'descript':"", 'author':""}
key = 'ttbqus71461328001' #Input Key 
print("\n\n\n\n\n\n")
for A in range(2, 34):
    BookDataDict = {'title':"", 'img_url':"",'book_info':"", 'author':"", 'isbn':"", 'category':"", 'pubdate':"", 'publisher':""}
    url = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={key}&QueryType=ItemNewAll&MaxResults={A}&start={A}&SearchTarget=Book&output=xml&Version=20131101"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    TitleList = str(soup).split("</searchcategoryname>")[1]
    #print(TitleList)
    title = TitleList.split("<title>",1)[1].split("</title>",1)[0]
    print(title)
    author = TitleList.split("<author>",1)[1].split("</author>",1)[0]
    #print(author)
    description = TitleList.split("<description>",1)[1].split("</description>",1)[0]
    #print(description)
    logo = TitleList.split("<cover>",1)[1].split("</cover>",1)[0]
    isbn = TitleList.split("<isbn>",1)[1].split("</isbn>",1)[0]
    category = TitleList.split("<categoryname>",1)[1].split("</categoryname>",1)[0]
    publisher = TitleList.split("<publisher>",1)[1].split("</publisher>",1)[0]
    pubdate = TitleList.split("<pubdate>",1)[1].split("</pubdate>",1)[0]
    BookDataDict["title"] = title
    BookDataDict["img_url"] = logo
    BookDataDict["author"] = author
    BookDataDict["book_info"] = description
    BookDataDict["isbn"] = isbn
    BookDataDict["category"] = category
    BookDataDict["pubdate"] = pubdate
    BookDataDict["publisher"] = publisher
    FinialBookDataList.append(BookDataDict)
    print("==========\n")

#print(FinialBookDataList)

with open('./testA.json', 'w', encoding='utf-8') as make_file:
    json.dump(FinialBookDataList, make_file, indent="\t", ensure_ascii=False)