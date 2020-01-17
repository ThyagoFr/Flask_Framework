from flask import Flask,render_template,g,request
import sqlite3

app = Flask(__name__)

def connect_db():
    sql = sqlite3.connect("data.db")
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,"sqlite3"):
        g.sqlite_db.close()

@app.route("/")
def index():
    return "<h1> HM </h1>"

@app.route("/form",methods =['POST','GET'])
def form():
    if request.method == 'GET':
        return render_template("form.html")
    else :
        name = request.form['name']
        location = request.form['location']

        db = get_db()
        db.execute("insert into users (name,location) values (?,?)",[name,location])
        db.commit()
    return render_template("form.html")   

@app.route("/home/<name>")
def home(name):
    return render_template("home.html",test = name, display=True,lista = [1,2,3], dic = {"Key1" : 1, "Key2" : 2})

@app.route("/viewdatabase")
def view():
    db = get_db()
    qry = db.execute("select id,name,location from users")
    results = qry.fetchall()
    return render_template("view.html",data = results)

if __name__ == "__main__":
    app.run(debug=True)