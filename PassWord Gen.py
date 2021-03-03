import secrets

def password():
    length = int(input("Please enter the length of the password: "))
    pw = secrets.token_hex(length)
    return print(f"Here your new password ==> {pw}")

