import tkinter as tk
from tkinter import ttk
from livro import Livro
from conexao import Conexao
from genero import Genero;
from editora import Editora;
from autor import Autor;
from funcoes import Funcoes

class ControleDeAcervo:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Acervo")
        self.root.geometry("500x500")
        
        self.atualizarGrid()
        
        f = Funcoes()
        # Criando os campos de entrada
        tk.Label(root, text="ISBN").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.isbn_entry = tk.Entry(root, width=30)
        self.isbn_entry.grid(row=1, column=0, padx=5, pady=5)

        tk.Label(root, text="Título").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.titulo_entry = tk.Entry(root, width=30)
        self.titulo_entry.grid(row=0, column=0, padx=5, pady=5)
        
        tk.Label(root, text="Preço").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.preco_entry = tk.Entry(root, width=30)
        self.preco_entry.grid(row=2, column=0, padx=5, pady=5)

        tk.Label(root, text="Quantidade").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.quantidade_entry = tk.Entry(root, width=30)
        self.quantidade_entry.grid(row=3, column=0, padx=5, pady=5)

        tk.Label(root, text="Gênero").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        nomes_generos = f.valoresComboBox("genero")
        self.genero_combobox = ttk.Combobox(root, values=nomes_generos, width=28)
        self.genero_combobox.grid(row=4, column=0, padx=5, pady=5)

        self.generoCadastrar = tk.Button(root,text="Cadastrar Genero", command= self.cadastrarGenero,width=20).grid(row= 4, column=1)
        
        nomesAutor = f.valoresComboBox("autor")
        tk.Label(root, text="Autor").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        self.autor_combobox = ttk.Combobox(root, values=nomesAutor, width=28)
        self.autor_combobox.grid(row=5, column=0, padx=5, pady=5)

        self.autorCadastro = tk.Button(root,text="Cadastro Autor",command= self.cadastrarAutor,width=20).grid(row=5, column=1)

        nomesEditora = f.valoresComboBox("editora")
        tk.Label(root, text="Editora").grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.editora_combobox = ttk.Combobox(root, values=nomesEditora, width=28)
        self.editora_combobox.grid(row=6, column=0, padx=5, pady=5)

        self.editoraCadastro = tk.Button(root, text="Cadastrar Editora",command=self.cadastrarEditora,width=20)
        self.editoraCadastro.grid(row=6, column=1)

        # Botão de cadastro
        self.cadastrar_button = tk.Button(root, text="Cadastrar Livro", command=self.cadastrar_livro, width=20)
        self.cadastrar_button.grid(row=7, column=0, pady=10)

        self.pesquisarBotao = tk.Button(root,text="pesquisar", command=self.pesquisar,width=20).grid(row=7,column=1 )

        self.UpdateBotao = tk.Button(root,text="Alterar Livro",command=self.updateLivro,width=20).grid(row=9,column=1 )

        # Listagem de livros
        self.tree = ttk.Treeview(root, columns=("ISBN","Título", "Quantidade", "Preço", "Editora", "Gênero",  "Autor"), show="headings", height=10)
        self.tree.grid(row=8, column=0, columnspan=2, pady=10)
        
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

        self.limpar= tk.Button(root,text="Limpar campos", command=self.limparCampos,width=20).grid(row=9,column=0)

        tk.Button(root, text="Deletar Livro",width=20,command=self.deleteLivro).grid(row=10,column=0)
    def atualizarGrid(self):

        coluna,linha=root.grid_size()
        i=0
        for i in range(coluna):
            root.columnconfigure(i,weight=1,minsize=300)
    def pesquisar(self,type_s="none"):

        self.tree.delete(*self.tree.get_children())
        livro = Livro("","","","","","","")
        titulo = self.titulo_entry.get()
        isbn = self.isbn_entry.get()

        if(titulo != "" and isbn =="" and type_s=="none"):
            self.pesquisaBruta=livro.pesquisar(titulo,type_s="tituloTable")

        elif(isbn != "" and titulo=="" and type_s=="none"):
            self.pesquisaBruta=livro.pesquisar(isbn, type_s="idTable")
        
        elif(isbn != "" and titulo != "" and type_s =="none"):
            self.pesquisaBruta=livro.pesquisar(isbn, type_s="idTable")
        
        elif type_s != "none":
            self.pesquisaBruta=livro.pesquisar(type_s="allTable")

        else:
            self.pesquisaBruta=livro.pesquisar(type_s="allTable")
        
        print(self.pesquisaBruta)
        for linha in self.pesquisaBruta:
            self.tree.insert("", "end", values=(linha))

    def cadastrar_livro(self):
        # Pegando os dados dos campos

        def addQuantidadeLivro():

            livro.updateQuantidade(str(isbn),type_s="add")
            frame.destroy()
            self.pesquisar()

        def remQuantidadeLivro():
            
            livro.updateQuantidade(str(isbn),type_s="rem")
            frame.destroy()
            self.pesquisar()

        titulo = self.titulo_entry.get()
        isbn = self.isbn_entry.get()
        
        livro = Livro("","","","","","","")

        pesquisaId=livro.pesquisar(str(isbn),type_s="id")

        if pesquisaId == "Registro nao encontrado":
            preco = float(self.preco_entry.get())
            quantidade = int(self.quantidade_entry.get())

            genero = self.genero_combobox.get()
            g= Genero()
            generoBruto=g.pesquisar(genero,type_s="")
            generos_dict = {nome: id for id, nome in generoBruto}
            idGenero = int(generos_dict.get(genero))

            autor = self.autor_combobox.get()
            a= Autor()
            autorBruto=a.pesquisar(autor,type_s="")
            autor_dict = {nome: id for id, nome in autorBruto}
            idAutor = int(autor_dict.get(autor))

            editora = self.editora_combobox.get()
            e= Editora()
            editoraBruto=e.pesquisar(editora,type_s="")
            editora_dict = {nome: id for id, nome in editoraBruto}
            idEditora = int(editora_dict.get(editora))

            livro.addLivro(isbn,titulo,quantidade,preco,idEditora,idGenero,idAutor)
            self.tree.insert("", "end", values=(isbn,titulo,quantidade,preco, idEditora,idGenero, idAutor))
    
            self.limparCampos()

        else:

            frame = tk.Toplevel(root)
            frame.title("controle de acervo")
            frame.geometry("400x400")
            frame.grab_set()
            
            coluna,linha=root.grid_size()
            i=0
            for i in range(coluna):
                frame.columnconfigure(i,weight=1,minsize=100)
            

            tk.Label(frame, text="O livro ja está registrado no sistema", font=("arial",20,"bold")).grid(row=1,column=0)
            tk.Label(frame, text="Deseja adicionar ou remover a quantidade do estoque?").grid(row=2, column=0)

            tk.Button(frame, text="Adicionar",command=addQuantidadeLivro).grid(row=3,column=0)
            tk.Button(frame, text="Remover", command= remQuantidadeLivro).grid(row=3, column=1)
            
        
    def updateLivro(self):

        frameModificarlivro = tk.Toplevel(root)
        frameModificarlivro.title("Controle de acervo")
        frameModificarlivro.geometry("400x400")
        frameModificarlivro.grab_set()
        f = Funcoes()

        def mostrarpesquisa():

            valorId = campoId.get()
            l = Livro("", "", "", "", "", "", "")
            valores = l.pesquisar(valorId, type_s="id")

            def updateLivro():
                
                g = Genero()
                bruto=g.pesquisar(campoGenero.get())

                id,_ = bruto[0]
                ideditora=id

                a = Autor()
                bruto = a.pesquisar(campoAutor.get())
                id,lixo = bruto[0]
                idautor= id

                e = Editora()
                bruto = e.pesquisar(campoEditora.get())
                id,lixo = bruto[0]
                ideditora=id
                print(type(campoId.get()))
                
                l.update(str(campoId.get()),str(campoNome.get()),float(campoPreco.get()),int(campoQuantidade.get()),int(ideditora), int(idgenero), int(idautor))
                frameModificarlivro.destroy()

            titulo = preco = quantidade = ideditora = idgenero = idautor = None
            resultado = valores[0]
            if len(resultado) == 7:
                try:
                    # Faz o unpacking
                    id,titulo, quantidade, preco, ideditora, idgenero, idautor = resultado
                    print("Unpacking realizado com sucesso!")
                except ValueError:
                    print("Erro no unpacking: valores não estão no formato correto.")
            else:
                print("Erro: valores não contém exatamente 7 elementos:", resultado)

        
            
            labelNome = tk.Label(frameModificarlivro, text="Nome:").grid(row=4, column=0)
            campoNome = tk.Entry(frameModificarlivro)
            campoNome.grid(row=4, column=1)
            
            if titulo is not None:
                campoNome.insert(0, titulo)

            labelPreco = tk.Label(frameModificarlivro, text="Preço:").grid(row=5, column=0)
            campoPreco = tk.Entry(frameModificarlivro)
            campoPreco.grid(row=5, column=1)
           
            if preco is not None:
                campoPreco.insert(0, preco)

            labelQuantidade = tk.Label(frameModificarlivro, text="Quantidade:").grid(row=6, column=0)
            campoQuantidade = tk.Entry(frameModificarlivro)
            campoQuantidade.grid(row=6, column=1)
            
            if quantidade is not None:
                campoQuantidade.insert(0, quantidade)

            editora=f.valoresComboBox("editora")
            labelEditora = tk.Label(frameModificarlivro, text="Editora:").grid(row=7, column=0)
            campoEditora = ttk.Combobox(frameModificarlivro,values=editora)
            campoEditora.grid(row=7, column=1)
            print(ideditora)

            if ideditora is not None:
                
                e =Editora()
                pesquisa=e.pesquisar(ideditora,type_s="id")
                resultado = pesquisa[0]
                _, nome = resultado
                
                campoEditora.insert(0, nome)

            genero = f.valoresComboBox("genero")
            labelGenero = tk.Label(frameModificarlivro, text="Gênero:").grid(row=8, column=0)
            campoGenero = ttk.Combobox(frameModificarlivro,values=genero)
            campoGenero.grid(row=8, column=1)

            if idgenero is not None:

                g =Genero()
                pesquisa=g.pesquisar(idgenero,type_s="id")
                resultado = pesquisa[0]
                _, nome = resultado
                campoGenero.insert(0, nome)

            autor = f.valoresComboBox("autor")
            labelAutor = tk.Label(frameModificarlivro, text="Autor:").grid(row=9, column=0)
            campoAutor = ttk.Combobox(frameModificarlivro, values=autor)
            campoAutor.grid(row=9, column=1)

            if idautor is not None:

                a =Autor()
                pesquisa=a.pesquisar(idautor,type_s="id")
                resultado = pesquisa[0]
                _, nome = resultado

                campoAutor.insert(0, nome)

            tk.Button(frameModificarlivro, text="Alterar",width=15, command=updateLivro).grid(row=10, column=0)
        

        titulo= tk.Label(frameModificarlivro,text="Alterar Livro", font=("arial",24,"bold")).grid(row=0,column=1)
        
        id = tk.Label(frameModificarlivro,text="Id:").grid(row=1,column=0)
        campoId = tk.Entry(frameModificarlivro)
        campoId.grid(row=1,column=1)
        btnpesquisar = tk.Button(frameModificarlivro, text= "pesquisar", command=mostrarpesquisa).grid(row=3, column=0)

    def deleteLivro(self):
           
        l=Livro("","","","","","","")
        l.dellivro(str(self.isbn_entry.get()))
        self.pesquisar(type_s = "all")
        self.limparCampos()
               

    def limparCampos(self):
        self.titulo_entry.delete(0, tk.END)
        self.isbn_entry.delete(0, tk.END)
        self.preco_entry.delete(0, tk.END)
        self.quantidade_entry.delete(0, tk.END)
        self.genero_combobox.set("")
        self.autor_combobox.set("")
        self.editora_combobox.set("")

    def cadastrarEditora(self):
        frameEditora = tk.Toplevel(root)
        frameEditora.title("controle de acervo")
        frameEditora.geometry("400x400")
        frameEditora.grab_set()

        def salvarEditora():
            nome = self.campoNome.get()
            print(nome)

            e = Editora()
            e.addEditora(nome)
            frameEditora.destroy()
            root.update_idletasks()

        self.labelTitulo = tk.Label(frameEditora, text="Cadastro de Editoras", font=("Arial", 24, "bold")).grid(row=0,column=1)
        self.labelNome = tk.Label(frameEditora, text="Nome:").grid(row=1, column=0, pady=10)
        self.campoNome = ttk.Entry(frameEditora)
        self.campoNome.grid(row=1, column=1)
        self.btnSalvar = tk.Button(frameEditora,text="Salvar", font=("bold"),bg="white", command=salvarEditora).grid(row=2, column= 1)

    def cadastrarAutor(self):
        frameAutor = tk.Toplevel(root)
        frameAutor.title("controle de acervo")
        frameAutor.geometry("400x400")
        frameAutor.grab_set()

        def salvarAutor():
            nome = self.campoNome.get()
            print(nome)

            a = Autor()
            a.addAutor(nome)
            frameAutor.destroy()
            root.update_idletasks()

        self.labelTitulo = tk.Label(frameAutor, text="Cadastro de Autores", font=("Arial", 24, "bold")).grid(row=0,column=1)
        self.labelNome = tk.Label(frameAutor, text="Nome:").grid(row=1, column=0, pady=10)
        self.campoNome = ttk.Entry(frameAutor)
        self.campoNome.grid(row=1, column=1)
        self.btnSalvar = tk.Button(frameAutor,text="Salvar", font=("bold"),bg="white", command=salvarAutor).grid(row=2, column= 1)

    def cadastrarGenero(self):
        frameGenero = tk.Toplevel(root)
        frameGenero.title("controle de acervo")
        frameGenero.geometry("400x400")
        frameGenero.grab_set()

        def salvarGenero():
            nome = self.campoNome.get()
            g = Genero()
            g.addGenero(nome)
            frameGenero.destroy()
            self.reiniciarMainLoop()

        self.labelTitulo = tk.Label(frameGenero, text="Cadastro de Genero", font=("Arial", 24, "bold")).grid(row=0,column=1)
        self.labelNome = tk.Label(frameGenero, text="Nome:").grid(row=1, column=0, pady=10)
        self.campoNome = ttk.Entry(frameGenero)
        self.campoNome.grid(row=1, column=1)
        self.btnSalvar = tk.Button(frameGenero,text="Salvar", font=("bold"),bg="white", command=salvarGenero).grid(row=2, column= 1)

    def reiniciarMainLoop(self):
       
        global root  
        root.destroy()  
        root = tk.Tk()  
        app = ControleDeAcervo(root)  
        root.mainloop()  

if __name__ == "__main__":
    root = tk.Tk()
    app = ControleDeAcervo(root)
    root.mainloop()