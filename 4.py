def cals(list, splitter):
	final_string = ""
	for reshte in list:
		new_list = reshte.split(splitter)
		for new_reshte in new_list:
			if final_string == "":
				final_string = new_reshte
			else:
				final_string = final_string + splitter + new_reshte
	
	return final_string
		

list = input("list of strings: ").split(" ")
splitter = input("Enter splitter: ")

print("The answer is: " + cals(list, splitter))