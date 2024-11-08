import psycopg as db
from config import Config
class Conexao(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect( dbname = "postgres" ,host = "gracelessly-native-octopus.data-1.use1.tembo.io",user = "postgres", password ="EW9Sxfvyb6Q1q4XT", port = 5432);
            self.cur = self.conn.cursor() 
        except Exception as e:
            print("Erro em conectar o banco de dados",e)
            exit(1)

    def __enter__ (self):
        return self
    
    def __exit__ (self, exc_type,exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn
    
    @property
    def cursor(self):
        return self.cur
    
    @property
    def commit(self):
        return self.connection.commit()
    
    def fetchall(self):
        return self.cursor.fetchall
    
    def execute(self, sql , params = None):

        self.cursor.execute(sql, params or ())
        
    def query(self, sql , params = None):

        self.cursor.execute(sql, params or ())
        return self.fetchall()