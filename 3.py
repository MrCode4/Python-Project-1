def cals(num1, num2, op):
	if op == "*":
		return num1*num2
	elif op == "/":
		return num1/num2;
	elif op == "-":
		return num1-num2;
	elif op == "+":
		return num1+num2;
		
num1 = int(input("Enter number1 : "))
num2 = int(input("Enter number2 : "))
op = input("Enter operator (* / + -): ")

print("The answer is: " + str(cals(num1, num2, op)))