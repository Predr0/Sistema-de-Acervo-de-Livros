from conexao import Conexao
from genero import Genero;
from editora import Editora;
from autor import Autor;
import psycopg


class Livro(Conexao):
    
    def __init__(self,isbn,titulo,quantidade,preco,editora,genero,autor):

        self._isbn = isbn;
        self._titulo = titulo;
        self._autor = autor;
        self._editora = editora;
        self._quantidade = quantidade
        self._preco = preco;
        self._genero =  genero;
        Conexao.__init__(self)

    @property
    def getIsbn(self):
        return self._titulo

    @getIsbn.setter
    def setIsbn(self, novo_isbn):
        if isinstance(novo_isbn, str) and novo_isbn:
            self._isbn = novo_isbn
        else:
            raise ValueError("O Isbn deve ser uma string não vazia.")
    
    # Getter e Setter para titulo
    @property
    def getTitulo(self):
        return self._titulo

    @getTitulo.setter
    def setTitulo(self, novo_titulo):
        if isinstance(novo_titulo, str) and novo_titulo:
            self._titulo = novo_titulo
        else:
            raise ValueError("O título deve ser uma string não vazia.")

    # Getter e Setter para autor
    @property
    def getAutor(self):
        return self._autor

    @getAutor.setter
    def setAutor(self, novo_autor):
        if isinstance(novo_autor, Autor) and novo_autor:
            self._autor = novo_autor
        else:
            raise ValueError("O autor deve ser uma string não vazia.")

    # Getter e Setter para editora
    @property
    def getEditora(self):
        return self._editora

    @getEditora.setter
    def setEditora(self, nova_editora):
        if isinstance(nova_editora, Editora) and nova_editora:
            self._editora = nova_editora
        else:
            raise ValueError("A editora deve ser uma string não vazia.")

    # Getter e Setter para quantidade
    @property
    def getQuantidade(self):
        return self._quantidade

    @getQuantidade.setter
    def quantidade(self, nova_quantidade):
        if isinstance(nova_quantidade, int) and nova_quantidade >= 0:
            self._quantidade = nova_quantidade
        else:
            raise ValueError("A quantidade deve ser um número inteiro não negativo.")

    # Getter e Setter para preco
    @property
    def getPreco(self):
        return self._preco

    @getPreco.setter
    def setPreco(self, novo_preco):
        if isinstance(novo_preco, (int, float)) and novo_preco >= 0:
            self._preco = novo_preco
        else:
            raise ValueError("O preço deve ser um número não negativo.")

    # Getter e Setter para localidade
    @property
    def getLocalidade(self):
        return self._localidade

    @getLocalidade.setter
    def setLocalidade(self, nova_localidade):
        if isinstance(nova_localidade, str) and nova_localidade:
            self._localidade = nova_localidade
        else:
            raise ValueError("A localidade deve ser uma string não vazia.")

    # Getter e Setter para genero
    @property
    def getGenero(self):
        return self._genero

    @getGenero.setter
    def setGenero(self, novo_genero):
        if isinstance(novo_genero, Genero) and novo_genero:
            self._genero = novo_genero
        else:
            raise ValueError("O gênero deve ser uma string não vazia.")

    def addLivro(self,*args):
       try:
         sql = "insert into livro(isbn,titulo,quantidade,preco,id_editora,id_genero,id_autor)values(%s,%s,%s,%s,%s,%s,%s)";
         self.execute(sql,args)
         self.commit()
       except Exception as e:
          print("erro ao inserir", e)
   
    def pesquisar(self, *args, type_s = "titulo"):
      sql = "select * from livro WHERE titulo LIKE %s"
      if type_s == "id":
         sql = "SELECT * FROM livro WHERE isbn = %s"
      if type_s == "all":
         sql = "SELECT * FROM livro"
      if type_s == "tituloTable":
          sql = "SELECT livro.isbn,livro.titulo,livro.quantidade,livro.preco,editora.nome AS nome_editora,genero.nome AS nome_genero,autor.nome AS nome_autor FROM livro  LEFT JOIN editora ON livro.id_editora = editora.id LEFT JOIN genero ON livro.id_genero = genero.id  LEFT JOIN autor ON livro.id_autor = autor.id WHERE livro.titulo LIKE %s;"
      if type_s == "idTable":
          sql= "SELECT livro.isbn,livro.titulo,livro.quantidade,livro.preco,editora.nome AS nome_editora,genero.nome AS nome_genero,autor.nome AS nome_autor FROM livro  LEFT JOIN editora ON livro.id_editora = editora.id LEFT JOIN genero ON livro.id_genero = genero.id  LEFT JOIN autor ON livro.id_autor = autor.id WHERE livro.isbn = %s;"
      if type_s == "allTable":
          sql = "SELECT livro.isbn,livro.titulo,livro.quantidade,livro.preco,editora.nome AS nome_editora,genero.nome AS nome_genero,autor.nome AS nome_autor FROM livro LEFT JOIN editora ON livro.id_editora = editora.id LEFT JOIN genero ON livro.id_genero = genero.id  LEFT JOIN autor ON livro.id_autor = autor.id;"

      self.cursor.execute(sql, args)
      data = self.cursor.fetchall()
      if data :
         return data
      else:
         return "Registro nao encontrado"

    def update(self, id, titulo,preco,quantidade,editora,genero,autor):
      try:

         sql = "update livro SET titulo = %s, preco= %s, quantidade = %s,id_editora= %s,id_genero = %s,id_autor = %s WHERE isbn = %s"
         self.execute(sql,(titulo, preco, quantidade, editora, genero, autor, id))
         self.commit()
         print("registro atualizado")
      
      except Exception as e:
         print("erro ao atualizar",e)
    
    def updateQuantidade(self, id, type_s="none"):
        
        print(type_s)
        print(id)
        if type_s == "add":
            try:
            
                sql= "update livro Set quantidade = quantidade+1 WHERE isbn = %s"
                self.execute(sql,(id,))
                self.commit()
                print("quantidade atualizada")

            except Exception as e:
                print("erro de", e)
        if type_s == "rem":
            try:
            
                sql= "update livro Set quantidade = quantidade-1 WHERE isbn = %s"
                self.execute(sql,(id,))
                self.commit()
                print("quantidade atualizada")

            except Exception as e:
                print("erro de", e)
        else:
            print("erro")
          
    def delete(self, s):
      try:
         sql_s = f"select * from livro where nome= '{s}' "
         if not self.query(sql_s):
            return "Registro não encontrado para deletar"
         sql_d = f"delete from livro where nome= '{s}'"
         self.execute(sql_d)
         self.commit()
         return "Registro realizado com sucesso"
      except Exception as e:
          print("erro ao deletar", e)
    def dellivro(self, id):
      try:
         sql_s = f"select * from livro where isbn= '{id}'"
         if not self.query(sql_s):
            return "Registro não encontrado para deletar"
         sql_d = f"delete from livro where isbn='{id}'"
         self.execute(sql_d)
         self.commit()
         return "Registro realizado com sucesso"
      except Exception as e:
          print("erro ao deletar", e)

