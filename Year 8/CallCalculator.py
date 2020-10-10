from calculator import calculator

n1 = int(input("Enter a whole number"))
n2 = int(input("Enter another whole number"))
operation = input("Do you want to sub or add?").lower()
calculator(n1, n2, operation)