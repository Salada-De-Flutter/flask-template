from flask import Flask
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def get_db():
    return psycopg2.connect(os.getenv('DATABASE_URL'))

try:
    conn = get_db()
    print('Database conectou')
    conn.close()
except:
    print('Erro na conexão com o database')

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)