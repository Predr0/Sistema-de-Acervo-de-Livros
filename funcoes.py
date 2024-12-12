from livro import Livro
from genero import Genero
from editora import Editora
from autor import Autor

class Funcoes():

    def __init__(self):
        pass

    def valoresComboBox(self,type_s = "None"):

            if type_s == "genero":
                g = Genero()
                generos_brutos = g.pesquisar(type_s="all")
                nomes_generos = [nome for _, nome in generos_brutos]
                return nomes_generos
            elif type_s == "autor":
                a = Autor()
                autorBrutos = a.pesquisar(type_s="all")
                nomesAutor = [nome for _, nome in autorBrutos]
                return nomesAutor
            elif type_s == "editora":
                e = Editora()
                editoraBrutos = e.pesquisar(type_s="all")
                nomesEditora = [nome for _,nome in editoraBrutos]
                return nomesEditora
            else:
                print("erro no valoresComboBox")

    def tuplasNomes(self,args,type_s):
         
         print(type_s)
         if type_s == "genero":
              
              g =Genero()
              pesquisa=g.pesquisar(args,"id")
              resultado = pesquisa[0]
              nome = None
              _, nome = resultado
              print(nome)
              if nome != None:
                   
                   return nome
    
         elif type_s == "editora":
              
              e =Editora()
              pesquisa=e.pesquisar(args,"id")
              resultado = pesquisa[0]
              nome = None
              _, nome = resultado
              print(nome)
              if nome != None:
                   
                   return nome
              
         elif type_s == "autor":
              
              a =Genero()
              pesquisa=a.pesquisar(args,"id")
              resultado = pesquisa[0]
              nome = None
              _, nome = resultado
              if nome != None:
                   
                   return nome
         else:
              print("erro na funcao tuplasNomes")

    def idCampo(nome, type_s):
         
         if type_s == "genero":
            g = Genero()
            bruto=g.pesquisar(nome)

            id,_ = bruto
            print("ideditora:",id)
            return id
         
         if type_s =="autor":
              a = Autor()
              bruto = a.pesquisar(nome)
              id,_ = bruto
              return id
         if type_s == "editora":
              
              e = Editora()
              bruto = e.pesquisar(nome)
              id,_ = bruto
              return id


