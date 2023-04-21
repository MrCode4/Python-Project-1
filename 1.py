my_list = input("Enter a list of numbers: ").split(" ")
z = int(input("Enter a number z: "))

# Convert list elements to integers
my_list = [int(num) for num in my_list]

out_list = []
for i in range(0, len(my_list)):
	for j in range(i+1, len(my_list)):
		for k in range(j+1, len(my_list)):
			if my_list[i]+my_list[j]+my_list[k] == z:
				new_list = {my_list[i], my_list[j], my_list[k]}
				out_list.append(new_list)

print(out_list)
			