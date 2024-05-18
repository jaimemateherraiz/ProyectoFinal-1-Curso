import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="swap_and_grow"
            )
            if self.conn.is_connected():
                print("Conexión a la base de datos exitosa")
                self.cursor = self.conn.cursor()
            else:
                print("Error al conectar a la base de datos")
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexión a la base de datos cerrada")
