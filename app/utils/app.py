from flask import Flask, render_template, redirect, url_for, request
from flask_sql import SQL
from .forms import ClienteForm
from .models import db, Cliente

app = Flask(__name__)
app.config['SQL_DATABASE_URI'] = 'mysql://usuario:senha@localhost/nome_do_banco'
app.config['SQL_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

@app.route('/')
def index():
    return redirect(url_for('listar_clientes'))

@app.route('/clientes/', methods=['GET'])
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)

@app.route('/cliente/novo', methods=['GET', 'POST'])
def adicionar_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        cliente = Cliente(nome=form.nome.data, endereco=form.endereco.data, contato=form.contato.data)
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('listar_clientes'))
    return render_template('cliente_form.html', form=form)

@app.route('/cliente/<int:id>/editar', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    form = ClienteForm(obj=cliente)
    if form.validate_on_submit():
        cliente.nome = form.nome.data
        cliente.endereco = form.endereco.data
        cliente.contato = form.contato.data
        db.session.commit()
        return redirect(url_for('listar_clientes'))
    return render_template('cliente_form.html', form=form, cliente=cliente)

@app.route('/cliente/<int:id>/deletar', methods=['POST'])
def deletar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('listar_clientes'))

if __name__ == '__main__':
    app.run(debug=True)
