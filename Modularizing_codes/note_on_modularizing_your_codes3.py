
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

# class Student:
#     def __init__(self, name, course, level, state_of_origin, university):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.state_of_origin = state_of_origin
#         self.cgpa = 0.0
#         self.university = university
# bola = Student("Bola Ojo", "Animal Science", "200", "Osun State","Federal University of Technology Akure")
# sola = Student("Sola Ige", "Nursing", "400", "Kogi State","Federal University of Technology Akure")
# # futa = Student("Federal University of Technology Akure")
# print(bola.name)             
# print(bola.course)        
# print(bola.state_of_origin)  
# student1 = Student("Bola Ojo", "Animal Science", "200", "Osun State","Federal University of Agriculture,Abeokuta")
# student2 = Student("Sola Ige", "Nursing", "400", "Kogi State","Federal University of Technology Akure")

# print(student1.name)  
# print(student2.name)

# # print(Student.university)     
# print(student1.university)   
# print(student2.university)

# class Student:
#     def __init__(self, name, course, level):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.cgpa = 0.0
#         self.fees_paid = False

#     def pay_school_fees(self):
#         self.fees_paid = True
#         return f"{self.name} has paid school fees for {self.level} level"
    
#     def register_courses(self):
#         if self.fees_paid:
#             return f"{self.name} has registered courses for {self.course}"
#         else:
#             return f"{self.name} must pay school fees first!"
#     def calculate_cgpa(self, grades):
#         if grades:
#             self.cgpa = sum(grades) / len(grades)
#             return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
#         return "No grades provided"
# ridwan = Student("Ridwan Oseni", "AI development", 400)
# print(ridwan.pay_school_fees())
# print(ridwan.register_courses())
# print(ridwan.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))


# class BankAccount:
#     def __init__(self, owner, bank_name, balance=0):
#         # ATTRIBUTES - What the account HAS
#         self.owner = owner
#         self.bank_name = bank_name
#         self.balance = balance
#         self.account_number = self.generate_account_number()
    
#     # METHODS - What the account can DO
#     def deposit(self, amount):
#         """Add money to the account"""
#         if amount > 0:
#             self.balance += amount  # Method changes attribute
#             return f"₦{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance:,}"
#         return "Invalid deposit amount"
    
#     def withdraw(self, amount):
#         """Remove money from the account"""
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount  # Method changes attribute
#             return f"₦{amount:,} withdrawn from {self.owner}'s account. New balance: ₦{self.balance:,}"
#         return "Insufficient funds or invalid amount"
    
#     def transfer(self, amount, recipient):
#         """Transfer money to another account"""
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: ₦{self.balance:,}"
#         return "Transfer failed: Insufficient funds"
    
#     def check_balance(self):
#         """Check current balance"""
#         return f"{self.owner}'s {self.bank_name} account balance: ₦{self.balance:,}"
    
#     def generate_account_number(self):
#         """Generate a unique account number"""
#         import random
#         return f"01{random.randint(10000000, 99999999)}"
# ridwan = BankAccount("Ridwan Oseni","Zenith Bank", 5000)
# print(f"Owner: {ridwan.owner}")
# print(f"Bank name: {ridwan.bank_name}")
# print(f"Balance: {ridwan.balance}")
# print(ridwan.deposit(5000))
# print(ridwan.withdraw(2000))
# print(ridwan.transfer(1000, "Esther"))
# print(ridwan.check_balance())
# print(ridwan.generate_account_number())


class NaijaPhone:
    def __init__(self, brand, model, network_provider):
        self.brand = brand
        self.model = model
        self.network_provider = network_provider
        self.airtime_balance = 0
        self.data_balance = 0
        self.is_on = False
    def power_on(self):
        self.is_on = True
        return f"Your {self.brand} phone is now on. Network: {self.network_provider}"
    def buy_airtime(self, amount):
        self.airtime_balance += amount
        return f"You just successfully recharged ₦{amount}. Your airtime balance is now ₦{self.airtime_balance}"
    def buy_data(self, amount):
        self.airtime_balance -= amount
        self.data_balance += amount
        return f"{amount}MB has been purchased. Your Data and Airtime balance are {self.data_balance}MB and {self.airtime_balance}MB respectively"
    def share_airtime(self, amount, recipient):
        if self.airtime_balance >= amount:
            self.airtime_balance -= amount
            return f"₦{amount} airtime has been successfully shared with {recipient}. Airtime balance is now: ₦{self.airtime_balance}"
        return "Failed! Insufficient airtime balance."
    def share_data(self, amount, recipient):
        if self.data_balance >= amount:
            self.data_balance -= amount
            return f"{amount}MB has been successfully shared with {recipient}. Data balance is now: {self.data_balance}MB"
        return f"Failed! Insufficient data balance."
    def make_call(self, recipient, call_duration):
        self.is_on = True
        if self.airtime_balance > 0:
            self.airtime_balance -= 10 * call_duration
            return f"Dailing {recipient}..., Duration of call is {call_duration} and the airtime balance is now {self.airtime_balance}"
        
        
         
        return f"Your airtime balance is low, please recharge or dail *303# to borrow airtime from {self.network_provider}"
    def send_SMS(self, message, recipient):
        self.is_on = True
        if self.airtime_balance >= 4:
            self.airtime_balance -= 4
            return f"SMS sent to {recipient}: '{message}'. Your remaining balance is {self.airtime_balance}"
        return f"Insufficient airtime balance."
    
phone = NaijaPhone("Apple","Iphone 12", "MTN" )
print(f"Brand: {phone.brand}")
print(f"Model: {phone.model}")
print(f"Network: {phone.network_provider}")
print(phone.buy_airtime(7000))
print(phone.send_SMS("THANK YOU FOR BANKING WITH US", "08050518803"))
print(phone.make_call("07031826698", 3 ))
print(phone.buy_data(2000))
print(phone.buy_airtime(2000))
print(phone.share_airtime(500, "09030103768"))
print(phone.share_data(1000, "09030103768"))



        