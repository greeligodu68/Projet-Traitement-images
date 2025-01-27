from flask import Flask, render_template, request,redirect,url_for


app = Flask(__name__)

@app.route("/")
def home():
    
      
        

    return render_template("index.html")

@app.route("/test")
def test():
     
     return 'test'



if __name__ == "__main__":
    app.run(debug=True)
