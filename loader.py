from flask import Flask, render_template
import json
import os

app = Flask(__name__)

for DataName in os.listdir('./data'):
    with open("./data/"+DataName, encoding='UTF8') as f:
        globals()[os.path.splitext(DataName)[0]] = json.load(f)

@app.route("/")
def test():
    # 메인화면
    # return render_template("Quest_View.html",BookData=bookdata, ReviewData=user_review, UserInfo=UserInfo) 

    # 다른사람 서재
    #return render_template("anotheruser_libray.html",UserInfo=UserInfo,LibraryData=OtherUserLibraryInformation) 

    # 책 정보
    return render_template("Book_Info.html", UserInfo=UserInfo, BookInfo=BookInfo)

    # 로그인
    #return render_template("Login.html")

    # 다른사람 리뷰 화면
    # return render_template("AnotherUser_Review.html", UserInfo=UserInfo, Datas=AnotherUser_Review)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) 
    