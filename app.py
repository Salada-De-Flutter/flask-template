from flask import Flask, render_template, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os

load_dotenv()

database_url = os.getenv('DATABASE_URL')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
db = SQLAlchemy(app)

try:
    with app.app_context():
        db.engine.connect
        print("Banco de dados conectado")
except Exception as e:
    print(f"Algo deu errado {e}")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/mandar', methods = ['POST'])
def mandar():
    usuario = request.form['usuario']
    senha = request.form['senha']
    novo_user = Usuario(senha = senha, usuario = usuario)
    return f'O usuario é: {usuario} e a senha é {senha}'

class Usuario(db.Model):
    __tablename__ = 'teste'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    senha = db.Column(db.Text)

if __name__ == '__main__':
    app.run(debug=True)