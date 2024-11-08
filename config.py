import psycopg as db;

class Config:

    def __init__(self):
        self.config = {

             "postgres":{
                 
                 "user" : "postgres",
                 "password" : "EW9Sxfvyb6Q1q4XT",
                 "host" : "gracelessly-native-octopus.data-1.use1.tembo.io",
                 "port":"5432",
                 "database" : "postgres"

             }

        }