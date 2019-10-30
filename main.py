"""."""
import os

from flask import Flask, render_template, request
from Estoque import Estoque

app = Flask(__name__, static_url_path='/static')

estoque = Estoque()


@app.route("/")
def login(msg=''):
    """Index."""
    return render_template('index.html', msg=msg)


@app.route("/teste", methods=['POST'])
def teste():
    """."""
    dados = request.form
    nome = dados.get("nome_produto")
    preco = dados.get("preco_produto")
    min = dados.get("qtd_minima_produto")
    q = dados.get("qtd_produto")

    return str(nome) + " - " + str(preco) + " - " + str(min) + " - " + str(q)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

app.run(host='0.0.0.0', port=port)
