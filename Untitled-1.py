user_db = {
    'username':['Rakesh','Rahul'],
    'password':[1234,3456]
}



usern = input("Enter your username: ")
passw = input("Enter your password: ")

def create_user():
    C_user=input("Enter the Name")
    C_password=input("Enter the password")
    user_db["username"].append(C_user)
    user_db["password"].append(C_password)
    print("Account Created Successful")

for i in range(len(user_db['username'])):
    if usern==user_db['username'][i] and int(passw)==user_db['password'][i]:
        print("Welcone")
        break
    else:
        print("account created successfully")
        print("Create an account")
        create_user()  
        break  
