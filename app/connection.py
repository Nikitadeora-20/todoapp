import mysql.connector

class MySQLHandler:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def create_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        return self.connection

    def execute_query(self, query, params=None):
        if self.cursor:
            try:
                self.cursor.execute(query, params or ())
                self.connection.commit()
                return self.cursor.fetchall()
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                return None
        else:
            print("Cursor is not initialized.")
            return None

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

# Usage
db_handler = MySQLHandler(host="localhost", user="root", password="Nikita20@", database="tasksdb")
connection = db_handler.create_connection()
if connection:
    result = db_handler.execute_query("SELECT * FROM your_table WHERE column = %s", ("value",))
    if result:
        for row in result:
            print(row)
    db_handler.close_connection()
