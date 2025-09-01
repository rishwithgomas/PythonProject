num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

give_oparator = input("give oparator: ")
if give_oparator == "+":
    print(f"the addition of 2 numbers is {num1 + num2}.")
elif give_oparator == "-":
    print(f"the subtraction of 2 numbers is {num1 - num2}.")
elif give_oparator == "*":
    print(f"the multiplication of 2 numbers is {num1 * num2}.")
elif give_oparator == "/":
    print(f"the division of 2 numbers is {num1 / num2}.")
else:
    print("Invalid input.")