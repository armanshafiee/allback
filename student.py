
class student:
    def __init__(self, name, school, grade, id):
        self.name = name
        self.school = school
        self.grade = grade
        self.id = id
    def printe (self):
        print ( )
        print ("thise is your name: ", self.name)
        print ("thise is your school name: ", self.school)
        print ("thise is your grade: ", self.grade)
        print ("thise is your ID: ", self.id)

name = input("give your name: ")
school = input("give your school name: ")
grade = input("give your grade: ")
id = input("give your ID: ")

s1 = student(name , school , grade , id)
s1.printe()
