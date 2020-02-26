#Greatest of three nos
def largeNumber(a,b,c):
    if(a>b and a>c):
        print(a)
    elif(b>a and b>c):
        print(b)
    else:
        print(c)
largeNumber(2,4,6)