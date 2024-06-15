import string
import random

def get_password_length():
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            return length
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_character_set():
    character_set = ""
    while True:
        print('''Choose character to set for password from these options: 
                1. Letters
                2. Digits
                3. Special characters
                4. Done''')
        choice = input("Pick a number (1-4): ")
        if choice == '1':
            character_set += string.ascii_letters
        elif choice == '2':
            character_set += string.digits
        elif choice == '3':
            character_set += string.punctuation
        elif choice == '4':
            if character_set:
                break
            else:
                print("Please select at least one character set.")
        else:
            print("Please select a valid option (1-4)!")
    return character_set

def generate_password(length, character_set):
    if len(character_set) < length:
        print("Warning: Character set is smaller than the password length. Some characters will repeat.")
    
    password = ''.join(random.sample(character_set, length))
    return password

def main():
    length = get_password_length()
    character_set = get_character_set()
    password = generate_password(length, character_set)
    print(f"The random password is: {password}")

if __name__ == "__main__":
    main()
