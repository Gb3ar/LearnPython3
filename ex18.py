#Names, Variable, Code, Functions

#this one is like your scripts with argv 

def print_two(*args):
    argOne, argTwo = args
    print (f"argOne: {argOne}, argTwo: {argTwo}")

#ok, that *args is actually pointless, we can just do this

def print_two_again(argOne, argTwo):
    print (f"argOne: {argOne}, argTwo: {argTwo}")

#this just takes one argument 

def print_one(argOne):
    print(f"argOne: {argOne}")

#this one takes no arguments

def print_none():
    print("I got nothin")

print_two("Benjamin", "McTiernan")
print_two_again("Benjamin", "McTiernan")
print_one("First!")
print_none()