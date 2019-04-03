class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person(self):
        print("Name : ", self.name, ", Age: ", self.age)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_address(self):
        return self.address
