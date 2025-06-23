# 🎓 Sistema de Cadastro de Alunos com Tkinter

> Um sistema completo de gestão de alunos, cursos e turmas com interface gráfica feita em Python utilizando **Tkinter**.

---

## 📌 Funcionalidades

✅ Cadastro de alunos com:
- Nome, email, telefone, CPF, data de nascimento, sexo  
- Seleção de turma  
- Upload de foto do aluno  

✅ Gestão de cursos:
- Nome, duração e valor  
- Visualização em tabela  

✅ Gestão de turmas:
- Nome da turma  
- Vinculação com curso  
- Data de início  

✅ Tabelas com scrollbar e colunas bem definidas  
✅ Separadores visuais e layout intuitivo  
✅ Código modular com separação em arquivos `.py`

---

## 🛠 Tecnologias utilizadas

| Ferramenta   | Descrição                                |
|--------------|--------------------------------------------|
| 🐍 Python     | Linguagem principal                        |
| 🖼 Tkinter    | Interface gráfica (GUI)                   |
| 📅 tkcalendar | Seleção de datas (DateEntry)             |
| 🖼 Pillow     | Manipulação de imagens (foto do aluno)    |

---

## 📂 Estrutura do Projeto

cadastro-alunos-tkinter/
├── cridb/
│ ├── logo.py.png
│ ├── add.py.png
│ ├── delete.py.png
│ ├── save.py.png
│ └── screenshot.png # captura de tela do sistema
├── db_operations.py # lógica de banco de dados
├── main.py # inicializa a interface Tkinter
├── vien.py # funções auxiliares
├── .gitignore
└── README.md


---

## 🚀 Como executar

```bash
# Criar ambiente virtual (opcional)
python -m venv venv
venv\Scripts\activate

# Instalar dependências
pip install tkcalendar pillow

# Executar o sistema
python main.py

👨‍💻 Autor
Matheus Junior Batista de Lara Pinho
📧 batistam032@gmail.com
📍 Cuiabá - MT
🎓 Engenharia de Software - Faculdade Anhanguera

📝 Licença
Este projeto está sob a licença MIT.
Sinta-se livre para usar, estudar e modificar.

💡 Contribuição
Fique à vontade para enviar sugestões ou melhorias!
Pull requests são bem-vindos
