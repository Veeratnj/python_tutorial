"""
Encapsulation

Example and comments for Encapsulation.
"""

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance

account = BankAccount(100)
print(account.get_balance())
