"""."""
import os

from flask import Flask, render_template, request
from Estoque import Estoque

app = Flask(__name__, static_url_path='/static')

estoque = Estoque()


@app.route("/")
def index():
    """Index."""
    return render_template('index.html')


@app.route("/cadastrar_produto")
def cadastrar_produto():
    """."""
    return render_template("cadastrar_produto.html")


@app.route("/processar_cadastro", methods=['POST'])
def processar_cadastro():
    """."""
    dados = request.form
    nome = dados.get("nome_produto")
    preco = dados.get("preco_produto")
    min = dados.get("qtd_minima_produto")
    q = dados.get("qtd_produto")

    estoque.insere_produto(nome=nome, preco=preco, qtd_minima=min, qtd=q)

    return index()


@app.route("/lista")
def lista():
    """."""
    return render_template('lista.html',
                           lista=estoque.lista_todos_produtos(),
                           qtd_produtos=len(estoque))


@app.route("/lista_ordenada")
def lista_ordenada():
    """."""
    return render_template('lista.html',
                           lista=estoque.gera_lista_ordenada(),
                           qtd_produtos=len(estoque))


@app.route("/remocao_produtos")
def remocao_produtos():
    """."""
    return render_template("remocao_produto.html",
                           lista=estoque.lista_todos_produtos())


@app.route("/remover_produto", methods=['GET'])
def remover_produto():
    """."""
    dados = request.args
    estoque.remove_produto(id_produto=int(dados.get('id_produto')))

    return remocao_produtos()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

app.run(host='0.0.0.0', port=port)
