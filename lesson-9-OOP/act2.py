class Student:
    grade ="8th"
    name = "Reyan"

    def introduce(self):
        print(f"My name is {self.name} and I am in grade {self.grade}.")

    def greet (self):
        print("Hello everyone!")

student1 = Student()
student1.introduce()
student1.greet()