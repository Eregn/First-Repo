import re

def strength():
    password = input("Please insert your password here: ")
    digit_error = re.search(r"\d",password) is None
    upper_case_error = re.search(r"[A-Z]",password) is None
    special_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]' ,password) is None
    password_verygood = not digit_error and not upper_case_error and not special_error
    password_ok = not digit_error or not upper_case_error or not special_error
    if len(password) > 8:
        if password_verygood:
            print("Password very strong. Good job!")
        elif len(password) > 20 and password_ok:
            print("Password strong. Well done!")
        elif password_ok:
            print("Password correct. Could be better!")
        else:
            print("Password weak. Please review for a better security.")
    else:
        print("The password is too short.")

strength()
