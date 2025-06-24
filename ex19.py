#FUNCTIONS AND VARIABLES

# Defines the function and variables
def cheese_and_crackers(cheese_count, box_of_cracker):
    print (f"You have {cheese_count} cheeses!")
    print (f"You have {box_of_cracker} boxes of crackers!")
    print ("Man that's enough for a party!")
    print ("Get a bucket .\n")

#Assign value to the variable directly in the function
print ("we can just give the function numbers directly:")
cheese_and_crackers(20,30)

#type out the variable names = value then using them in the function
print ("OR, we can use variable from our script:")
amount_of_cheese = 10
amount_of_cracker = 50

cheese_and_crackers(amount_of_cheese, amount_of_cracker)

#Same as but with math 
print("We can even do math inside too:")
cheese_and_crackers (10 + 20, 5 + 6)

#Same but with variable and math
print("And we can combine the two, variable and math")
cheese_and_crackers (amount_of_cheese + 100, amount_of_cracker + 1000)

print ("Thank you for your participation and now your responsible for the constipation")

#define a new function

def time_and_space (time, space):
    print (f"This is the {time} time of day we need to get started and the {space} place we need to be")

time_and_space (10,8141)

print ("This is the newest way to tell time and space apart")

time = '10:52'
space = "The pool"

time_and_space ( time, space)

print (">>>>>>>>>>>>", repr)