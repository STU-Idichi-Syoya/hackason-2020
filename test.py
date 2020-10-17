from flask import Flask, render_template #追加

app = Flask(__name__)
import random
@app.route('/<uuid>')
def hello(uuid):
    ppm=random.randint(100,2000)
    ppm=635

    # print(uuid)
    if ppm<1000:
        return render_template("chk.html",ppm=ppm)
    else:
        return render_template("tri.html",ppm=ppm)


## おまじない
if __name__ == "__main__":
    app.run(debug=True)