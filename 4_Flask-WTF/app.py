from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,IntegerField
from wtforms.validators import InputRequired,Length,Email

app = Flask(__name__)
app.config['SECRET_KEY'] = "MySecret"

class LoginForm(FlaskForm):
    username = StringField(label="HMMMM",validators=[InputRequired()])
    password = PasswordField(label="password",validators=[InputRequired(),Length(min=5,max=8,message="A senha precisa conter no minimo 5 e no maximo 8 caracteres")])
    true = BooleanField("true")
    age = IntegerField("age")
    email = StringField("email",validators=[Email()])

class User():
    def __init__(self,username,email,age):
        self.username = username
        self.email = email
        self.age = age

@app.route("/",methods=["GET","POST"])
def index():
    new_user = User("Thyago Freitas","thyagofr@alu.ufc.br",30)
    form = LoginForm(obj=new_user)
    if form.validate_on_submit():
        res = '<h1>Username : {}, Password : {}, Boolean : {} </h1>'.format(form.username.data,form.password.data,form.true.data)
        return res
    return render_template("index.html",form=form)

if __name__ == "__main__":
    app.run(debug=True) 