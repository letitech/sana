from model.user import User
from utils.pasword_manager import PasswordManager

class UserController():
    def __init__(self):
        self.user = User()
        self.password_manager = PasswordManager()

    def create_user(self, username, password):
        password = self.password_manager.hash_password(password)
        if self.user.create_user(username, password):
            return True
        else:
            return False

    def read_users(self):
        return self.user.read_users()
    
    def read_user_by_id(self, id):
        if id:
            return self.user.read_user_by_id(id)
    
    def read_user_by_username(self, username):
        if username:
            return self.user.read_user_by_username(username)
    
    def delete_user(self, id):
        if id:
            if self.user.delete_user(id):
                return True
            else:
                return False

    def login(self, username, password):
        user = self.user.read_user_by_username(username)
        if user:
            if self.password_manager.verify_password(password, user[2]):
                return user
            else:
                return False
        else:
            return False