class User:
    first_name = "Nasta"
    last_name = "Last"

    def __init__(self, first_name, last_name):
        self.username = first_name
        self.lastname = last_name

    def get_name(self):
        return self.username

    def get_lname(self):
        return self.lastname

    def get_name_lname(self):
        return f"{self.username} {self.lastname}"
