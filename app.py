from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
database_url = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
db = SQLAlchemy(app)
import uuid

try:
    with app.app_context():
        db.engine.connect()
        print("DATABASE CONECTADO")
except Exception as e:
    print(f"DATABASE NÃO CONECTADO: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mandar', methods=['POST'])
def mandar():
    nome = request.form['nome']
    senha = request.form['senha']
    novo_user = Users(nome = nome, senha = senha, id = uuid.uuid4())
    db.session.add(novo_user)
    db.session.commit
    try:
        return render_template('login.html')
    except Exception as e:
        return f"Usuario não adiconado: {e}"
    
@app.route('/login', methods=['POST'])
def logar():
    nome = request.form['nome']
    senha = request.form['senha']
    usuario = Users.query.filter_by(nome=nome).first()
    if senha == usuario.senha and nome == usuario.nome:
        return f"id do usuario: {usuario.id}"
    else:
        return "Usuario não encontrado"
        
class Users(db.Model):
    __tablename__ = 'teste2'
    id = db.Column(db.Text, primary_key=True, not_null=True)
    nome = db.Column(db.Text)
    senha = db.Column(db.Text)

if __name__ == '__main__':
    app.run(debug=True)