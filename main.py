from recipe import *
import os
import pytest

#String -> String
#removes the extension from the filename
def remove_ex(str):
	result = ""
	for i in range(0, len(str)):
		if(str[i] != '.'):
			result += str[i]
		else:
			return result
	return result

#test
assert remove_ex("test.text") == "test"
assert remove_ex("") == ""
assert remove_ex("none") == "none"

#-------------------------------------------------------
#grabbing recipes
list_recipe = []

for filename in os.listdir("recipes"):
	#assumes file name is recipe name
	rec = Recipe(remove_ex(filename)) 
	rec.recipe_read("recipes/" + filename)
	list_recipe.append(rec)

#printing recipe names 
i = 1; 
names = []
for rec in list_recipe:
	names.append(rec.name)
	print(rec.name + " ", end="")
	if(i % 6 == 0):
		print("")
	i += 1

#checking valid recipe
recipename = None
while(recipename == None):
	recipename = input("\nChoose from recipes:")
	if(recipename in names):
		break
	else:
		recipename = None

#grabbing recipe from list
recipe = None
for r in list_recipe:
	if(r.name == recipename):
		recipe = r
		break

#removing the choosen recipe from the list
list_recipe.remove(recipe)

#sorts in increasing order of % similar
list_recipe = sorted(list_recipe, key=lambda r: (r.in_common(recipe)/len(r.ingredient)))

#outputs the recipes that are most similar
amount = -1
while(amount < 0 or amount > len(list_recipe) + 1):
	amount = int(input("How many recipes including this one?"))

result = []
for i in range(1, amount):
	result.append(list_recipe.pop())

print("\nsimilar recipes:")

for r in result:
	print(r.to_string())

#generates a shopping list

#adding the choosen recipe back into the result
result.append(recipe)

#puts common ingredients into a dictionary
ingredients = {} 
for r in result:
	for i in r.ingredient:
		amt = ingredients.get(i.name)
		if(amt):
			ingredients[i.name] = amt + " + " + str(i.amount) + " " + i.denom + " "
		else:
			ingredients[i.name] = str(i.amount) + " " + i.denom + " "

#outputting to file and printing ingredients
with open("output.txt", "w") as file:
	file.write("Recipes:")
	print("\nRecipes: ")
	for r in result:
		file.write(r.name + " ")
		print(r.name + " ", end = "")
	print("")

	file.write("\n\nIngredients: \n")
	print("\ningredients:")
	for i in ingredients.keys():
		file.write(i + ": ")
		file.write(ingredients[i])
		file.write("\n")
		print(i + ":"  + ingredients[i])

input("\ntype anything to quit")








