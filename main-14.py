#Sum of digits in a number
def sum_of_digits(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n/10)
    return sum

n = int(input("Enter a number : "))
print(sum_of_digits(n))