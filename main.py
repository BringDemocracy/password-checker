import os, time # Importing the necessary libraries



def cls(): # Function to clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

def wait(x): # Function to wait for x seconds
    time.sleep(x)

def choosepass(): # Function to choose a password
    return input("Choose a password:")

def check_length(password): # Function to check if the password is between 4 and 20 characters long
    if len(password) >= 4:
        if len(password) <= 20:
            return True
        else:
            return False
        
def check_uppercase(password): # Function to check if the password contains an uppercase letter
    for char in password:
        if char.isupper():
            return True
    return False

def check_lowercase(password): # Function to check if the password contains a lowercase letter
    for char in password:
        if char.islower():
            return True
    return False

def check_number(password): # Function to check if the password contains a number
    for char in password:
        if char.isdigit():
            return True
    return False

def check_special(password): # Function to check if the password contains a special character
    special_chars = "!@#$%^&*()-+"
    for char in password:
        if char in special_chars:
            return True
    return False

def password_checker(password): # Function to check if the password meets all the requirements
    if check_length(password) == True & check_uppercase(password) == True & check_lowercase(password) == True & check_number(password) == True & check_special(password) == True:
        return True
    else:
        return False

def display_error(password): # Function to show which requirements the password does not meet
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

def makepassmenu(): # Function to display the menu of the program
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

def password_checker_true(): # Function to display that the password is valid
    cls()
    print("Password accepted!")
    wait(2)
    main()

def password_checker_false(): # Function to display that the password is invalid
    cls()
    print("Password denied!")
    wait(2)
    main()

def main(): # The main function of the program
    makepassmenu()
    password = choosepass()
    if password_checker(password) == True:
        password_checker_true()
    else:
        display_error(password)
        password_checker_false()

main()