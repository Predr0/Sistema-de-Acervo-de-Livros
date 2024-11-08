from genero import Genero;
from editora import Editora;
from autor import Autor;
import psycopg

conn = psycopg.connect( dbname = "postgres" ,host = "gracelessly-native-octopus.data-1.use1.tembo.io",user = "postgres", password ="EW9Sxfvyb6Q1q4XT", port = 5432);
print(conn.info);

class Livro:
    
    def __init__(self,isbn,titulo,autor,editora,quantidade,preco,localidade,genero):

        self._isbn = isbn;
        self._titulo = titulo;
        self._autor = autor;
        self._editora = editora;
        self._quantidade = quantidade
        self._preco = preco;
        self._localidade = localidade;
        self._genero =  genero;


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

