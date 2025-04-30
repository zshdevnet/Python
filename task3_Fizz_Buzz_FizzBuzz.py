'''
Write a Python program that prints numbers from 1 to 20, but:
    For numbers divisible by 3, print "Fizz" instead.
    For numbers divisible by 5, print "Buzz" instead
    For numbers divisible by both 3 and 5, print "FizzBuzz".
    For all others, print the number itself.

'''

def fizzbuzz(number1, number2):
    for i in range(number1,number2+1):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)

try:
    number1 = int(input("From Number: "))
    number2 = int(input("To Number: "))
    fizzbuzz(number1, number2)
except:
    print("Wrong format input")