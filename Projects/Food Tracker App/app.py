from flask import Flask,render_template,jsonify,request,g
import sqlite3

app = Flask(__name__)

def db_connect():
    sql = sqlite3.connect("database/food.db")
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g,"sqlite3_db"):
        g.sqlite3_db = db_connect()
    return g.sqlite3_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,"sqlite3_db"):
        g.sqlite3_db.close()

@app.route("/",methods=["POST","GET"])
def index():
    db = get_db()
    if request.method == "POST":
        data = request.form["date"]
        return data.replace("-")
    else:
        return render_template("home.html")

@app.route("/view")
def home():
    return render_template("day.html")

@app.route("/add",methods=['GET','POST'])
def add_food():
    db = get_db()
    if request.method == 'POST':
        food_name = request.form['food-name']
        protein = int(request.form['protein'])
        carbo = int(request.form["carbohydrates"])
        fat = int(request.form['fat'])
        calories = protein+carbo+fat
        
        db.execute("insert into food(name_food,protein,carbohydrates,fat,calories) values (?,?,?,?,?)",[food_name,protein,carbo,fat,calories])
        db.commit()
        return render_template("add_food.html",test = True)
    qry = db.execute("select name_food,protein,carbohydrates,fat,calories from food")
    results = qry.fetchall()
    return render_template("add_food.html", data = results)   


if __name__ == '__main__':
    app.run(debug=True)