import hashlib
import time 

username = input("Enter your username")
password="password123!"

# print(f"Original password is: {password}")

password= password.encode()
hashed_pw=hashlib.sha256(password).hexdigest()
# print(f"Hashed PW is: {hashed_pw}")

tries =3
wait_time=5

successful=False

while tries>=1 and successful == False:
    attempt=input("Type in your password: ")
    attempt.attempt.encode()
    hashed_attempt=hashlib.sha_256(attempt).hexdigest()
    if hashed_attempt !=hashed_pw:
        # The user failed
        tries -=1
        print("Incorrect Username and/or Password. Try Again.")
        print("You have {tries} remaining")
    else:
        print("woah!")
