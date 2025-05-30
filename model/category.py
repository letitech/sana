from config.config import DataBase

class Category:
    def __init__(self):
        self.database = DataBase()

    def create_category(self, name, user_id):
        query = "INSERT INTO categories (name, user_id) VALUES (?, ?)"
        params = (name, user_id)
        if self.database.execute_query(query, params):
            return True
        else:
            return False
    
    def read_categories(self, user_id):
        query = "SELECT * FROM categories WHERE user_id = ?"
        params = (user_id,)
        cursor = self.database.execute_query(query, params)
        if cursor:
            return cursor.fetchall()
        else:
            return None
    
    def read_category_by_id(self, id):
        query = "SELECT * FROM categories WHERE id = ?"
        params = (id,)
        cursor =  self.database.execute_query(query, params)
        if cursor:
            return cursor.fetchone()
        else:
            return None
    
    def update_category(self, name, id):
        query = "UPDATE categories SET name = ? WHERE id = ?"
        params = (name, id)
        if self.database.execute_query(query, params):
            return True
        else:
            return False
        
    def delete_category(self, id):
        query = "DELETE FROM categories WHERE id = ?"
        params = (id,)
        if self.database.execute_query(query, params):
            return True
        else:
            return False
        
    def search_categories(self, search_term):
        query = "SELECT * FROM categories WHERE name LIKE ?"
        params = (f'%{search_term}%')
        cursor =  self.database.execute_query(query, params)
        if cursor:
            return cursor.fetchall()
        else:
            return None