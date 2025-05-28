from bcrypt import gensalt, hashpw, checkpw

class PasswordManager:
    def __init__(self, rounds: int = 12):
        """
        Inicializa el gestor de contraseñas
        
        Args:
            rounds (int): Factor de costo para bcrypt (default: 12)
        """
        self.rounds = rounds
    
    def hash_password(self, password: str) -> str:
        """
        Hashea una contraseña usando bcrypt
        
        Args:
            password (str): Contraseña en texto plano
            
        Returns:
            str: Hash de la contraseña
        """
        if not password:
            raise ValueError("La contraseña no puede estar vacía")
        
        # Convertir a bytes
        password_bytes = password.encode("utf-8")

        # Generar salt y hash
        salt = gensalt(rounds=self.rounds)
        hashed = hashpw(password_bytes, salt)

        return hashed.decode("utf-8")
    
    def verify_password(self, password: str, stored_hash: str) -> bool:
        """
        Verifica si una contraseña coincide con su hash
        
        Args:
            password (str): Contraseña en texto plano
            hash_almacenado (str): Hash almacenado en la base de datos
            
        Returns:
            bool: True si la contraseña es correcta
        """

        if not password or not stored_hash:
            return False
        
        try:
            password_bytes = password.encode("utf-8")
            hash_bytes = stored_hash.encode("utf-8")
            return checkpw(password_bytes, hash_bytes)
        except Exception:
            return False