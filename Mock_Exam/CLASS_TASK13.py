
email = input("Enter your email address: ")
if "@" in email and '.' in email.split('@')[1]:
    username, domain = email.split('@')
    print(f"Username: {username}\nDomain: {domain}")
else:
    print("Invalid address")