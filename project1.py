# Hi this is my first ever semi complex python project. 

print("HELLO USER")
print("A.SIGN UP \nB.LOG IN")

Option=input("Enter your choice of option:")

if(Option=="A"): 

    userId=input("Create your user ID:")

    #checking if the user id already exist or not
    with open('sample.txt','r') as file:
        ids=file.read()
        if userId not in ids:

            with open('sample.txt','a') as file:
                file.write(userId)
                file.write(",")
                Password=input("Enter your password:")
                file.write(Password)
                file.write("\n")
                
        else:
            print("THIS USER ID ALREADY EXIST")
                     
elif(Option=="B"):  

    userId=input("Enter your user ID:")
    Password=input("Enter your password:")

    with open('sample.txt','r') as file:
        ids1=file.read()
        if userId not in ids1:
            print("THIS ID DOES NOT EXIST, KINDLY SIGN UP FIRST!")
        else:
            newids=ids1.split("\n")
            for id in newids:
                temp=id.split(',')
                user=temp[0]
                code=temp[1]
                if userId==user:
                    if Password==code:
                        print("LOGIN SUCCESFUL!")
                    else:
                        print("Incorrect password")         
            
            
