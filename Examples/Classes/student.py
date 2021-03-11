from contact import Contact

# Opiskelija expands Contact type with a student id
class Student(Contact):
    def __init__(self, first_name, last_name, phone, birth_year, student_id):
        # Executes the (Contact) constructor
        super().__init__(first_name, last_name, phone, birth_year)
        self.student_id = student_id

    def ToString(self):
        base = super().ToString()
        return f"{base} #{self.student_id}"