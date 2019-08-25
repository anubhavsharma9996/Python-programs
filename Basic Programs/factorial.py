# Program for factorial of a number

def factorial(num):
    return 1 if(num == 0 or num == 1) else num * factorial(num - 1) # recursion

num = int(input("Enter a number"))
print(factorial(num))

# End5
