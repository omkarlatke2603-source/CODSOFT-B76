import random
import string

print("===== PASSWORD GENERATOR =====")

# Ask user for password length
length = int(input("Enter password length: "))

# Ask user for complexity
print("\nChoose complexity:")
print("1. Simple   (letters only)")
print("2. Medium   (letters + numbers)")
print("3. Strong   (letters + numbers + symbols)")

choice = input("\nEnter choice (1/2/3): ")

# Set characters based on choice
if choice == "1":
    characters = string.ascii_letters

elif choice == "2":
    characters = string.ascii_letters + string.digits

elif choice == "3":
    characters = string.ascii_letters + string.digits + string.punctuation

else:
    print("Invalid choice! Using Strong by default.")
    characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display the result
print("\n==============================")
print(f"  Generated Password: {password}")
print("==============================")
