from conexao import Conexao
class Editora(Conexao):

    def __init__(self):
     Conexao.__init__(self)

    def addEditora(self,*args):
       try:
         sql = "insert into editora(nome)values(%s)";
         self.execute(sql,args)
         self.commit()
       except Exception as e:
          print("erro ao inserir", e)
   
    def pesquisar(self, *args, type_s = "nome"):
      sql = "select * from editora WHERE nome LIKE %s"
      if type_s == "id":
         sql = "SELECT * FROM editora WHERE id = %s"
      if type_s == "all":
         sql = "SELECT * FROM editora"
      self.cursor.execute(sql, args)
      data = self.cursor.fetchall()
      if data :
         return data
      else:
         return "Registro nao encontrado"

    def update(self, id, *args):
      try:

         sql = f"update editora SET nome = %s WHERE id = {id}"
         self.execute(sql, args)
         self.commit()
         print("registro atualizado")
      
      except Exception as e:
         print("erro ao atualizar",e)
          
    def delete(self, s):
      try:
         sql_s = f"select * from editora where nome= '{s}' "
         if not self.query(sql_s):
            return "Registro não encontrado para deletar"
         sql_d = f"delete from editora where nome= '{s}'"
         self.execute(sql_d)
         self.commit()
         return "Registro realizado com sucesso"
      except Exception as e:
          print("erro ao deletar", e)
    def delGenero(self, id):
      try:
         sql_s = f"select * from editora where id= {id}"
         if not self.query(sql_s):
            return "Registro não encontrado para deletar"
         sql_d = f"delete from editora where id={id}"
         self.execute(sql_d)
         self.commit()
         return "Registro realizado com sucesso"
      except Exception as e:
          print("erro ao deletar", e)
if __name__ == "__main__":
      
   e2 = Editora();
   e2.addEditora("Letras")
