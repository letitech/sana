from config.config import DataBase

class User:
    def __init__(self):
        self.database = DataBase()

    def create_user(self, username, password):
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        params = (username, password)
        if self.database.execute_query(query, params):
            return True
        else:
            return False
    
    def read_users(self):
        query = "SELECT * FROM users"
        cursor = self.database.execute_query(query)
        if cursor:
            return cursor.fetchall()
        else:
            return None
    
    def read_user_by_id(self, id):
        query = "SELECT * FROM users WHERE id = ?"
        params = (id,)
        cursor =  self.database.execute_query(query, params)
        if cursor:
            return cursor.fetchone()
        else:
            return None
    
    def read_user_by_username(self, username):
        query = "SELECT * FROM users WHERE username = ?"
        params = (username,)
        cursor =  self.database.execute_query(query, params)
        if cursor:
            return cursor.fetchone()
        else:
            return None
    
    def delete_user(self, id):
        query = "DELETE FROM users WHERE id = ?"
        params = (id,)
        if self.database.execute_query(query, params):
            return True
        else:
            return False