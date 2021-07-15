#assigns 10 to types_of_people and assigns a string to x calling the variable
types_of_people = 10
x = f"There are {types_of_people} types of people."

#created 2 variables and assined strings to them
binary = "binary"
do_not = "don't"

#assigned string calling 2 variables to y
y = f"Those who know {binary} and those who {do_not}."

#print x and y
print(x)
print(y)

#print strings calling x and y
print(f"I said: {x}")
print(f"I also said: '{y}'")

#create 2 variables, 1 with a bool and another with a string with empty curly brace
hilarious = False
joke_evaluation = "Isn't that joke funny!? {}"

#prints variable and injects variable into string with the .format() function
print(joke_evaluation.format(hilarious))

#assigns string to w and e
w = "This is the left side of..."
e = "a string with a right side."

#prints w and e
print(w + e)