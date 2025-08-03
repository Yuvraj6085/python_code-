class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def hello():
        return "Hello, World!"
    

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"
s1= Student("Alice", 25)
print(s1.display_info())
print(Student.hello())