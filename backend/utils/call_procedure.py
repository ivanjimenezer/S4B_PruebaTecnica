import psycopg2
from psycopg2 import sql
import environ, os


class call_Procedure:
    def __init__(self):
        env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../scrappingApp/.env')
        env = environ.Env()
        env.read_env(env_path)

        self.dbname = env.str('DB_NAME')
        self.user = env.str('DB_USER')
        self.password = env.str('DB_PASSWORD')
        self.host = env.str('DB_HOST')
        self.port = env.int('DB_PORT', 5432) 

        self.connection = None
        self.cursor = None

    def connect(self):
        if self.connection is None:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()

    def call_procedure(self, proc_name, *args):
        self.connect()
        args_placeholders = ', '.join(['%s'] * len(args))
        query = sql.SQL("CALL {}({});").format(
            sql.Identifier(proc_name),
            sql.SQL(args_placeholders)
        )
        self.cursor.execute(query, args)
        self.connection.commit()
        
   
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
