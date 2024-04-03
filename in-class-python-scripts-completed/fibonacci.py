#! /usr/bin/env python3


def get_input():
    # get the input
    number = input("Enter the number: ")
    return number


def fib(beyonce):
    # initialize our variables for calculating the Fibonacci number at this position in the sequence
    a,b = 0,1

    # one way to calculate the Fibonacci number
    for i in range(int(beyonce)):
        a,b = b,a+b

    # store the result so it's obvious
    fibonacci_number = a

    return fibonacci_number


def print_output(number, fibonacci_number):
    # print the output
    print('The Fibonacci number for', number, 'is:', fibonacci_number)


def main():
    # first get the input
    number = get_input()

    # calculate the fibonacci number
    fibonacci_number = fib(number)

    # print the output
    print_output(number, fibonacci_number)


# set the environment for this script
# is it main, or is this a module being called by another script
if __name__ == '__main__':
    main()