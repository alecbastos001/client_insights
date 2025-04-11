import sqlite3
from app.models import ClientePerfil

DB_PATH = "clientes.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
        nome TEXT,
        telefone TEXT,
        nome_completo TEXT,
        profissao TEXT,
        redes_sociais TEXT,
        interesses TEXT,
        mencoes TEXT,
        imagens TEXT,
        inferencias TEXT
    )''')
    conn.commit()
    conn.close()

def insert_cliente(perfil: ClientePerfil):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (
        perfil.nome,
        perfil.telefone,
        perfil.nome_completo,
        perfil.profissao,
        str(perfil.redes_sociais),
        str(perfil.interesses),
        str(perfil.mencoes),
        str(perfil.imagens),
        str(perfil.inferencias)
    ))
    conn.commit()
    conn.close()
