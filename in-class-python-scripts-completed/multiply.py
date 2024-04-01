#! /usr/bin/env python3

# ask for the size of the multiplication matrix
size = int(input("Enter the size of your table: "))

# calculate how many spaces we'll need for the output of each cell in the matrix
cell_width = len(str((size * size))) + 1

# nested for loop to calculate i * j
for i in range(1,size+1):
    for j in range(1,size+1):
        # nice formatted print statement for each cell
        print("{:>{cell_width}}".format(i * j, cell_width = cell_width), end='')
        # print("{:6d}".format(i * j), end='')

    # print a newline character at the end of each row
    print()
