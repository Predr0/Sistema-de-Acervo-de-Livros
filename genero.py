import psycopg
from conexao import Conexao 

class Genero(Conexao):

   def __init__(self):
     Conexao.__init__(self)

   def addGenero(self,*args):
       try:
         sql = "insert into genero(nome)values(%s)";
         self.execute(sql,args)
         self.commit()
       except Exception as e:
          print("erro ao inserir", e)
   def delete(self, s):
      try:
         sql_s = f"select * from genero where nome= {s} "
         if not self.query(sql_s):
            return "Registro não encontrado para deletar"
         sql_d = f"delete from genero where nome= {s}"
         self.execute(sql_d)
         self.commit()
         return "Registro realizado com sucesso"
      except Exception as e:
          print("erro ao deletar", e)
   def delGenero(self, id):
      try:
         sql_s = f"select * from genero where id= '{id}'"
         if not self.query(sql_s):
            return "Registro não encontrado para deletar"
         sql_d = f"delete from genero where id={id}"
         self.execute(sql_d)
         self.commit()
         return "Registro realizado com sucesso"
      except Exception as e:
          print("erro ao deletar", e)
if __name__ == "__main__":
      
   g2 = Genero();
   g2.delete("comedia")