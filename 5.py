def is_it_prime(num):
	if num == 1:
		return False
	if num == 2:
		return True
		
	for i in range(2, num):
		if (num % i) == 0:
			return False
			
	return True
		
def cals(num):
	answer = 1
	
	for i in range(num, 2, -1):
		if (num % i == 0) and is_it_prime(i):
			return i
		
		

number = int(input("Enter number: "))

print("The answer is: " + str(cals(number)))