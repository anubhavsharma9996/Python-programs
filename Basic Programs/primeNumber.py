# Program to check Prime Number

def checkPrime(num):
    if num > 1:
        for i in range(2, num//2):
            if num % i == 0:
                print("Number Not Prime")
                break
        else:
            print("Number is Prime")
    else:
        print("Number is Not Prime")

num = int(input("Enter a number : "))
checkPrime(num)

# End