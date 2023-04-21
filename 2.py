def calc(reshte):
	words = reshte.split(" ")
	
	ans_word = ""
	size = 0;
	
	for word in words:
		if len(word) > size:
			size = len(word)
			ans_word = word
			
	print("The answer is: " + ans_word)

reshte = input("Enter string:")

calc(reshte)