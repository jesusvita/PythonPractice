# take down information and place them in varaibles
name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# print out the variables with text and stuff
print(f"Let's talk about {name}.")
print(f"He's {height}inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
print(f"This is your height in centimeters: ", height * 2.54)
print(f"This is your weight in kilograms: ", weight * (1 / 2.2))
