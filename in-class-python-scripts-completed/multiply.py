#! /usr/bin/env python3

def get_input():
    
    # ask for the size of the multiplication matrix
    size = int(input("Enter the size of your table: "))

    return size

def print_table(n):

    # calculate how many spaces we'll need for the output of each cell in the matrix
    cell_width = len(str((n * n))) + 1

    # nested for loop to calculate i * j
    for i in range(1,n+1):
        for j in range(1,n+1):
            # nice formatted print statement for each cell
            print("{:>{cell_width}}".format(i * j, cell_width = cell_width), end='')
            # print("{:6d}".format(i * j), end='')

        # print a newline character at the end of each row
        print()


def main():
    input_num = get_input()

    print_table(input_num)


# set the environment for this script
# is it main, or is this a module being called by another script
if __name__ == '__main__':
    main()