from typing import List

class Account:
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance
        self.history: List[str] = []

    def __add__(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError("No such logic")
        self.balance+=amount
        self.history.append(f"Deposit: {amount}")
        return self 
    
    def __sub__(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError("No such logic")
        self.balance-=amount
        self.history.append(f"Withdrawal: {amount}")
        return self 
    
    def __str__(self):
        return f"Account: {self.name}, Balance: {self.balance}"

        




acc = Account("John", 1000)
acc += 500
acc -= 200
print(acc)  # Account: John, Balance: 1300
print(acc.history)  # ['Deposit: 500', 'Withdrawal: 200']
