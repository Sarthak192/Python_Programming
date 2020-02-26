#No of digits in a number
def noOfDigits(no):
    count = 0
    while(no!=0):
        no = int(no/10)
        count = count+1
    return count

print(noOfDigits(18))