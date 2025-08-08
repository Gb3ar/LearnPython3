# assign values to variable 
types_of_people = 45
binary = "binary"
do_not = "don't"
x = f"There are {types_of_people} types of people."
y = f"Those who know {binary} and those who {do_not}."
w = "This is the left side of ...."
e = "a string with a right side."
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"


print(x)
print(y) 
print(f"I said:{x}" f"{y}" f"Then there was a problem because I kept trying to include more {w}")
print(f"I also said:'{y}'")
print(joke_evaluation.format(hilarious))
print(w + e)
print(x + y)