print("welcome to the win or bust quiz you will be challenged with 3 questions")
print("If, you get 3 marks you win!!!")
name = input("What is your name?")

print("Hello " + name + ".")
marks = 0

answer_1 = int(input("1. What is the square root of 144?"))

if answer_1 == 12:
    print("1. Well Done you are still in!")
    marks = marks + 1

    answer_2 = int(input("2. What is the sum of the first 10 even numbers""."))
    if answer_2 == 110:
            print("2. Well Done you will pass to the next question!")
            marks = marks + 1
            answer_3 = int(input("What is 13 times 13?"))
            if answer_3 == 169:
                print("3. Well Done, now you will get your result ")
                marks = marks + 1
            else:
                print("Sorry, you failed in the last question, better luck next time!!!")
                print("Bye, please try again")
    else:
        print("2. Sorry, wrong answer!")
        print("Bye, please try again")
else:
    print("1. Sorry, wrong answer!")
    print("Bye, please try again")
print("You got " + str(marks) + " marks"".")


































































































