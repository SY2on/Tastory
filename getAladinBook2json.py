import requests
from bs4 import BeautifulSoup
import json

startpg = 1
endpg = 1000
FinialBookDataList = []
TitleList = []
#BookDataDict = {'title':"", 'bookcover':"",'descript':"", 'author':""}
key = '' #Input Key 
print("\n\n\n\n\n\n")
for A in range(2, 10):
    BookDataDict = {'title':"", 'bookcover':"",'descript':"", 'author':""}
    url = f"http://www.aladin.co.kr/ttb/api/ItemList.aspx?ttbkey={key}&QueryType=ItemNewAll&MaxResults={A}&start={A}&SearchTarget=Book&output=xml&Version=20131101"
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    TitleList = str(soup).split("</searchcategoryname>")[1]

    title = TitleList.split("<title>",1)[1].split("</title>",1)[0]
    #print(title)
    author = TitleList.split("<author>",1)[1].split("</author>",1)[0]
    #print(author)
    description = TitleList.split("<description>",1)[1].split("</description>",1)[0]
    print(description)
    logo = TitleList.split("<cover>",1)[1].split("</cover>",1)[0]
    BookDataDict["title"] = title
    BookDataDict["bookcover"] = logo
    BookDataDict["author"] = author
    BookDataDict["descript"] = description
    FinialBookDataList.append(BookDataDict)
    print("==========\n")

print(FinialBookDataList)

with open('./testA.json', 'w', encoding='utf-8') as make_file:
    json.dump(FinialBookDataList, make_file, indent="\t", ensure_ascii=False)