# Check Whether it is uppercase, lowercase, number or symbol
def check(ch):
    if(ord(ch)>=65 and ord(ch)<=90):
        print("Uppercase")
    elif(ord(ch)>=97 and ord(ch)<=122):
        print("Lowercase")
    elif(ord(ch)>=48 and ord(ch)<=57):
        print("Number")
    else:
        print("Symbol")
        
ch = input("Enter: ")
check(ch)



