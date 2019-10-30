from flask import Flask,render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = "http://nodegarden.herokuapp.com/data_farm"
    data = requests.get(url, auth = ('thyago392035', '392035') )
    print(data.json()['dados'])
    return render_template("index.html", response = data.json()['dados'])

if __name__ == "__main__":
    app.run(debug=True)