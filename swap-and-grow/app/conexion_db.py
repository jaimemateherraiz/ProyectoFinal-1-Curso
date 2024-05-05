import mysql.connector

class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="superadmin",
                password="superadmin",
                database="swap_and_grow"
            )
            print("¡Conexión exitosa a la base de datos!")
        except mysql.connector.Error as error:
            print("Error al conectarse a la base de datos:", error)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("¡Conexión cerrada!")

