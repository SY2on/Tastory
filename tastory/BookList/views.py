from django.shortcuts import render
from models import BestBookList
import pandas as pd
import json

# Create your views here.
with open('./testA.json', 'r') as f:
    data = json.loads(f.read())

# dataFrame 변환
df = pd.json_normalize(data)

for idx, row in df.iterrows():
    BestBookList.objects.create(isbn=row['isbn'], category=row['category'],
                            title=row['title'], author=row['author'],
                            book_info=row['book_info'], pubdate = row['pubdate'], publisher = row['publisher'], img_url = ['img_url'])
