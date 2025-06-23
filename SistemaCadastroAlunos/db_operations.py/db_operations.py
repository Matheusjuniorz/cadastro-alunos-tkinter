import sqlite3

# Função para conectar ao banco de dados
def conectar_bd():
    conn = sqlite3.connect('escola.db')
    return conn

# --- Funções para Alunos ---
def criar_tabela_alunos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT,
            telefone TEXT,
            sexo TEXT,
            imagem TEXT,
            data_nascimento TEXT,
            cpf TEXT,
            turma TEXT
        )
    ''')
    conn.commit()
    conn.close()

def criar_alunos(dados):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", dados)
    conn.commit()
    conn.close()

def ver_alunos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conn.close()
    return alunos

def atualizar_aluno(dados):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("UPDATE alunos SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, turma=? WHERE id=?", dados)
    conn.commit()
    conn.close()

def deletar_aluno(aluno_id):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE id=?", (aluno_id,))
    conn.commit()
    conn.close()

# --- Funções para Cursos ---
def criar_tabela_cursos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            duracao TEXT,
            preco REAL
        )
    ''')
    conn.commit()
    conn.close()

def criar_cursos(dados):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cursos (nome, duracao, preco) VALUES (?, ?, ?)", dados)
    conn.commit()
    conn.close()

def ver_cursos():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cursos")
    cursos = cursor.fetchall()
    conn.close()
    return cursos

def atualizar_cursos(dados):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("UPDATE cursos SET nome=?, duracao=?, preco=? WHERE id=?", dados)
    conn.commit()
    conn.close()

def deletar_cursos(curso_id):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cursos WHERE id=?", (curso_id,))
    conn.commit()
    conn.close()

# --- Funções para Turmas ---
def criar_tabela_turmas():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_turma TEXT NOT NULL,
            curso_associado TEXT,
            data_inicio TEXT
        )
    ''')
    conn.commit()
    conn.close()

def criar_turma(dados):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO turmas (nome_turma, curso_associado, data_inicio) VALUES (?, ?, ?)", dados)
    conn.commit()
    conn.close()

def ver_turmas():
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM turmas")
    turmas = cursor.fetchall()
    conn.close()
    return turmas

def atualizar_turma(dados):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("UPDATE turmas SET nome_turma=?, curso_associado=?, data_inicio=? WHERE id=?", dados)
    conn.commit()
    conn.close()

def deletar_turma(turma_id):
    conn = conectar_bd()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM turmas WHERE id=?", (turma_id,))
    conn.commit()
    conn.close()

# Chamadas iniciais para criar as tabelas se elas não existirem
criar_tabela_alunos()
criar_tabela_cursos()
criar_tabela_turmas()