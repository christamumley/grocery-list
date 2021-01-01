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

list_recipe = []

for filename in os.listdir("recipes"):
	#assumes file name is recipe name
	rec = Recipe(remove_ex(filename)) 
	rec.recipe_read("recipes/" + filename)
	list_recipe.append(rec)

for i in list_recipe:
	print(i.to_string())



