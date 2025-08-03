class Student:
    def __init__(self, name, roll_no, age):
        self.name = name          # Public attribute
        self._roll_no = roll_no   # Protected attribute
        self.__age = age          # Private attribute

    # Private method (only accessible within the class)
    def __display(self):
        return f"Name: {self.name}, Roll No: {self._roll_no}, Age: {self.__age}"

    # Public method to access private __display
    def display_private_data(self):
        return self.__display()

    # Getter for private __age
    def get_age(self):
        return self.__age

    # Setter for private __age
    def set_age(self, new_age):
        if new_age > 0:  # Validation example
            self.__age = new_age
        else:
            print("Invalid age")

    # Getter for protected _roll_no
    def get_roll_no(self):
        return self._roll_no

    # Setter for protected _roll_no
    def set_roll_no(self, new_roll_no):
        self._roll_no = new_roll_no

class Branch(Student):
    def show(self):
        return f"Branch of {self.get_roll_no()}"  # Access protected via getter

# Usage
s1 = Student("Vinit", 101, 20)

# Access private attribute via getter/setter
print(s1.get_age())      # Output: 20
s1.set_age(21)           # Update age
print(s1.get_age())      # Output: 21

# Access protected attribute via getter/setter
print(s1.get_roll_no())  # Output: 101
s1.set_roll_no(102)      # Update roll number
print(s1.get_roll_no())  # Output: 102

# Access private method via public wrapper
print(s1.display_private_data())  
# Output: Name: Vinit, Roll No: 102, Age: 21

# Subclass usage
b1 = Branch("Ankit", 109, 22)
print(b1.show())  # Output: Branch of 109