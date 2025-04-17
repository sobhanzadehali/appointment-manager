from abc import ABC
from entities.wallet import Wallet

class User(ABC):
    def __init__(self, name: str, email: str, password: str,):
        self.name = name
        self.email = email
        self.password = password
        self.wallet = Wallet()
    def __str__(self):
        return f"User(name={self.name}, email={self.email})"
    
    def __repr__(self):
        return f"User(name={self.name}, email={self.email})"
    
    def __eq__(self, other):
        return self.email == other.email
    
    def __hash__(self):
        return hash(self.email)
    
    
    
    
