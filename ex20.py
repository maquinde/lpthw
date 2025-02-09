# imports argv from sys
from sys import argv

# sets a file name to a variable (file was previously created)
input_file = "ex20_test.txt"

# function to take in a argument and read the files contents 
def print_all(f):
    print(f.read())

# function to change the files pointer to the beginning of the file
def rewind(f):
    f.seek(0)

# function to print the line entered in the argument, for the current file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# opens the input file variable and assigns it to another variable
current_file = open(input_file)

print("First let's print the whole file:\n")

# uses the print all function to print the input file variable
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# resets the position of the file handle to the beginning of the file
rewind(current_file)

print("Let's print three lines:")

# sets current line to 1
current_line = 1

# prints current line of the current file 
print_a_line(current_line, current_file)

# updates the current line +1
current_line += 1

# prints current line of the current file 
print_a_line(current_line, current_file)

# updates the current line +1
current_line += 1

# prints current line of the current file 
print_a_line(current_line, current_file)