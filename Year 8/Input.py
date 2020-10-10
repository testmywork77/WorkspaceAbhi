# Receiving input
# Read the scenarios.  You need to decide on an appropriate variable name
# and get some input from a user.  You will then need to decide if it needs to
# be cast to do what you are asked to do and provide the required output.

# 1. Ask the user for their name.  Output a message that includes the name
# the user enters e.g. if they are called Bob it might output "Hello Bob".
name = input("What is your name?")
print("Hello " + name)

# 2. Ask the user for their age.  Calculate what their age will be in 10 years
# and print out a message to say how old the user will be in 10 years.
age = int(input("What is your age?"))
print(name + " will be " + str(age) + " in 10 years.")

# 3. Ask the user how many pies they want to buy, then ask them how much a pie
# costs.  The program should then say how much it will cost for the number of
# pies that were entered.
pies = int(input("How many pies do you want to buy?"))
cost = int(input("What is the cost of each pie?"))
total_cost = pies * cost
print("Total Pies " + str(pies))
print("Each pie costs " + str(cost) + " pounds")
print(str(pies) + " pies will cost " + str(total_cost) + " pounds.")

# 4. Write a program that will split the bill for people at a restaurant.  You
# will need to get the total value of the bill as well as the number of people
# at the meal from the user.  the program should output the amount each person
# should pay.
total_value = int(input("What is the total value of the bill?"))
people = int(input("How many people would we serve?"))
cost = int(total_value / people)
print("The total Value is " + str(total_value) + " pounds")
print("There are " + str(people) + " people")
print("Each person should pay " + str(cost) + " pounds.")
