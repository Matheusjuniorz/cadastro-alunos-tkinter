# Importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# Importando o Pillow
from PIL import Image, ImageTk

# tk calendar
from tkcalendar import Calendar, DateEntry
from datetime import date

# Importando as funções do banco de dados
import db_operations as db # Assegure-se que o arquivo db_operations.py está no mesmo diretório

# Cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca
co2 = "#e5e5e5"  # Grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"  # Letra
co6 = "#003452"  # Azul
co7 = "#ef5350"  # Vermelho

co8 = "#038cfc"  # Azul
co9 = "#263238"  # + Verde
co10 = "#e9edf5"  # + Verde

class StudentManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gestão de Alunos")
        self.master.geometry('850x620')
        self.master.configure(background=co1)
        self.master.resizable(width=FALSE, height=FALSE)

        self.style = Style(self.master)
        self.style.theme_use("clam")

        # --- Criando Frames ---
        self.frame_logo = Frame(self.master, width=850, height=52, bg=co6)
        self.frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

        ttk.Separator(self.master, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

        self.frame_dados = Frame(self.master, width=850, height=65, bg=co1)
        self.frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

        ttk.Separator(self.master, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

        self.frame_detalhes = Frame(self.master, width=850, height=200, bg=co1)
        self.frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

        self.frame_tabela = Frame(self.master, width=850, height=200, bg=co1)
        self.frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

        self.setup_logo()
        self.setup_navigation_buttons()

        # --- Carregando dados do banco de dados ---
        self.dados_alunos = db.ver_alunos()
        self.dados_cursos = db.ver_cursos()
        self.dados_turmas = db.ver_turmas()

        # Variáveis para armazenar a imagem e seu caminho
        self.current_image = None
        self.current_image_path = "sem_imagem.png" # Inicializa com o caminho padrão

        # Inicia na tela de Cadastro
        self.control("cadastro")

    def setup_logo(self):
        """Configura a imagem e o texto do logo no frame_logo."""
        try:
            logo_imagem = Image.open('logo.py.png')
            logo_imagem = logo_imagem.resize((50, 50))
            self.logo_photo = ImageTk.PhotoImage(logo_imagem) # Store as instance attribute
            self.app_logo = Label(self.frame_logo, image=self.logo_photo, text="Cadastro de Aluno", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy', 15, 'bold'), bg=co6, fg=co1)
            self.app_logo.place(x=0, y=0)
        except FileNotFoundError:
            self.app_logo = Label(self.frame_logo, text="Cadastro de Aluno", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy', 15, 'bold'), bg=co6, fg=co1)
            self.app_logo.place(x=0, y=0)
            print("Aviso: 'logo.py.png' não encontrada. Exibindo apenas o texto.")

    def setup_navigation_buttons(self):
        """Configura os botões de navegação no frame_dados."""
        # Tenta carregar as imagens para os botões de navegação
        try:
            self.app_img_cadastro = ImageTk.PhotoImage(Image.open('add.py.png').resize((18, 18)))
        except FileNotFoundError:
            self.app_img_cadastro = None
            print("Aviso: 'add.py.png' não encontrada para o botão de cadastro.")

        try:
            self.app_img_adicionar = ImageTk.PhotoImage(Image.open('add.py.png').resize((18, 18)))
        except FileNotFoundError:
            self.app_img_adicionar = None
            print("Aviso: 'add.py.png' não encontrada para o botão de adicionar.")

        try:
            self.app_img_salvar = ImageTk.PhotoImage(Image.open('save.py.png').resize((18, 18)))
        except FileNotFoundError:
            self.app_img_salvar = None
            print("Aviso: 'save.py.png' não encontrada para o botão de salvar.")

        # Cria os botões e associa as imagens
        Button(self.frame_dados, command=lambda: self.control("cadastro"), image=self.app_img_cadastro, text="Cadastro", width=100, compound=LEFT, overrelief=RAISED, font=('Ivy', 11), bg=co1, fg=co0).place(x=10, y=30)
        Button(self.frame_dados, command=lambda: self.control("adicionar"), image=self.app_img_adicionar, text="Adicionar", width=100, compound=LEFT, overrelief=RAISED, font=('Ivy', 11), bg=co1, fg=co0).place(x=123, y=30)
        Button(self.frame_dados, command=lambda: self.control("salvar"), image=self.app_img_salvar, text="Salvar", width=100, compound=LEFT, overrelief=RAISED, font=('Ivy', 11), bg=co1, fg=co0).place(x=236, y=30)

    def escolher_imagem(self):
        """Permite ao usuário selecionar uma imagem e exibe-a no frame de detalhes."""
        imagem_string = fd.askopenfilename(
            title="Selecionar Imagem",
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.gif")]
        )

        if imagem_string:
            app_imagem = Image.open(imagem_string)
            app_imagem = app_imagem.resize((130, 130))
            self.current_image_path = imagem_string # Guarda o caminho da imagem aqui
            self.current_image = ImageTk.PhotoImage(app_imagem)  # Store as instance attribute

            # Clear previous image label if exists
            for widget in self.frame_detalhes.winfo_children():
                if isinstance(widget, Label) and widget.winfo_x() == 300 and widget.winfo_y() == 10:
                    widget.destroy()

            l_imagem = Label(self.frame_detalhes, image=self.current_image, bg=co6)
            l_imagem.place(x=300, y=10)

    def salvar_aluno(self):
        """Salva um novo aluno no banco de dados."""
        nome = self.e_nome.get()
        email = self.e_email.get()
        tel = self.e_tel.get()
        sexo = self.c_sexo.get()
        data_nascimento = self.cal_nascimento.get_date().strftime("%d/%m/%Y")
        cpf = self.e_cpf.get()
        turma = self.c_turma.get()
        imagem_path = self.current_image_path # Pega o caminho da imagem salvo na variável

        lista = [nome, email, tel, sexo, imagem_path, data_nascimento, cpf, turma]

        for item in lista:
            if item == "" or item is None: # Adicionado 'is None' para combobox vazia
                messagebox.showerror('Erro', 'Preencha todos os campos obrigatórios (*).')
                return

        try:
            # Chama a função do banco de dados para criar o aluno
            db.criar_alunos(tuple(lista))
            messagebox.showinfo('Sucesso', 'Aluno cadastrado com sucesso!')
            self.clear_student_fields()
            self.dados_alunos = db.ver_alunos() # Recarrega os dados da tabela
            self.mostrar_alunos()  # Atualiza a tabela
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao cadastrar aluno: {e}')

    def atualizar_aluno(self):
        """Atualiza os dados de um aluno selecionado no banco de dados."""
        selected_item = self.tree_aluno.selection()
        if not selected_item:
            messagebox.showerror('Erro', 'Selecione um aluno para atualizar.')
            return

        item_values = self.tree_aluno.item(selected_item)['values']
        aluno_id = item_values[0] # O ID é o primeiro valor

        nome = self.e_nome.get()
        email = self.e_email.get()
        tel = self.e_tel.get()
        sexo = self.c_sexo.get()
        data_nascimento = self.cal_nascimento.get_date().strftime("%d/%m/%Y")
        cpf = self.e_cpf.get()
        turma = self.c_turma.get()
        imagem_path = self.current_image_path # Pega o caminho da imagem salvo na variável

        lista = [nome, email, tel, sexo, imagem_path, data_nascimento, cpf, turma, aluno_id]

        for item in lista[:-1]: # Exclui o ID da checagem
            if item == "" or item is None:
                messagebox.showerror('Erro', 'Preencha todos os campos obrigatórios (*).')
                return

        try:
            # Chama a função do banco de dados para atualizar o aluno
            db.atualizar_aluno(tuple(lista))
            messagebox.showinfo('Sucesso', 'Aluno atualizado com sucesso!')
            self.clear_student_fields()
            self.dados_alunos = db.ver_alunos() # Recarrega os dados da tabela
            self.mostrar_alunos()
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao atualizar aluno: {e}')

    def deletar_aluno(self):
        """Deleta um aluno selecionado do banco de dados."""
        selected_item = self.tree_aluno.selection()
        if not selected_item:
            messagebox.showerror('Erro', 'Selecione um aluno para deletar.')
            return

        resposta = messagebox.askyesno('Confirmar', 'Tem certeza que deseja deletar este aluno?')
        if not resposta:
            return

        item_values = self.tree_aluno.item(selected_item)['values']
        aluno_id = item_values[0]

        try:
            # Chama a função do banco de dados para deletar o aluno
            db.deletar_aluno(aluno_id)
            messagebox.showinfo('Sucesso', 'Aluno deletado com sucesso!')
            self.clear_student_fields()
            self.dados_alunos = db.ver_alunos() # Recarrega os dados da tabela
            self.mostrar_alunos()
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao deletar aluno: {e}')

    def selecionar_aluno_para_edicao(self, event):
        """Preenche os campos do formulário do aluno com os dados do aluno selecionado na Treeview."""
        selected_item = self.tree_aluno.selection()
        if not selected_item:
            return

        item_values = self.tree_aluno.item(selected_item)['values']

        self.clear_student_fields()

        self.e_nome.insert(0, item_values[1])
        self.e_email.insert(0, item_values[2])
        self.e_tel.insert(0, item_values[3])
        self.c_sexo.set(item_values[4])
        # Data de nascimento: item_values[6] está em string, precisa converter para objeto date
        try:
            day, month, year = map(int, item_values[6].split('/'))
            self.cal_nascimento.set_date(date(year, month, day))
        except ValueError:
            pass # Keep current date or set to today if invalid
        self.e_cpf.insert(0, item_values[7])
        self.c_turma.set(item_values[8])

        # Lógica para carregar a imagem do aluno
        imagem_path = item_values[5]
        if imagem_path and imagem_path != "sem_imagem.png":
            try:
                app_imagem = Image.open(imagem_path)
                app_imagem = app_imagem.resize((130, 130))
                self.current_image = ImageTk.PhotoImage(app_imagem)
                self.current_image_path = imagem_path # Salva o caminho da imagem
                l_imagem = Label(self.frame_detalhes, image=self.current_image, bg=co6)
                l_imagem.place(x=300, y=10)
            except FileNotFoundError:
                print(f"Imagem {imagem_path} não encontrada para o aluno.")
                self.current_image = None
                self.current_image_path = "sem_imagem.png"


    def clear_student_fields(self):
        """Limpa todos os campos de entrada do formulário de aluno."""
        self.e_nome.delete(0, END)
        self.e_email.delete(0, END)
        self.e_tel.delete(0, END)
        self.c_sexo.set('')
        self.cal_nascimento.set_date(date.today())  # Resetar a data para o dia atual
        self.e_cpf.delete(0, END)
        self.c_turma.set('')
        # Remove a imagem exibida, se houver
        for widget in self.frame_detalhes.winfo_children():
            if isinstance(widget, Label) and widget.winfo_x() == 300 and widget.winfo_y() == 10:
                widget.destroy()
        self.current_image = None # Limpa a referência da imagem
        self.current_image_path = "sem_imagem.png" # Reseta o caminho da imagem

    def novo_curso(self):
        """Salva um novo curso no banco de dados."""
        nome = self.e_nome_curso.get()
        duracao = self.e_duracao_curso.get()
        preco = self.e_preco_curso.get()

        if nome == "" or duracao == "" or preco == "":
            messagebox.showerror('Erro', 'Preencha todos os campos para o curso.')
            return

        try:
            # Chama a função do banco de dados para criar o curso
            db.criar_cursos((nome, duracao, float(preco))) # Preço como float
            messagebox.showinfo('Sucesso', 'Curso inserido com sucesso!')
            self.clear_course_fields()
            self.dados_cursos = db.ver_cursos() # Recarrega os dados da tabela
            self.mostrar_cursos(self.frame_tabela_curso_sub)  # Atualiza a tabela de cursos
            self.cursos_disponiveis_update() # Atualiza a combobox de cursos para turmas
        except ValueError:
            messagebox.showerror('Erro', 'O preço deve ser um número válido.')
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao inserir curso: {e}')


    def atualizar_curso(self):
        """Atualiza os dados de um curso selecionado no banco de dados."""
        selected_item = self.tree_curso.selection()
        if not selected_item:
            messagebox.showerror('Erro', 'Selecione um curso para atualizar.')
            return

        item_values = self.tree_curso.item(selected_item)['values']
        curso_id = item_values[0]

        nome = self.e_nome_curso.get()
        duracao = self.e_duracao_curso.get()
        preco = self.e_preco_curso.get()

        if nome == "" or duracao == "" or preco == "":
            messagebox.showerror('Erro', 'Preencha todos os campos para atualizar o curso.')
            return

        try:
            # Chama a função do banco de dados para atualizar o curso
            db.atualizar_cursos((nome, duracao, float(preco), curso_id))
            messagebox.showinfo('Sucesso', 'Curso atualizado com sucesso!')
            self.clear_course_fields()
            self.dados_cursos = db.ver_cursos() # Recarrega os dados da tabela
            self.mostrar_cursos(self.frame_tabela_curso_sub)  # Atualiza a tabela
            self.cursos_disponiveis_update() # Atualiza as turmas para a combobox 'curso'
        except ValueError:
            messagebox.showerror('Erro', 'O preço deve ser um número válido.')
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao atualizar curso: {e}')

    def deletar_curso(self):
        """Deleta um curso selecionado do banco de dados."""
        selected_item = self.tree_curso.selection()
        if not selected_item:
            messagebox.showerror('Erro', 'Selecione um curso para deletar.')
            return

        resposta = messagebox.askyesno('Confirmar', 'Tem certeza que deseja deletar este curso? Isso pode afetar as turmas associadas.')
        if not resposta:
            return

        item_values = self.tree_curso.item(selected_item)['values']
        curso_id = item_values[0]

        try:
            # Chama a função do banco de dados para deletar o curso
            db.deletar_cursos(curso_id)
            messagebox.showinfo('Sucesso', 'Curso deletado com sucesso!')
            self.clear_course_fields()
            self.dados_cursos = db.ver_cursos() # Recarrega os dados da tabela
            self.mostrar_cursos(self.frame_tabela_curso_sub)  # Atualiza a tabela
            self.cursos_disponiveis_update()  # Atualiza as turmas para a combobox 'curso' (importante se cursos deletados afetam turmas)
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao deletar curso: {e}')

    def selecionar_curso_para_edicao(self, event):
        """Preenche os campos do formulário do curso com os dados do curso selecionado na Treeview."""
        selected_item = self.tree_curso.selection()
        if not selected_item:
            return

        item_values = self.tree_curso.item(selected_item)['values']

        self.clear_course_fields()

        self.e_nome_curso.insert(0, item_values[1])  # Nome do Curso
        self.e_duracao_curso.insert(0, item_values[2])  # Duração
        self.e_preco_curso.insert(0, str(item_values[3]))  # Preço

    def clear_course_fields(self):
        """Limpa todos os campos de entrada do formulário de curso."""
        self.e_nome_curso.delete(0, END)
        self.e_duracao_curso.delete(0, END)
        self.e_preco_curso.delete(0, END)

    def cursos_disponiveis_update(self):
        """Atualiza os valores do combobox de cursos disponíveis para a criação de turmas."""
        # Recarrega os dados dos cursos do banco de dados
        self.dados_cursos = db.ver_cursos()
        cursos_disponiveis = [curso[1] for curso in self.dados_cursos] # Pega apenas o nome do curso
        
        # Verifica se o combobox 'c_curso' foi criado e está acessível
        if hasattr(self, 'c_curso') and self.c_curso.winfo_exists():
            self.c_curso['values'] = tuple(cursos_disponiveis)
            # Limpa a seleção atual se o valor não estiver mais disponível
            if self.c_curso.get() not in cursos_disponiveis:
                self.c_curso.set('')

    def turmas_disponiveis_update(self):
        """Atualiza os valores do combobox de turmas disponíveis para o cadastro de alunos."""
        # Recarrega os dados das turmas do banco de dados
        self.dados_turmas = db.ver_turmas()
        turmas_disponiveis = [turma[1] for turma in self.dados_turmas] # Pega apenas o nome da turma
        
        # Verifica se o combobox 'c_turma' foi criado e está acessível
        if hasattr(self, 'c_turma') and self.c_turma.winfo_exists():
            self.c_turma['values'] = tuple(turmas_disponiveis)
            # Limpa a seleção atual se o valor não estiver mais disponível
            if self.c_turma.get() not in turmas_disponiveis:
                self.c_turma.set('')

    def nova_turma(self):
        """Salva uma nova turma no banco de dados."""
        nome_turma = self.e_nome_turma.get()
        curso_selecionado = self.c_curso.get()
        data_inicio = self.cal_data_inicio.get_date().strftime("%d/%m/%Y")

        if nome_turma == "" or curso_selecionado == "" or data_inicio == "":
            messagebox.showerror('Erro', 'Preencha todos os campos para a turma.')
            return

        try:
            # Chama a função do banco de dados para criar a turma
            db.criar_turma((nome_turma, curso_selecionado, data_inicio))
            messagebox.showinfo('Sucesso', 'Turma inserida com sucesso!')
            self.clear_class_fields()
            self.dados_turmas = db.ver_turmas() # Recarrega os dados da tabela
            self.mostrar_turmas(self.frame_tabela_turma_sub)  # Atualiza a tabela de turmas
            self.turmas_disponiveis_update()  # Atualiza a combobox de turmas na tela de alunos
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao inserir turma: {e}')


    def atualizar_turma(self):
        """Atualiza os dados de uma turma selecionada no banco de dados."""
        selected_item = self.tree_turma.selection()
        if not selected_item:
            messagebox.showerror('Erro', 'Selecione uma turma para atualizar.')
            return

        item_values = self.tree_turma.item(selected_item)['values']
        turma_id = item_values[0]

        nome_turma = self.e_nome_turma.get()
        curso_selecionado = self.c_curso.get()
        data_inicio = self.cal_data_inicio.get_date().strftime("%d/%m/%Y")

        if nome_turma == "" or curso_selecionado == "" or data_inicio == "":
            messagebox.showerror('Erro', 'Preencha todos os campos para atualizar a turma.')
            return

        try:
            # Chama a função do banco de dados para atualizar a turma
            db.atualizar_turma((nome_turma, curso_selecionado, data_inicio, turma_id))
            messagebox.showinfo('Sucesso', 'Turma atualizada com sucesso!')
            self.clear_class_fields()
            self.dados_turmas = db.ver_turmas() # Recarrega os dados da tabela
            self.mostrar_turmas(self.frame_tabela_turma_sub)
            self.turmas_disponiveis_update()
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao atualizar turma: {e}')

    def deletar_turma(self):
        """Deleta uma turma selecionada do banco de dados."""
        selected_item = self.tree_turma.selection()
        if not selected_item:
            messagebox.showerror('Erro', 'Selecione uma turma para deletar.')
            return

        resposta = messagebox.askyesno('Confirmar', 'Tem certeza que deseja deletar esta turma?')
        if not resposta:
            return

        item_values = self.tree_turma.item(selected_item)['values']
        turma_id = item_values[0]

        try:
            # Chama a função do banco de dados para deletar a turma
            db.deletar_turma(turma_id)
            messagebox.showinfo('Sucesso', 'Turma deletada com sucesso!')
            self.clear_class_fields()
            self.dados_turmas = db.ver_turmas() # Recarrega os dados da tabela
            self.mostrar_turmas(self.frame_tabela_turma_sub)
            self.turmas_disponiveis_update()
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao deletar turma: {e}')

    def selecionar_turma_para_edicao(self, event):
        """Preenche os campos do formulário da turma com os dados da turma selecionada na Treeview."""
        selected_item = self.tree_turma.selection()
        if not selected_item:
            return

        item_values = self.tree_turma.item(selected_item)['values']

        self.clear_class_fields()

        self.e_nome_turma.insert(0, item_values[1])
        self.c_curso.set(item_values[2])
        try:
            day, month, year = map(int, item_values[3].split('/'))
            self.cal_data_inicio.set_date(date(year, month, day))
        except ValueError:
            pass # Keep current date or set to today if invalid

    def clear_class_fields(self):
        """Limpa todos os campos de entrada do formulário de turma."""
        self.e_nome_turma.delete(0, END)
        self.c_curso.set('')
        self.cal_data_inicio.set_date(date.today())

    def alunos(self):
        """Cria e exibe a interface para cadastro de alunos."""
        # Criando campos de entrada
        l_nome = Label(self.frame_detalhes, text="Nome *", height=1, anchor=NW, font=('lvy', 10), bg=co1, fg=co4)
        l_nome.place(x=4, y=10)
        self.e_nome = Entry(self.frame_detalhes, width=45, justify='left', relief='solid')
        self.e_nome.place(x=7, y=40)

        l_email = Label(self.frame_detalhes, text="Email *", height=1, anchor=NW, font=('lvy', 10), bg=co1, fg=co4)
        l_email.place(x=4, y=70)
        self.e_email = Entry(self.frame_detalhes, width=45, justify='left', relief='solid')
        self.e_email.place(x=7, y=100)

        l_tel = Label(self.frame_detalhes, text="Telefone *", height=1, anchor=NW, font=('lvy', 10), bg=co1, fg=co4)
        l_tel.place(x=4, y=130)
        self.e_tel = Entry(self.frame_detalhes, width=20, justify='left', relief='solid')
        self.e_tel.place(x=7, y=160)

        # Selecao de sexo
        l_sexo = Label(self.frame_detalhes, text="Sexo *", height=1, anchor=NW, font=('lvy', 10), bg=co1, fg=co4)
        l_sexo.place(x=190, y=130)
        self.c_sexo = ttk.Combobox(self.frame_detalhes, width=12, font=('lvy', 8, 'bold'))
        self.c_sexo['values'] = ('Masculino', 'Feminino', 'Outro') # Adicionado 'Outro'
        self.c_sexo.place(x=190, y=160)

        l_data_nascimento = Label(self.frame_detalhes, text="Data de nascimento", height=1, anchor=NW, font=('lvy', 10), bg=co1, fg=co4)
        l_data_nascimento.place(x=446, y=10)
        self.cal_nascimento = DateEntry(self.frame_detalhes, width=18, background='darkblue', foreground='white', borderwidth=2, year=date.today().year, locale='pt_BR')
        self.cal_nascimento.place(x=450, y=40)

        l_cpf = Label(self.frame_detalhes, text="CPF *", height=1, anchor=NW, font=('lvy', 10), bg=co1, fg=co4)
        l_cpf.place(x=446, y=70)
        self.e_cpf = Entry(self.frame_detalhes, width=20, justify='left', relief='solid')
        self.e_cpf.place(x=450, y=100)

        # Pegando as Turmas disponíveis
        self.turmas_disponiveis = [turma[1] for turma in self.dados_turmas]

        l_turma = Label(self.frame_detalhes, text="Turma *", height=1, anchor=NW, font=('lvy', 10), bg=co1, fg=co4)
        l_turma.place(x=446, y=130)
        self.c_turma = ttk.Combobox(self.frame_detalhes, width=20, font=('lvy', 8, 'bold'))
        self.c_turma['values'] = tuple(self.turmas_disponiveis) # Garantir que os valores sejam um tuple
        self.c_turma.place(x=450, y=160)
        self.turmas_disponiveis_update() # Chama a atualização após criar o combobox

        # Botao para escolher imagem
        Button(self.frame_detalhes, command=self.escolher_imagem, text="Carregar Foto", width=20, anchor=CENTER, compound=CENTER, overrelief=RAISED, font=('Ivy', 7), bg=co1, fg=co0).place(x=300, y=160)

        # Linha separadora
        Label(self.frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('lvy', 1), bg=co0, fg=co0).place(x=610, y=10)
        Label(self.frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('lvy', 1), bg=co1, fg=co0).place(x=608, y=10)

        # Procurar aluno
        Label(self.frame_detalhes, text="Procurar Aluno [Entra o nome]", height=1, anchor=NW, font=('lvy', 10), bg=co1, fg=co4).place(x=627, y=10)
        self.e_nome_pesquisa = Entry(self.frame_detalhes, width=17, justify='center', relief='solid', font=('ivy', 10))
        self.e_nome_pesquisa.place(x=630, y=35)

        # Atualiza o botão de procurar para chamar o novo método
        Button(self.frame_detalhes, command=self.procurar_aluno, anchor=CENTER, text="Procurar", height=1, overrelief=RIDGE, font=('lvy', 7, 'bold'), bg=co1, fg=co0).place(x=757, y=35)

        # Botoes de acao (Salvar, Atualizar, Deletar, Ver)
        Button(self.frame_detalhes, command=self.salvar_aluno, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy', 7, 'bold'), bg=co3, fg=co1).place(x=627, y=110)
        Button(self.frame_detalhes, command=self.atualizar_aluno, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy', 7, 'bold'), bg=co6, fg=co1).place(x=627, y=135)
        Button(self.frame_detalhes, command=self.deletar_aluno, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy', 7, 'bold'), bg=co7, fg=co1).place(x=627, y=160)
        # Atualiza o botão 'Ver' para chamar o novo método
        Button(self.frame_detalhes, command=self.ver_aluno, text='Ver'.upper(), width=10, overrelief=RIDGE, font=('Ivy', 7, 'bold'), bg=co1, fg=co0).place(x=727, y=160)

        self.mostrar_alunos()  # Chama a função para exibir a tabela de alunos

    def adicionar(self):
        """Cria e exibe a interface para adicionar cursos e turmas."""
        # Limpa o frame_detalhes e frame_tabela antes de criar os sub-frames
        for widget in self.frame_detalhes.winfo_children():
            widget.destroy()
        for widget in self.frame_tabela.winfo_children():
            widget.destroy()

        # Criando frames para tabelas
        self.frame_tabela_curso_sub = Frame(self.frame_tabela, width=300, height=200, bg=co1)
        self.frame_tabela_curso_sub.grid(row=0, column=0, pady=0, padx=10, sticky=NSEW)

        self.frame_tabela_linha_sub = Frame(self.frame_tabela, width=30, height=200, bg=co1)
        self.frame_tabela_linha_sub.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)

        self.frame_tabela_turma_sub = Frame(self.frame_tabela, width=300, height=200, bg=co1)
        self.frame_tabela_turma_sub.grid(row=0, column=2, pady=0, padx=0, sticky=NSEW)

        # Detalhes do Curso
        Label(self.frame_detalhes, text="Nome do curso *", height=1, anchor=NW, font=('lvy', 10), bg=co1, fg=co4).place(x=4, y=10)
        self.e_nome_curso = Entry(self.frame_detalhes, width=35, justify='left', relief='solid')
        self.e_nome_curso.place(x=7, y=40)

        Label(self.frame_detalhes, text="Duração *", height=1, anchor=NW, font=('lvy', 10), bg=co1, fg=co4).place(x=4, y=70)
        self.e_duracao_curso = Entry(self.frame_detalhes, width=20, justify='left', relief='solid')
        self.e_duracao_curso.place(x=7, y=100)

        Label(self.frame_detalhes, text="Preço *", height=1, anchor=NW, font=('lvy', 10), bg=co1, fg=co4).place(x=4, y=130)
        self.e_preco_curso = Entry(self.frame_detalhes, width=10, justify='left', relief='solid')
        self.e_preco_curso.place(x=7, y=160)

        # Botões para Curso (Salvar, Atualizar, Deletar)
        Button(self.frame_detalhes, command=self.novo_curso, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy', 7, 'bold'), bg=co3, fg=co1).place(x=107, y=160)
        Button(self.frame_detalhes, command=self.atualizar_curso, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy', 7, 'bold'), bg=co6, fg=co1).place(x=197, y=160)
        Button(self.frame_detalhes, command=self.deletar_curso, anchor=CENTER, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy', 7, 'bold'), bg=co7, fg=co1).place(x=287, y=160)

        # Linha separadora do meio
        Label(self.frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('lvy', 1), bg=co0, fg=co0).place(x=374, y=10)
        Label(self.frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('lvy', 1), bg=co1, fg=co0).place(x=372, y=10)

        # Linha separadora da tabela
        Label(self.frame_tabela_linha_sub, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('lvy', 1), bg=co0, fg=co0).place(x=6, y=10)
        Label(self.frame_tabela_linha_sub, relief=GROOVE, text='h', width=1, height=140, anchor=NW, font=('lvy', 1), bg=co1, fg=co0).place(x=4, y=10)

        # Detalhes da Turma
        Label(self.frame_detalhes, text="Nome da Turma *", height=1, anchor=NW, font=('lvy', 10), bg=co1, fg=co4).place(x=404, y=10)
        self.e_nome_turma = Entry(self.frame_detalhes, width=35, justify='left', relief='solid')
        self.e_nome_turma.place(x=407, y=40)

        Label(self.frame_detalhes, text="Curso *", height=1, anchor=NW, font=('lvy', 10), bg=co1, fg=co4).place(x=404, y=70)

        # Pegando os cursos disponíveis para a combobox da turma
        self.cursos_disponiveis = [curso[1] for curso in self.dados_cursos]
        self.c_curso = ttk.Combobox(self.frame_detalhes, width=20, font=('lvy', 8, 'bold'))
        self.c_curso['values'] = tuple(self.cursos_disponiveis) # Garantir que os valores sejam um tuple
        self.c_curso.place(x=407, y=100)
        self.cursos_disponiveis_update() # Chama a atualização após criar o combobox

        Label(self.frame_detalhes, text="Data de inicio *", height=1, anchor=NW, font=('lvy', 10), bg=co1, fg=co4).place(x=406, y=130)
        self.cal_data_inicio = DateEntry(self.frame_detalhes, width=10, background='darkblue', foreground='white', borderwidth=2, year=date.today().year, locale='pt_BR')
        self.cal_data_inicio.place(x=407, y=160)

        Button(self.frame_detalhes, command=self.nova_turma, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy', 7, 'bold'), bg=co3, fg=co1).place(x=507, y=160)
        Button(self.frame_detalhes, command=self.atualizar_turma, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy', 7, 'bold'), bg=co6, fg=co1).place(x=587, y=160)
        Button(self.frame_detalhes, command=self.deletar_turma, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy', 7, 'bold'), bg=co7, fg=co1).place(x=667, y=160)

        self.mostrar_cursos(self.frame_tabela_curso_sub)  # Exibe a tabela de cursos no sub-frame
        self.mostrar_turmas(self.frame_tabela_turma_sub)  # Exibe a tabela de turmas no sub-frame

    def procurar_aluno(self):
        """Procura alunos na tabela pelo nome digitado no campo de pesquisa."""
        termo_pesquisa = self.e_nome_pesquisa.get().strip().lower()

        # Limpa todos os itens atuais da treeview
        for item in self.tree_aluno.get_children():
            self.tree_aluno.delete(item)

        if not termo_pesquisa: # Se o campo de pesquisa estiver vazio, mostra todos os alunos
            for item in self.dados_alunos:
                self.tree_aluno.insert('', 'end', values=item)
        else: # Caso contrário, filtra os alunos
            for aluno in self.dados_alunos:
                if termo_pesquisa in aluno[1].lower(): # aluno[1] é o nome
                    self.tree_aluno.insert('', 'end', values=aluno)

    def ver_aluno(self):
        """Exibe os detalhes completos do aluno selecionado em uma messagebox."""
        selected_item = self.tree_aluno.selection()
        if not selected_item:
            messagebox.showerror('Erro', 'Selecione um aluno para ver os detalhes.')
            return

        item_values = self.tree_aluno.item(selected_item)['values']

        # Formata os detalhes para exibição
        detalhes = (
            f"ID: {item_values[0]}\n"
            f"Nome: {item_values[1]}\n"
            f"Email: {item_values[2]}\n"
            f"Telefone: {item_values[3]}\n"
            f"Sexo: {item_values[4]}\n"
            f"Data de Nascimento: {item_values[6]}\n"
            f"CPF: {item_values[7]}\n"
            f"Turma: {item_values[8]}\n"
            f"Caminho da Imagem: {item_values[5]}"
        )
        messagebox.showinfo('Detalhes do Aluno', detalhes)


    def mostrar_alunos(self):
        """Exibe a tabela de alunos no frame_tabela."""
        for widget in self.frame_tabela.winfo_children():
            widget.destroy()

        Label(self.frame_tabela, text="Tabela de Estudantes", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy', 10, 'bold'), bg=co1, fg=co4).grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        list_header = ['ID', 'Nome', 'Email', 'Telefone', 'Sexo', 'Imagem', 'Data Nasc.', 'CPF', 'Turma']

        self.tree_aluno = ttk.Treeview(self.frame_tabela, selectmode="extended", columns=list_header, show="headings")
        self.tree_aluno.bind("<<TreeviewSelect>>", self.selecionar_aluno_para_edicao)

        vsb = ttk.Scrollbar(self.frame_tabela, orient="vertical", command=self.tree_aluno.yview)
        hsb = ttk.Scrollbar(self.frame_tabela, orient="horizontal", command=self.tree_aluno.xview)

        self.tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree_aluno.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        self.frame_tabela.grid_rowconfigure(1, weight=1) # Ensure the treeview expands vertically

        hd = ["nw", "nw", "nw", "center", "center", "center", "center", "center", "center"]
        h = [40, 150, 150, 70, 70, 70, 80, 80, 100]
        n = 0

        for col in list_header:
            self.tree_aluno.heading(col, text=col.title(), anchor=NW)
            self.tree_aluno.column(col, width=h[n], anchor=hd[n])
            n += 1
        
        # Recarrega os dados do banco antes de popular a tabela
        self.dados_alunos = db.ver_alunos() 
        for item in self.dados_alunos:
            self.tree_aluno.insert('', 'end', values=item)


    def mostrar_cursos(self, frame_alvo):
        """Exibe a tabela de cursos no frame_alvo especificado."""
        for widget in frame_alvo.winfo_children():
            widget.destroy()

        Label(frame_alvo, text="Tabela de Cursos", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy', 10, 'bold'), bg=co1, fg=co4).grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        list_header = ['ID', 'Curso', 'Duração', 'Preço']

        self.tree_curso = ttk.Treeview(frame_alvo, selectmode="extended", columns=list_header, show="headings")
        self.tree_curso.bind("<<TreeviewSelect>>", self.selecionar_curso_para_edicao)

        vsb = ttk.Scrollbar(frame_alvo, orient="vertical", command=self.tree_curso.yview)
        hsb = ttk.Scrollbar(frame_alvo, orient="horizontal", command=self.tree_curso.xview)

        self.tree_curso.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree_curso.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_alvo.grid_rowconfigure(1, weight=1) # Ensure the treeview expands vertically

        hd = ["nw", "nw", "e", "e"]
        h = [30, 150, 80, 60]
        n = 0

        for col in list_header:
            self.tree_curso.heading(col, text=col.title(), anchor=NW)
            self.tree_curso.column(col, width=h[n], anchor=hd[n])
            n += 1
        
        # Recarrega os dados do banco antes de popular a tabela
        self.dados_cursos = db.ver_cursos()
        for item in self.dados_cursos:
            self.tree_curso.insert('', 'end', values=item)


    def mostrar_turmas(self, frame_alvo):
        """Exibe a tabela de turmas no frame_alvo especificado."""
        for widget in frame_alvo.winfo_children():
            widget.destroy()

        Label(frame_alvo, text="Tabela de Turmas", height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy', 10, 'bold'), bg=co1, fg=co4).grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

        list_header = ['ID', 'Nome da Turma', 'Curso', 'Início']

        self.tree_turma = ttk.Treeview(frame_alvo, selectmode="extended", columns=list_header, show="headings")
        self.tree_turma.bind("<<TreeviewSelect>>", self.selecionar_turma_para_edicao)

        vsb = ttk.Scrollbar(frame_alvo, orient="vertical", command=self.tree_turma.yview)
        hsb = ttk.Scrollbar(frame_alvo, orient="horizontal", command=self.tree_turma.xview)

        self.tree_turma.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree_turma.grid(column=0, row=1, sticky='nsew')
        vsb.grid(column=1, row=1, sticky='ns')
        hsb.grid(column=0, row=2, sticky='ew')
        frame_alvo.grid_rowconfigure(1, weight=1) # Ensure the treeview expands vertically

        hd = ["nw", "nw", "e", "e"]
        h = [30, 150, 80, 60]
        n = 0

        for col in list_header:
            self.tree_turma.heading(col, text=col.title(), anchor=NW)
            self.tree_turma.column(col, width=h[n], anchor=hd[n])
            n += 1
        
        # Recarrega os dados do banco antes de popular a tabela
        self.dados_turmas = db.ver_turmas()
        for item in self.dados_turmas:
            self.tree_turma.insert('', 'end', values=item)

    def control(self, i):
        """Controla qual interface (Cadastro de Aluno ou Adicionar Curso/Turma) é exibida."""
        # Limpa completamente os frames dinâmicos antes de recriar os elementos
        for widget in self.frame_detalhes.winfo_children():
            widget.destroy()
        for widget in self.frame_tabela.winfo_children():
            widget.destroy()

        if i == "cadastro":
            self.alunos()
        elif i == "adicionar":
            self.adicionar()
        elif i == "salvar":
            messagebox.showinfo('Informação', 'Ação Salvar - Use os botões específicos na tela atual (Aluno/Curso/Turma).')


if __name__ == "__main__":
    janela = Tk()
    app = StudentManagementApp(janela)
    janela.mainloop()