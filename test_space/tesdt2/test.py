from flask import Flask, render_template #追加

app = Flask(__name__,static_folder="static")
import random
@app.route('/<uuid>')
def hello(uuid):
    ppm=random.randint(100,2000)
    # ppm=ppm

    # print(uuid)
    if ppm<1000:
        return render_template("chk.html",ppm=ppm)
    else:
        return render_template("tri.html",ppm=ppm)
@app.route('/')
def root():
    return render_template("食堂店舗のご案内｜食堂｜関西大学生活協同組合.html")
## おまじない
if __name__ == "__main__":
    app.run(debug=False,port=5555)