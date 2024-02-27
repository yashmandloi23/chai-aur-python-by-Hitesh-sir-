# password strength checker
password = str(input("enter password: "))
password_length = len(password)

if password_length < 6:
    print("weak")
elif password_length <= 10:
    print("medium")
elif password_length >= 15:
    print("strong") 
