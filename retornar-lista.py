from flask import Flask, jsonify

app = Flask(__name__)

app.route("/")
def padrao():
    # cria o texto de retorno padrão com links :-p
    return '''Exemplo de servidor que retorna lista. Ações:
    <a href="/lista_texto">Lista em texto</a> | 
    <a href="/lista_json">Lista em json</a>
    '''
@app.route("/lista_texto")
def lista_texto():
    # cria a lista
    lista = ['ola', 'esta lista', 'vai ser mostrada', 
             'em formato', 'textual']
    # inicia uma variável de retorno
    retorno = ''
    # percorre a lista
    for s in lista:
        # concatena a string no retorno, separando por quebra de linha
        retorno += "<br>"
        retorno += s

    # retorna a string final
    return retorno

@app.route("/lista_json")
def lista_json():
    # cria a lista
    lista = ['será que', 'você vai gostar', 'da lista em json?',
             'veremos', ':-)']
    # retorna a lista em formato json
    # note que no import do flask (linha 1) 
    # é preciso informar o jsonify
    return jsonify(lista)

app.run()

'''
resultados de execução:

$ curl localhost:5000
Exemplo de servidor que retorna lista. Ações:
    <a href="/lista_texto">Lista em texto</a> | 
    <a href="/lista_json">Lista em json</a>

$ curl localhost:5000/lista_texto
<br>ola<br>esta lista<br>vai ser mostrada<br>em formato<br>textual

$ curl localhost:5000/lista_json
["ser\u00e1 que","voc\u00ea vai gostar","da lista em json?","veremos",":-)"]

'''
