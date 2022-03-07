from config.Config import Config
from config.Database import Database
from dao.PinturasDao import PinturasDao
from flask import Flask, request, render_template

from model.Pinturas import Pinturas

app = Flask(__name__)

dao = PinturasDao(Database(Config().config).conn)

@app.route('/', methods=["GET"])
def main():
    lista = dao.listarPinturas()
    return render_template("main.html", lista=lista)

@app.route('/pintura/criar', methods=["GET"])
def nova():
    return render_template("inserir.html")

@app.route('/pintura/criar', methods=["POST"])
def criar():
    pintura = Pinturas()
    pintura.idcodigo = request.form.get("idcodigo")
    pintura.nomedaobra = request.form.get("nomedaobra")
    pintura.preco = request.form.get("preco")
    pintura.artista = request.form.get("artista")

    dao.inserirPinturas(pintura)

    lista = dao.listarPinturas()
    return render_template(
        "main.html",
        lista=lista
    )
    

@app.route('/pintura/<idcodigo>', methods=["GET"])
def editarPagina(idcodigo):
    pintura = dao.selecionarPinturas(idcodigo)
    return render_template("editar.html", pintura=pintura)

@app.route('/pintura/editar', methods=["POST"])
def editar():
    pintura = Pinturas()
    pintura.idcodigo = request.form.get("idcodigo")
    pintura.nomedaobra = request.form.get("nomedaobra")
    pintura.preco = request.form.get("preco")
    pintura.artista = request.form.get("artista")
    pintura = dao.alterarPinturas(pintura)
    
    lista = dao.listarPinturas()
    return render_template(
        "main.html",
        lista=lista
    )

@app.route('/pintura/remover/<idcodigo>', methods=["GET"])
def remover(idcodigo):
    pintura = Pinturas()
    pintura.idcodigo = idcodigo
    dao.excluirPinturas(pintura)
    
    lista = dao.listarPinturas()
    return render_template(
        "main.html",
        lista=lista
    )

if __name__ == '__main__':
    app.run()
