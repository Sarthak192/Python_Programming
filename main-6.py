#Swap two nos
def swapNos(a, b):
    a = a+b
    b = a-b
    a = a-b
    print(a,b)
a = input("Enter first number")
a1 = int(a)
b = input("Enter second number")
b1 = int(b)
swapNos(a1,b1)    
    
