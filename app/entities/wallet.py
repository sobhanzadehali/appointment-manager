

class Wallet:
    def __init__(self, balance: int=0):
        self.balance = balance
    
    def deposit(self, amount: int):
        self.balance += amount
    
    def withdraw(self, amount: int):
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        self.balance -= amount
    
    def __str__(self):
        return f"Wallet(balance={self.balance})"
    
    def __repr__(self):
        return f"Wallet(balance={self.balance})"
    
    def __eq__(self, other):
        return self.balance == other.balance
    
    def __hash__(self):
        return hash(self.balance)
    
    
    
    
