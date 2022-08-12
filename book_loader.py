import json

# 같은 폴더 레벨에 있는 book.json을 읽기 모드로 가져오고, 그것을 f라 지칭
with open('books.json', 'r', encoding='UTF8') as f:
    # book_list에 현재 json 형식으로 불러온 f를 저장
    book_list = json.load(f)

new_list = []
for book in book_list:
    # 우리의 목적에 나와있는 것과 같이 모델의 이름을 설정해주는 것이다.
    # 모델의 이름을 우리는 'book'으로 쓰기로 함
    new_data = {"model": "review.book"}
    new_data["fields"] = book
    new_list.append(new_data)

# json 파일을 만들기 전에 생성된 모델의 형태 확인
print(new_list)

# json 파일로 생성 ㄱㄱ
# 아까와 같이 book_data.json이라는 파일을 쓰기모드로 가져오고 인코딩 형식을 지정해줌
# 우리는 book_data.json이라는 파일이 없는데, 이렇게 쓰면 자기가 알아서 파일을 만들어줌!
with open('books_data.json', 'w', encoding='UTF-8') as b:
    json.dump(new_list, b, ensure_ascii=False, indent=2)
