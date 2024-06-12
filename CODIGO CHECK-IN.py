import random

def create_code(name, letters_numbers):
    code = name + "-"
    for i in range(6):
        code += str(random.choice(letters_numbers))
    print(code)


if __name__ == "__main__":
    name = input("Enter your name: ").capitalize()
    letters_numbers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    create_code(name[0], letters_numbers)
