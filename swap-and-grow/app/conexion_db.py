import mysql.connector

class DatabaseConnection:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="swap_and_grow"
        )
        self.cursor = self.conn.cursor()

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
