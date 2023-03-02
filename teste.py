#TESTANDO 

from flask import Flask

app = Flask(__name__)

@app.route("/")
def ola():
    return "<b>Olá, gente!!</b>"

app.run(debug=True, host="0.0.0.0", port=4999)

