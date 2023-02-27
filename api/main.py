from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/home')
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/manga')
def manga():
    id = request.args.get("mal_id")
    name = request.args.get("name")
    return render_template("manga.html", id = id,name=name)

@app.round("/manga/chapters")
def chapters():
  id = request.args.get("name")
  return render_template("chapters.html", name = name)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8000)