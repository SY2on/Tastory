from flask import Flask, render_template
import json
app = Flask(__name__)
with open("testA.json") as f:
	bookdata = json.load(f)
with open("user_review.json") as f:
    review = json.load(f)
with open("userinfo.json") as f:
    userinfo = json.load(f)
@app.route("/")
def test():
    return render_template("test.html",bookdata=bookdata, review=review)


@app.route("/1")
def aaa():
    return render_template("anotheruser_libray.html",userinfo=userinfo)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)