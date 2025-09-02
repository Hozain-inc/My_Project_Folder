
# class Student:
#     def __init__(self, name, course, level):
#         print("Creating a new student...")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} has been created. ")
# ola = Student("Ola Abgaje", "Python", 500)


# class NigerianStudent:
#     def __init__(self, name, state, university, course):
#         print(f" Creating objects...")
#         self.name = name
#         self.state_of_origin = state
#         self.university = university
#         self.course = course
#         self.student_id = self.generate_id()
#         print(f" {self.name} from {self.state_of_origin}, studying {self.course} in the {self.university} ,Nigeria")
#     def generate_id(self):
#         import random
#         return f"UNISAIL{random.randint(1000, 9999)}"

# ridwan = NigerianStudent("Ridwan Oseni", "Oyo", "University of Ibadan", "Economics")    
# print(ridwan.student_id)

# class PhoneUser:
#     def __init__(self, owner, brand, network):
#         self.owner = owner
#         self.brand = brand
#         self.network = network
#         self.airtime = 0
#         self.data = 0
#         print(f"{self.owner} owns an {self.brand} and has joined {self.network} Network")

#     def buy_airtime(self, amount):
#         self.airtime += amount 
#         return f"{self.owner} now has ₦{self.airtime} airtime"
#     def buy_data(self, MB):
#         self.data += MB
#         return f"{self.owner} have successfully purchased {MB}MB data "
# ridwan = PhoneUser("Ridwan Oseni", "iphone", "MTN")
# print(ridwan.buy_airtime(1000))
# print(ridwan.buy_data(2000))
# print(ridwan.airtime)
# print(ridwan.data,"MB")
# susan = PhoneUser("Susan Corbon", "iphone", "Airtel")
# print(susan.buy_airtime(500))
# print(susan.buy_data(800))
# print(susan.airtime)
# print(susan.data,"MB")

class Student:
    def __init__(self, name, course, level, state_of_origin, university):
        self.name = name
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin
        self.cgpa = 0.0
        self.university = university
bola = Student("Bola Ojo", "Animal Science", "200", "Osun State","Federal University of Technology Akure")
sola = Student("Sola Ige", "Nursing", "400", "Kogi State","Federal University of Technology Akure")
# futa = Student("Federal University of Technology Akure")
print(bola.name)             
print(bola.course)        
print(bola.state_of_origin)  
student1 = Student("Bola Ojo", "Animal Science", "200", "Osun State","Federal University of Agriculture,Abeokuta")
student2 = Student("Sola Ige", "Nursing", "400", "Kogi State","Federal University of Technology Akure")

print(student1.name)  
print(student2.name)

# print(Student.university)     
print(student1.university)   
print(student2.university)

