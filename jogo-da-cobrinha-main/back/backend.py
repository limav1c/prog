from config import *
from modelo import *

@app.route("/")
def ola():
    return "backend operante"

# curl localhost:5000/incluir/Caverna -X POST -d '{"mensagem":"Dragão da história: quando foi descoberto o Brasil?", "continua":1, "segredo":"1500", "x":50, "y":200, "nome_imagem":"caverna1_mini.png"}' -H "Content-Type:application/json"
@app.route("/incluir/Jogador", methods=['post'])
def incluir(classe):
    # receber as informações do novo objeto
    dados = request.get_json()  
    try:
        nova = None
        if classe == "Jogador":
            nova = Jogador(**dados)

        db.session.add(nova)  # adicionar no BD
        db.session.commit()  # efetivar a operação de gravação
        # retorno de sucesso :-)
        return jsonify({"resultado": "ok", "detalhes": "ok"})
    except Exception as e:  # em caso de erro...
        # informar mensagem de erro :-(
        return jsonify({"resultado": "erro", "detalhes": str(e)})

# curl localhost:5000/listar/Caverna
@app.route("/listar/Jogador")
def listar(classe):
    # obter os dados da classe informada
    dados = None
    if classe == "Jogador":
        dados = db.session.query(Jogador).all()
    if dados:
      # converter dados para json
      lista_jsons = [x.json() for x in dados]

      meujson = {"resultado": "ok"}
      meujson.update({"detalhes": lista_jsons})
      return jsonify(meujson)
    else:
      return jsonify({"resultado":"erro", "detalhes":"classe informada inválida: "+classe})

# criar o banco de dados, caso não esteja criado
db.create_all()

# provendo o CORS ao sistema
CORS(app)

# iniciar o servidor
app.run(debug=True)
