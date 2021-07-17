#assign 4 curly braces to variable
formatter = "{} {} {} {}"

#prints variable and injects 1234 with .format() function
print(formatter.format(1,2,3,4))

#prints variable and injects strings with .format() function
print(formatter.format("one", "two", "three", "four"))

#prints variable and injects bools with .format() function
print(formatter.format(True, False, False, True))

#prints variable and injects same variable with .format() function
print(formatter.format(formatter, formatter, formatter, formatter))

#prints variable and injects custom string with .format() function
print(formatter.format(
    "Hello", 
    "there.", 
    "I'm", 
    "Mike"
))

# Study Drill: Repeat drill 7
