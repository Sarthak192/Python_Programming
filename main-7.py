#Check LCM of two nos
print("Enter two numbers")
a = int(input())
b = int(input())
lcm = 0
if(a > b):
    lcm = a
else:
    lcm = b
while(1):
    if( lcm % a == 0 and lcm % b == 0 ):
        print("LCM of",a,"and",b,"is",lcm)
        break
    lcm = lcm + 1