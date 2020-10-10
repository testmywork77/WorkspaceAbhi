# Else if syntax task
# Correct the syntax on the program below


#Task 1
# This program should award grade A for scores over 40, B for scores over 30,
# C for scores over 20 and D for 20 or less

score = int(input("What score did you get on the test? "))
if score > 40:
    grade = "A"
elif score > 30:
    grade = "B"
elif score > 20:
    grade = "C"
elif score <= 20:
    grade = "F"
print("You got a grade", grade)



# Task 2
# This program gives a different answer depending what the user inputs.

superhero = input("Who is your favourite superhero? ").lower()
if superhero == "superman":
    print("Really Superman?")
    print("You know he's scared of the dark right?")
elif superhero == "goku":
    print("Nice choice.")
print("Gotta love a Dragonball Z hero.")
print("I'm not sure I know", superhero)



# Task 3
# This program checks a score in a quiz against the three stored highscores
# and outputs whether it is top score, second, third or not in the high scores

highscore1 = 25
highscore2 = 17
highscore3 = 13
score = 17
if score > highscore1:
    print("Top score")
elif score > highscore2:
    print("Second - well done.")
elif score > highscore3:
    print("3rd place - not bad.")

else:
    print("Sorry you didn't make a highscore this time.")




# Task 4
# This program should take a users waist size and store the size of belt
# they will need. Anyone with a waist size of less than 50cm is small, and
# a waist size of 70 or more is large.  in between is medium.

waist_size = int(input("Enter your waist size in cm"))
if waist_size < 70:
    belt_size = "large"
elif waist_size < 50:
    belt_size = "medium"
else:
    belt_size = "small"
print("Your belt size is", belt_size)



# Task 5
# This program works but can be simplified so it doesn't need to use the
# AND operator.  It should award 1 ticket for 10 or less points, 2 tickets
# for 11 - 20 points and 5 tickets for more than 20 points.

points = int(input("How many points were scored playing the game?"))
if points <= 10:
    tickets = 1
elif points <= 20:
    tickets = 2
else:
    tickets = 5
print(tickets)

