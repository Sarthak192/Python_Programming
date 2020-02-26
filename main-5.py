#Check whether number is odd or even
def check_odd_even(no):
    if(no%2==0):
        print("No is even")
    else:
        print("No is odd")
        
no = input("Enter number")
nos = int(no)
check_odd_even(nos)