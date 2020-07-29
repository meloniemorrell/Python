#Parent Class

class Teacher:
        subject = "Social Studies"
        name = "Tara Whitman"
        pin = "abc123"

        def getGPAInfo(self):
            entry_name = input("Enter your name: ")
            entry_pin = input("Enter your id: ")
            entry_subject = input("Enter subject: ")
            if (entry_pin == self.pin and entry_name == self.name):
                    print("Let's get started, {}!".format(entry_name))
            else:
                    print("The name or pin is incorrect, please try again.")

#Child Class 1
class Student(User):
        name = "Johnnie Rocket"
        subject = "Social Studies"
        grade = "10"
        email = "johnnierocket@gmail.com
        id = "123456"
#Same method as teacher class "User"
#Difference is use of  pin instead of student id.

     

    def getGPAInfo(self):
        entry_name = input("Enter your name: ")
        entry_subject = input("Enter subject: ")
        entry_grade = input("Enter your grade: ")
        entry_email = input("Enter your email: ")
        entry_id = input("Enter student id: ")
        if (entry_id == self.id and entry_name == self.name):
                print("Let's get started, {}!".format(entry_name))
        else:
                print("The name or id is incorrect, please try again.")



    
#Child Class 2
class Parent(User):
        parent name = "Rebecca Rocket"
        parent phone = "4542324000"
        parent password = "cool_mom"
        student name = "Johnnie Rocket"
        student subject = "Social Studies"
        student grade = "10"
#Same method as teacher class "User" and student class "User
#Difference is use of pw instead of student id and pin.

     

    def getGPAInfo(self):
        entry_name = input("Enter your name: ")
        entry_phone = input("Enter your telephone number: ")
        entry_password= input("Enter your password: ")
        entry_student name = input("Enter student name: ")
        entry_student subject = input("Enter student subject: ")
        entry_grade = input("Enter student grade: ")
        if (entry_password == password.id and entry_name == self.name):
                print("Let's get started, {}!".format(entry_name))
        else:
                print("The name or id is incorrect, please try again.")




#The following code invokes the methods inside each class for teacher, student, and parent.

        teacher = User()
        teacher.getGPAInfo()

        
        student = Student()
        student.getGPAInfo()

        parent = Parent()
        parent.getGPAInfo()
        

