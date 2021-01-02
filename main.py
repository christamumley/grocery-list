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
i = 0; 
names = []
for rec in list_recipe:
	names.append(rec.name)
	print(rec.name + " ", end="")
	if(i == 5):
		print("\n")

#checking valid recipe
recipename = None
while(recipename == None):
	recipename = input("\nchoose from recipes:")
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

#sorts in order from least similar to most similar
list_recipe = sorted(list_recipe, key=lambda r: r.in_common(recipe))

#outputs the recipes that are most similar
result = []

amount = input("How many recipes?")
for i in range(0, amount):
	result.append(list_recipe.pop())

print("\nsimilar recipes:")

for r in result:
	print(r.to_string())

#generates a shopping list
print("\nNecessary ingredients/amounts:")

ingredients = {} 
for r in result:
	for i in r.ingredient:
		amt = ingredients.get(i.name)
		if(amt):
			ingredients[i.name] = amt + " + " + str(i.amount) + " " + i.denom + " "
		else:
			ingredients[i.name] = str(i.amount) + " " + i.denom + " "

for i in ingredients.keys():
	print(i + ": ", end = "")
	print(ingredients[i])

input("type anything to quit")








