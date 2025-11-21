class Student():
    name=""
    age=12
    schoolclass="6 A"
    house="saphire"
    classteacher="Pooja Maam"

    def __init__(self):
        print("Making a new student")

    def chane_detail(self):
        print("Please enter your age:  ")
        self.age=int(input())
        print("Please enter the name of the student:  ")
        self.name=input

    def show_details(self):
        print("The Details of the student:  ")
        print(self.name)
        print(self.age)
        print(self.schoolclass)
        print(self.house)
        print(self.classteacher)

Jonathan=Student()

Jonathan.show_details()