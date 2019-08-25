# Program to find N-th FIbonacci Number

start, end = 0,1
num = int(input("Enter number : "))
if num == 1:
    print(start)
elif num == 2:
    print(end)
else:
    count = 0
    while True:
        fib = start + end
        start, end = end, fib
        count += 1
        if count == num - 2:
            print(fib)
            break
        
# End
