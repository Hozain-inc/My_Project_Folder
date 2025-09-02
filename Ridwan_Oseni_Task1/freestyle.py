# name = "Ridwan Obasanjo Oseni"
# university = "University of Ibadan"
# local_government = "Kajola"
# fave_nig_food = "Amala"

# print(name,"\n", university,"\n", local_government,"\n", fave_nig_food,"\n")

# name = "RIDWAN"
# state = "OYO"
# print("Name:", name)
# print("State:", state)

# print('Time\t\tSubject\t\tTeacher\t')
# print('11:00-11:40\tPython\t\tMr Chris')
# print('11:00-11:40\tMaths\t\tMr Ola')
# print('11:00-11:40\tChemistry\tMr Malik')
# print('11:00-11:40\tEconomics\tMr Ibrahim')
# print('11:00-11:40\tEnglish\t\tMr Deji')
# print('11:00-11:40\tCivic\t\tMr Dotun')


# name = "Obasanjo"
# level = "level 8"
# best_subject = "AI development"
# print(f"My name is {name}, i am in {level} and my best subject is {best_subject}")


# letters = set("mississippi")
# print(letters)

# class BRTBus:
#     def __init__(self, route, bus_number):
       
#         self.route = route            
#         self.bus_number = bus_number    
#         self.current_stop = "Ikorodu"
#         self.passenger_count = 0
#         self.fare = 300
    
 
#     def announce_stop(self):
#         return f"Next stop: {self.current_stop}. Fare is ₦{self.fare}"
    
#     def board_passengers(self, count):
#         self.passenger_count += count
#         return f"{count} passengers boarded. Total: {self.passenger_count}"
#     bus = BRTBus("ojoo", 654321 )
#     print(f"Route: {bus.route}")

    



class BankAccount:
    def __init__(self, owner, bank_name, balance=0):
        # ATTRIBUTES - What the account HAS
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()
    
    # METHODS - What the account can DO
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount  # Method changes attribute
            return f"₦{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance:,}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Remove money from the account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount  # Method changes attribute
            return f"₦{amount:,} withdrawn from {self.owner}'s account. New balance: ₦{self.balance:,}"
        return "Insufficient funds or invalid amount"
    
    def transfer(self, amount, recipient):
        """Transfer money to another account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: ₦{self.balance:,}"
        return "Transfer failed: Insufficient funds"
    
    def check_balance(self):
        """Check current balance"""
        return f"{self.owner}'s {self.bank_name} account balance: ₦{self.balance:,}"
    
    def generate_account_number(self):
        """Generate a unique account number"""
        import random
        return f"01{random.randint(10000000, 99999999)}"
ridwan = BankAccount("Ridwan Oseni","Zenith Bank", 5000)
print(f"Owner: {ridwan.owner}")
print(f"Bank name: {ridwan.bank_name}")
print(f"Balance: {ridwan.balance}")
print(ridwan.deposit(5000))
print(ridwan.withdraw(2000))
print(ridwan.transfer(1000, "Esther"))
print(ridwan.check_balance())
print(ridwan.generate_account_number())