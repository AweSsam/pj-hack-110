from flask import Flask, render_template, request
from helpers import constip

app: Flask = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("quiz.html")
    return render_template('index.html')

@app.route("/quiz")
def quiz():
    if request.method == "POST":
        return render_template("quiz.html")
    return render_template("quiz.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/jungle")
def jungle():
    return render_template("jungle.html")

@app.route("/shore")
def shore():
    return render_template("shore.html")

@app.route("/light")
def light():
    return render_template("light.html")

@app.route("/stream")
def stream():
    return render_template("stream.html")

@app.route("/streamgo")
def streamgo():
    return render_template("streamgo.html")

@app.route("/sit")
def sit():
    return render_template("sit.html")

@app.route("/take")
def take():
    return render_template("take.html")

@app.route("/foil")
def foil():
    return render_template("foil.html")

@app.route("/coconut")
def coconut():
    return render_template("coconut.html")

@app.route("/buy")
def buy():
    cheetos: int = request.form['cheetos']
    if request.method == "POST":
        num_cheetos: str = constip(cheetos)
        if num_cheetos == "live":
            return render_template("cheetogood.html", num_cheetos = num_cheetos)
        if num_cheetos == "constipation":
            return render_template("cheetobad.html", num_cheetos = num_cheetos)
    return render_template("buy.html")

@app.route("/save")
def save():
    return render_template("save.html")

@app.route("/drink")
def drink():
    return render_template("drink.html")

@app.route("/streamsurvive")
def streamsurvive():
    return render_template("streamsurvive.html")

@app.route("/moncoco")
def moncoco():
    return render_template("moncoco.html")

@app.route("/moncheetos")
def moncheetos():
    return render_template("moncheetos.html")

@app.route("/monnothing")
def monnothing():
    return render_template("monnothing.html")

@app.route("/moncheetos2")
def moncheetos2():
    return render_template("moncheetos2.html")

@app.route("/moncoco")
def moncoco():
    return render_template("moncoco.html")

@app.route("/monnocheetos")
def monnocheetos():
    return render_template("monnocheetos.html")

@app.route("/monnothing")
def monnothing():
    return render_template("monnothing.html")

if __name__ == '__main__':
    app.run(debug=True)