import os, time # Importing the necessary libraries

def cls(): # Function to clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

def wait(x): # Function to wait for x seconds
    time.sleep(x)

def choosepass():
    return input("Choose a password:")

def check_length(password):
    if len(password) >= 4:
        if len(password) <= 20:
            return True
        else:
            return False
        
def check_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False

def check_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False

def check_number(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def check_special(password):
    special_chars = "!@#$%^&*()-+"
    for char in password:
        if char in special_chars:
            return True
    return False

def password_checker(password):
    if check_length(password) == True:
        if check_uppercase(password) == True:
            if check_lowercase(password) == True:
                if check_number(password) == True:
                    if check_special(password) == True:
                        return True
    return False
def display_error(password):
    cls()
    if check_length(password) == False:
        print("Password must be between 4 and 20 characters long.")
    if check_uppercase(password) == False:
        print("Password must contain at least one uppercase letter.")
    if check_lowercase(password) == False:
        print("Password must contain at least one lowercase letter.")
    if check_number(password) == False:
        print("Password must contain at least one number.")
    if check_special(password) == False:
        print("Password must contain at least one special character.")
    wait(2)

def makepassmenu():
    cls()
    print("---------------------")
    print("| Choose a password |")
    print("---------------------")
    print("\n")
    print("conditions:")
    print("1. The password must be between 4 and 20 characters long.")
    print("2. The password must contain at least one uppercase and lowercase letter.")
    print("3. The password must contain at least one number.")
    print("4. The password must contain at least one special character.")
    print("\n")

def password_checker_true():
    cls()
    print("Password accepted!")
    wait(2)
    main()

def password_checker_false():
    cls()
    print("Password denied!")
    wait(2)
    main()

def main():
    makepassmenu()
    password = choosepass()
    if password_checker(password) == True:
        password_checker_true()
    else:
        display_error(password)
        password_checker_false()

main()