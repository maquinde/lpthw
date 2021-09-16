from sys import argv

script, filename = argv

file = open(filename, "w")

file.read()
file.write("This is a test")
file.close()