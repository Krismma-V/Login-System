import re
file=open("registration.txt","w")
text = [{"username"," ","\t","password"," ","\n"}]
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
def check(username):
    if (re.search(regex,username)):
        file.write(username+" ")
    else:
        print("Invalid email")
username=input()
check(username)
def checkin(password):
    if len(password) > 5 and len(password) < 16:
        if (char.isdigit() for char in password):
            if (char.isupper() for char in password):
                if(char.islower() for char in password):
                    file.write("\n"+password+" ")
                else:
                    print("Invalid password")
            else:
                print("Invalid password")
        else:
            print("Invalid password")
    else:
        print("Invalid Password")
password=input()
checkin(password)
def login(username,password):
    if (username,password)==text:
        print("Login")
    else:
        print("username or password is invalid")









