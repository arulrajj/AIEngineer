

def verify_password(pwd):
    correct_pwd = "openAI123"
    if(pwd == correct_pwd):
        return True
    else:
        return False


for i in range(3):
    pwd = input("Enter the password:")
    pwd_validation_flag = verify_password(pwd)
    if(pwd_validation_flag):
        print("Login Successful")
        break
if(pwd_validation_flag == False):
   print("Account Locked")

