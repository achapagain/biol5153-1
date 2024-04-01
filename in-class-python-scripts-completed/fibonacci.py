#! /usr/bin/env python3

# get the input
number = input("Enter the number: ")

# initialize our variables for calculating the Fibonacci number at this position in the sequence
a,b = 0,1

# one way to calculate the Fibonacci number
for i in range(int(number)):
    a,b = b,a+b

# store the result so it's obvious
fibonacci_number = a

# print the output
print('The Fibonacci number for', number, 'is:', fibonacci_number)