from flask import Flask,g,request,jsonify
from database import db_helpers
from functools import wraps

api_username = "thyago392035"
api_password = "392035"

def protected(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        auth = request.authorization
        if auth and auth.username == api_username and auth.password == api_password:
            return f(*args,**kwargs)
        else:
            return jsonify({"message " : "Authentication failed"}),403
    return decorated

app = Flask(__name__)
@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()

@app.route("/member", methods = ["GET"])
@protected
def get_members():
    db = db_helpers.get_db()
    response_qry = db.execute("SELECT * FROM members")
    members = response_qry.fetchall()
    list_members = []
    for member in members:
        member = {"id":member["id"],"name":member['name'],"email":member["email"],"level":member["level"]}
        list_members.append(member)
    return jsonify(list_members)


@app.route("/member/<int:member_id>",methods=["GET"])
@protected
def get_member(member_id):
    db = db_helpers.get_db()
    response_qry = db.execute("SELECT * FROM members WHERE id == {}".format(member_id))
    data_member = response_qry.fetchone()
    member = {"id":data_member["id"],"name":data_member["name"],"email":data_member["email"],"level":data_member["level"]}
    return jsonify(member)


@app.route("/member",methods=["POST"])
@protected
def add_member():
    new_member = [value for value in request.get_json().values()]
    db = db_helpers.get_db()
    db.execute("INSERT INTO members (name,email,level) VALUES (?,?,?)",new_member)
    db.commit()
    return "Membro inserido com sucesso"

@app.route("/member/<int:member_id>",methods=["PUT","PATCH"])
@protected
def edit_member(member_id):
    db = db_helpers.get_db()
    if request.method == "PUT":
        new_values = [value for value in request.get_json().values()]
        new_values.append(member_id)
        db.execute("UPDATE members SET name = '{}',email = '{}',level = '{}' WHERE id = {}".format(*new_values))
        db.commit()
        return "Membro COMPLETAMENTE editado com sucesso"
    keys = [*request.get_json()]
    values = [*request.get_json().values()]
    qry = "UPDATE members SET "
    for n in range(len(values)):
        if n < len(values)-1:
            qry += "{} = '{}',".format(keys[n],values[n])
        elif n == len(values)-1:
            qry += "{} = '{}'".format(keys[n],values[n])
    qry += " WHERE id = {}".format(member_id)
    db.execute(qry)
    db.commit()
    return "Membro PARCIALMENTE editado com sucesso"


@app.route("/member",methods=["DELETE"])
@protected
def delete_members():
    db = db_helpers.get_db()
    db.execute("DELETE FROM members")
    db.commit()
    return "Todos os membros foram deletados com sucesso"


@app.route("/member/<int:member_id>",methods=["DELETE"])
@protected
def delete_member(member_id):
    db = db_helpers.get_db()
    db.execute("DELETE FROM members WHERE id == {}".format(member_id))
    db.commit()
    return "Membro deletado com sucesso"

if __name__ == "__main__":
    app.run(debug=True)