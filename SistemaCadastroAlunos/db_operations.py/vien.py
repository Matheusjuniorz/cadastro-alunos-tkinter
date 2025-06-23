#Importando SQLite3

import sqlite3 as lite

#Criando conxão

try:
    con = lite.connect('cadastro_alunos.db')
    print('Conexao com o banco de dados realizado com sucesso!')
    
except sqlite3.Error as e:
    print("Error ao concetar com o banco de dados:")

#Tabela de Cursos ----------------------------------------

#Criar Cursos (CREATE C )

def criar_cursos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Cursos (nome, duracao, preco) VALUES (?, ?, ?)"
        cur.execute(query, i)


#criar_cursos(['Python', 'Semanas', 50])

# Ver todos os cursos ( Read R)

def ver_cursos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Cursos')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista

print(ver_cursos())

#Atualizar os Cursos (Update U) 

def atualizar_cursos(l):
    with con:
        cur = con.cursor()
        query = "UPDATE Cursos SET nome=?, duracao=?, preco=? WHERE id=?"
        cur.executemany(query, l)

l = [('Python', 'Duas Semanas', 50.0, 1)]

# Deletar os Cursos (Upedate U)

def deletar_cursos(id):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Cursos WHERE id=?"
        cur.execute(query, (id,))

#deletar_cursos(1)


#Tabela de Turmas ----------------------------------------

# Criar turmas( Inserir )

def criar_turma(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Turmas (nome, cursos_nome, data_inicio) VALUES (?, ?, ?)"
        cur.execute(query, (i))

# Ver todas as turmas ( Read R)

def ver_turmas():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Turmas')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista

#Atualizar as Turmas(Update U) 

def atualizar_turma(l):
    with con:
        cur = con.cursor()
        query = "UPDATE Turma SET nome=?, cursos_nome=?, data_inicio=? WHERE id=?"
        cur.executemany(query, i)


# Deletar Turma (Upedate U)

def deletar_turma(id):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Turmas WHERE id=?"
        cur.execute(query, (id,))

#Tabela Alunos ----------------------------------------

# Criar Alunos( Inserir )

def criar_alunos(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Alunos (nome, email, telefone, sexo, imagem, data_nascimento, cpf, turma_nome) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, (i))

# Ver Alunos ( Read R)

def ver_alunos():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Alunos')
        linha = cur.fetchall()
        
        for i in linha:
            lista.append(i)
    return lista

#Atualizar Alunos(Update U) 

def atualizar_aluno(l):
    with con:
        cur = con.cursor()
        query = "UPDATE Turma SET nome=?, email=?, telefone=?, sexo=?, imagem=?, data_nascimento=?, cpf=?, turma_nome=? WHERE id=?"
        cur.executemany(query, i)

# Deletar Aluno (Delete D   )

def deletar_aluno(id):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Alunos WHERE id=?"
        cur.execute(query, (id,))

