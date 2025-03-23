from flask import Flask, render_template, request,redirect,url_for
import datetime

app = Flask(__name__)


@app.route('/home')

def home():
    
    return render_template("index.html")

@app.route("/heure")
def heure():
    date_heure = datetime.datetime.now()
    h = date_heure.hour
    m = date_heure.minute
    s = date_heure.second
    return render_template("heure.html", heure = h,minute = m, seconde = s)


if __name__ == "__main__":
    app.run(debug=True)
