#Sum of n natural nos
def sum(n):
    sum = 0
    for i in range(1, n):
        sum = sum + i
    return sum
print(sum(10))