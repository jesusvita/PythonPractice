import re

def passwordChecker(password):
    if len(password) < 8:
        print('Password must be longer than 8 characters.')
        return False
    elif not re.search(r'[A-Z]', password):
        print('Password needs atleast 1 uppercase character.')
        return False
    elif not re.search(r'[a-z]', password):
        print('Password needs atleast 1 lowerscase character.')
        return False
    elif not re.search(r'[0-9]', password):
        print('Password needs atleast 1 digit.')
        return False
    else:
        return True


passwordStrength = False

while not passwordStrength:
    password = input('Please enter a password: ')
    passwordStrength = passwordChecker(password)
