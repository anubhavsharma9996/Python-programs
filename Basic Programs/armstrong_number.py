# Program for Armstrong Number

def sum(digit, p):
    s  = pow(digit, p)
    return s

num = int(input("Enter a Number : "))
p = len(str(num))
l = num
finalSum = 0
while l > 0:
    print(l)
    finalSum += sum(l % 10, p)
    l //= 10
if finalSum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

# End
