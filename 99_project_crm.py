"""
Project: CRM

Example and comments for Project: CRM.
"""

# Project: CRM
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

customers = [Customer("Anna", "anna@example.com")]
for c in customers:
    print(c.name, c.email)
