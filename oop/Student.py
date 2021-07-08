
class Student():

    def __init__(self, name="student", age="student", class_="student"):
        self.name = name
        self.age = age
        self.class_ = class_

    def calculate_scores(self, val1, val2, val3):
        answer = (val1 + val2 + val3) / 3
        return f"Average test score: {answer}"

    def to_string(self):
        return f"Student Name: {self.name}, \nStudent Age: {self.age}, \nStudent Class: {self.class_}."


Earl = Student("Earl", 33, "delinquent")
Earl2 = Student()

print(Earl.to_string())
print(Earl.calculate_scores(50, 65, 65))
