import random
import string

print("Password Generator")

length = int(input("Enter password length: "))

print("\nChoose Password Strength")
print("1. Only Letters")
print("2. Letters and Numbers")
print("3. Letters, Numbers and Symbols")

choice = input("Enter your choice (1/2/3): ")

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

if choice == "1":
    characters = letters

elif choice == "2":
    characters = letters + numbers

elif choice == "3":
    characters = letters + numbers + symbols

else:
    print("Invalid choice")
    exit()

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)