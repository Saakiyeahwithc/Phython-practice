# Python program to check if the input number is prime or not
 #num = 407
 # take input from the user
num = int(input("Enter a number: "))
 # prime numbers are greater than 1
if num > 1:
    rem=1
    for i in range(2,num):
        rem=num%i
        if rem == 0:
            break
    if rem == 0:
        print(num,"is not a prime number")
    else:
        print(num,"is a prime number")
 # if input number is less than
 # or equal to 1, it is not prime
else:
    print(num,"is not a prime number")