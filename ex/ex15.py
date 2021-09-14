#Imports argv from sys
from os import close
from sys import argv

#Assigns script and filename with argv
script, filename = argv

#Take filename variable, opens it, assigns the object contents to txt
txt = open(filename)

#Prints the filename 
print(f"Here's your file {filename}:")

#Takes the txt variable and uses read() functin to read the object
print(txt.read())

close(txt)

#Asks user for input
print("Type the filename again:")

#User input assigned to file_again
file_again = input("> ")

#Opens file_again and assigns to txt_again
txt_again = open(file_again)

#Reads txt_again with read() function
print(txt_again.read())

close(txt_again)