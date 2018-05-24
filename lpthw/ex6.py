
types_of_people = 10

# converts the variable of 10 to a string with the rest of the string
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "dont't"

y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# this take the variable string and adds the other variable in as a string with the {} is at
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
