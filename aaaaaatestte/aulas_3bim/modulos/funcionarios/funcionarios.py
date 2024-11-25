from flask import Blueprint, render_template, request, redirect, flash
from models import Funcionarios
from models import Empresa
from database import db

bp_funcionarios = Blueprint('funcionarios', __name__, template_folder='templates')

@bp_funcionarios.route('/')
def index():
    dados = Funcionarios.query.all()
    return render_template('funcionarios.html', funcionarios = dados)

@bp_funcionarios.route('/add')
def add():
    dados = Empresa.query.all()
    return render_template('funcionarios_add.html', empresa = dados)

@bp_funcionarios.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    cargo = request.form.get('cargo')
    id_empresa = request.form.get('id_empresa')
    if nome and cargo and id_empresa:
        bd_pedido = Funcionarios(nome, cargo, id_empresa)
        db.session.add(bd_pedido)
        db.session.commit()
        flash('Pedido salvo com sucesso!!!')
        return redirect('/funcionarios')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/funcionarios/add')
    
@bp_funcionarios.route('/edit/<int:id_funcionario>')
def edit(id_funcionario):
    dados = Funcionarios.query.get(id_funcionario)
    return render_template('funcionarios_edit.html', funcionarios = dados)

    
@bp_funcionarios.route('/editsave', methods=['POST'])
def editsave():
    id_empresa = request.form.get('id_empresa')
    nome = request.form.get('nome')
    cargo = request.form.get('cargo')
    if id_empresa and nome and cargo:
        funcionario = Funcionarios.query.get(id_empresa)
        funcionario.nome = nome
        funcionario.cargo = cargo
        funcionario.id_empresa = id_empresa
        db.session.commit()
        flash('Dados editados com sucesso!!!')
        return redirect('/funcionarios')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/funcionarios')





