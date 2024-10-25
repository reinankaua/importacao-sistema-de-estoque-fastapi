from flask import Flask, render_template, request
from .database import SessionLocal
from .models import Cliente, Produto, Estoque

app = Flask(__name__)

@app.route("/clientes/")
def listar_clientes():
    db = SessionLocal()
    clientes = db.query(Cliente).all()
    return render_template("clientes.html", clientes=clientes)

@app.route("/estoque/")
def consulta_estoque():
    db = SessionLocal()
    cliente_id = request.args.get('cliente_id')
    produto_id = request.args.get('produto_id')
    
    query = db.query(Estoque)
    if cliente_id:
        query = query.filter_by(cliente_id=cliente_id)
    if produto_id:
        query = query.filter_by(produto_id=produto_id)
        
    estoque = query.all()
    return render_template("estoque.html", estoque=estoque)
