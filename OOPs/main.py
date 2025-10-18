# class Student:
#     pass

# class Teacher:
#     pass

# student_obj = Student()

# print(type(student_obj))
# print(type(student_obj) is Student)
# print(type(student_obj) is Teacher)



# class Student:
#     status = "Eligible"

# print(Student.status)

# Student.is_present = True
# print(Student.is_present)

# student_obj = Student()
# student_obj.name = "Nick"
# print("Student",student_obj.status,student_obj.is_present,student_obj.name)




# Attribute Shadowing

# class User:
#     role = "student"
#     is_salaried = False

# student = User()

# student.role = "monitor"
# print(f"Role after changing {student.role}")
# print(f"Role before changing {User.role}")

# del student.role
# print(f"Role after deletion {User.role}")

# #manualy injected value which is not present in class, on deleting this will lead to attribute error as no fallback is present in class
# student.grade = 5
# # del student.grade
# print(f"Student grade {student.grade}")





#Seld Argument in python

# class Student:
#     grade = 5

#     def sayHello(self):
#         return f"My grade is {self.grade}"
    
# st1 = Student()
# print(st1.sayHello())    
# print(Student.sayHello(st1))    






# # Constructor

# class User:
#     def __init__(self,name,city):
#         self.name = name
#         self.city = city

#     def summary(self):
#         return f"{self.name} lives in {self.city}"


# user1 = User(city="Delhi",name="Nick")
# user2 = User("Nia","Patna")
# print(user1.summary())       
# print(user2.summary())       




# class User:
#     def __init__(self,name):
#         self.name = name

#     def introduce(self):
#         print(f"{self.name} says Hello")    


# class Student(User):
#     def talks(self):
#         print(f"I am a student and my name is {self.name}")


# st1 = Student("Nia")
# st1.talks()



 #Multiple Inheritence(MOR-Method Resolution Order)

# class A:
#     text = "I am from A"

# class B(A):
#     text = "I am from B"

# class C(A):
#     text = "I am from C"

# class D(B,C):
#     pass

# obj = D()
# print(obj.text)
# print(D.__mro__)



#Static methods

# class User:
    
#     @staticmethod
#     def sayHello(name):
#         print(f"{name} says Hello👋")


# User.sayHello("Nick")        