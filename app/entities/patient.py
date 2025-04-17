from entities.user import User

class Patient(User):
    def __init__(self, name: str, email: str, password: str,):
        super().__init__(name, email, password)
    
    def __str__(self):
        return f"Patient(name={self.name}, email={self.email})"

    
