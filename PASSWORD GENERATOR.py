import string
import random

def password_generator():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length must be at least 1.")
            return
        
        print("\nSelect the complexity of the password:")
        print("1. Letters only")
        print("2. Letters and digits")
        print("3. Letters, digits, and special characters")
        
        complexity = input("Enter your choice (1/2/3): ")

        if complexity == '1':
            characters = string.ascii_letters
        elif complexity == '2':
            characters = string.ascii_letters + string.digits
        elif complexity == '3':
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            print("Invalid choice. Please select a valid option.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"\nGenerated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter numeric values for length.")

password_generator()
