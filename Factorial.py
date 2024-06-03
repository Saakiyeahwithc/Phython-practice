def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        print("Factorial of negative number cannot be found!")
    else:
        return num * factorial(num - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial of negative number cannot be found!")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", num, "is", factorial(num))
