# While loop
i = 1
while i < 6:
    print(i)
    i +=1
	
# While loop with break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break;
    i +=1
	
# While loop with continue statement
i = 0
while i < 6:
    i +=1
    if i == 3:
        continue
    print(i)

# While loop with else statement
i = 1
while i < 6:
    print(i)
    i +=1
else:
    print( i, " is no longer less than 6")
	
***===============================================================***
#Abhi Homework

#46:
# While loop
number = int(input("Enter number: "))
while number < 5:
    number = int(input("Enter number: "))
else:
    print("The last number you entered was", number)
    print("where ",number," is the number the user entered that is over 5.")

#47:
Ask the user to enter a number and then a second number. Add these together and store the total. Then ask the user if they want to add another number. If they answer "y" then let the user input another number and add it to the total. The program should keep asking if they want to add another number and lettig them until they don't answer "y" to would you like to add another number. Once the user finishes adding numbers output:

The total is [total]

where [total] is the total of all the numbers the user has entered.

#Solution:
	firstNumber = int(input("Enter first number: "))
	secondNumber = int(input("Enter second number: "))
	total = firstNumber + secondNumber
	answer = input("Do you want to add another number, enter y/n: ").lower();
	while answer == "y":
		anotherNumber = int(input("Enter another number:" ))
		total = total + anotherNumber
		answer = input("Do you want to add another number, enter y/n: ").lower();
	else:
		print("The total is",total)
		print("where",total, " is the total of all the numbers the user has entered.")
	
#Output:
	Enter first number: 1
	Enter second number: 2
	Do you want to add another number, enter y/n: y
	Enter another number:3
	Do you want to add another number, enter y/n: y
	Enter another number:4
	Do you want to add another number, enter y/n: n
	The total is  10
	where  10  is the total of all the numbers the user has entered.
	
#49


