from flask import Flask, render_template
import json
app = Flask(__name__)
with open("testA.json") as f:
	bookdata = json.load(f)
with open("user_review.json") as f:
    review = json.load(f)
@app.route("/")
def test():
    return render_template("test.html",bookdata=bookdata, review=review)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)