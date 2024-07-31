import random
import string

def generate_password(length=12):
    # Define character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Ask user for the length of the passwords
    while True:
        try:
            password_length = int(input("Enter desired password length (minimum 1): "))
            if password_length < 1:
                raise ValueError("Length must be at least 1.")
            break
        except ValueError as e:
            print(e)
    
    # Generate and print at least 10 passwords with indices
    num_passwords = 10
    print(f"Generating {num_passwords} passwords of length {password_length}:")
    for i in range(1, num_passwords + 1):
        password = generate_password(length=password_length)
        print(f"{i}) {password}")

# Run the main function
if __name__ == "__main__":
    main()
