from flask import Flask,jsonify,request
app = Flask(__name__)

# BASICO
@app.route("/")
def index():
    return "<h1> Meu primeiro Hello World com FLASK </h1>"

# TESTANDO PARAMETROS DEFAUL
@app.route("/information",methods=["POST","GET"],defaults={"name" : "Nome_Default"})
@app.route("/information/<name>",methods=["POST","GET"])
def info(name):
    return "<h1> Bem vindo a pagina de informaçao, {} <h1>".format(name.upper())

# QUERY STRING
# CASO EU PASSE ALGO ASSIM /query?name=Thyago&location=Pindoretama
# IREI CONSEGUI PEGAR OS VALORES DE NAME E LOCATION USANDO REQUEST.ARGS.GET
# @app.route("/query")
def query():
    name = request.args.get("name")
    location = request.args.get("location")
    return "<h1> Hi, {}, your location is {} </h1>".format(name,location)

# JSON
@app.route("/json")
def json():
    return jsonify( {"Key1" : 1, "Key2_new" : [1,2,3] })

# USANDO DADOS DE UM FORM
@app.route("/data_form")
def form():
    return ''' <form method="POST" action="/process_data"> 
                   <input type="text" name="name">
                   <input type="text" name="location">
                   <input type="submit" value="Submit">
               </form>
           '''
# OS DADOS COLOCADOS NA ROTA data_form SAO REPASSADOS PARA ESSA ROTA
# PODEMOS PEGALOS USANDO O request.form["nome do campo"]
# DEVEMOS ESPECIFICAR O METHOD POST,JA Q É O METODO PARA REPASSARMOS VALORES
@app.route("/process_data",methods=["POST"])
def process():
    name = request.form['name']
    location = request.form['location']
    return "Hello {}, you're from {}!".format(name,location)

# PEGANDO VARIAVEIS PELA URL
@app.route("/puppy_latin/<name>")
def puppy_name(name):
    if name[-1] != "y":
        name += "y"
    else:
        name = name[:-1] + "iful"
    return "<h1> Name of puppy in puppy latin : {}".format(name)

@app.route("/rec_data_json",methods=['POST'])
def json_data():
    data = request.get_json()
    return "<h1> Name : {}, Location : {}  </h1>".format(data['name'],data['location'])

if __name__ == "__main__":
    app.run(debug=True)