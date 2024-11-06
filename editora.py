class Editora:

    def __init__(self,nome):
       self._nome = nome;

    def getNome(self):

        return self._nome;
    def setNome(self, nome):
        if isinstance(nome, str):
            self._nome = nome;
        else:
            print("erro");