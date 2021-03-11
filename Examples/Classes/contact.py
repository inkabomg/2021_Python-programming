# Retrieve from the datetime module a class datetime, and use it in this script
from datetime import datetime

class Contact:
    def __init__(self, first_name, last_name, phone, birth_year):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.birth_year = birth_year
    
    def ToString(self):
        # f-string formats string so that the variable within {} is
        # replaced with the variable's value 
        return f"{self.first_name} {self.last_name}, p. {self.phone}"

    def Age(self):
        current_year = datetime.now().year
        age = current_year - self.birth_year
        return age
