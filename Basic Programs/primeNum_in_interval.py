# Program to print Prime Numbers in an interval

start, end = int(input("Enter start : ")), int(input("Enter end : "))

def checkPrime(num):
    count = 0
    for i in range(2, num//2+1):
        if num % i == 0:
            count += 1
    if count == 0:
        print(num)
while(start <= end):
    checkPrime(start)
    start += 1

# End