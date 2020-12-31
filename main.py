
with open("recipe_list.txt", newline='') as file:
	recipe_index = file.readlines()

index = 0
for val in recipe_index:
	recipe_index[index] = val.strip()
	index += 1




