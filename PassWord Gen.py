import secrets
import string


def password():
    # While loop for validate inputs till is correctly enter by the user
    while True:
        try:
            length = int(input("Please enter the length of the password (50 max): "))
            if 0 < length < 50:
                break
            else:
                print("The length of the password is too long. Please try again!")
        except:
            print("Must be a number.Try again!")
    while True:
        upper_case = input("Do you want implement upper case in your password(Y/N): ").lower()
        if upper_case == "y" or upper_case == "n":
            break
        else:
            print("You must enter \'y\' or \'n\'.")
    while True:
        digit = input("Do you want to implement digits into your password(Y/N): ").lower()
        if digit == "y" or digit == "n":
            break
        else:
            print("You must enter \'y\' or \'n\'.")
    while True:
        special = input("Do you want to implement special characters into your password(Y/N): ").lower()
        if special == "y" or special == "n":
            break
        else:
            print("You must enter \'y\' or \'n\'.")


    # Conditions for user's inputs for create the password
    if upper_case == "y" and digit == "y" and special == "y":
        alphabet = string.ascii_letters + string.digits + string.punctuation
    elif upper_case == "y" and digit == "n" and special == "y":
        alphabet = string.ascii_letters + string.punctuation
    elif upper_case == "y" and digit == "y" and special == "n":
        alphabet = string.ascii_letters + string.digits
    elif upper_case == "y" and digit == "n" and special == "n":
        alphabet = string.ascii_letters
    elif digit == "y" and upper_case == "n" and special == "n":
        alphabet = string.ascii_lowercase + string.digits
    elif special == "y" and digit == "n" and upper_case == "n":
        alphabet = string.ascii_lowercase + string.punctuation
    elif upper_case == "n" and digit == "y" and special == "y":
        alphabet = string.ascii_lowercase + string.digits + string.punctuation
    else:
        alphabet = string.ascii_lowercase

    # Create the password with the parameters chosen by the user
    pw = ''.join(secrets.choice(alphabet) for i in range(length + 1))

    return print(f"Here is your new password ==> {pw}")

password()

