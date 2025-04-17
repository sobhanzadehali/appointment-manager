from entities.user import User
class Doctor(User):
    def __init__(self, name: str, email: str, password: str, specialization: str):
        super().__init__(name, email, password)
        self.specialization = specialization
    
    def __str__(self):
        return f"Doctor(name={self.name}, email={self.email}, specialization={self.specialization})"
    
    def __repr__(self):
        return f"Doctor(name={self.name}, email={self.email}, specialization={self.specialization})"
    
    def __eq__(self, other):
        return self.email == other.email
    
    def __hash__(self):
        return hash(self.email)
        
        

