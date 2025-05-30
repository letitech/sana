from model.category import Category

class CategoryController():
    def __init__(self):
        self.category = Category()

    def create_category(self, name, user_id):
        if self.category.create_category(name, user_id):
            return True
        else:
            return False

    def read_categories(self, user_id):
        return self.category.read_categories(user_id)
    
    def read_category_by_id(self, id):
        if id:
            return self.category.read_category_by_id(id)
    
    def update_category(self, name, id):
        if self.category.update_category(name, id):
            return True
        else:
            return False
        
    def delete_category(self, id):
        if id:
            if self.category.delete_category(id):
                return True
            else:
                return False
            
    def search_categories(self, search_term):
        if search_term:
            return self.category.search_categories(search_term)