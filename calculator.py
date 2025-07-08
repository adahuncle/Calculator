def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Division by zero."

while True:
	print("\nSelect operation: +, -, *, /, or 'q' to quit.")
	choice = input("Enter operation: ")

	if choice == 'q':
		break
	
	try:
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
	except ValueError:
		print("Invalid Input. Please enter numeric values.")
		continue

	if choice == '+':
		print("Result:", add(num1, num2))
	elif choice == '-':
		print("Result:", subtract(num1, num2))
	elif choice == '*':
		print("Result:", multiply(num1, num2))
	elif choice == '/':
		print("Result:", divide(num1, num2))
	else:
		print("Invalid operation.")