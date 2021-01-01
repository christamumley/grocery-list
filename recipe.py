import pytest

#Ingredient that has a name, amount, and amount denomination 
class Ingredient:
	def __init__(self, name, amount, denom):
		self.name = str(name)
		self.amount = float(amount)
		self.denom = str(denom)

	#Recipe -> String
	#converts the Ingredient to a string 
	def to_string(self):
		result = self.name + " "
		result += str(self.amount) + " "
		result += self.denom + "\n"
		return result

#Represents a recipe with a name and a list of Ingredient
class Recipe:
	def __init__(self, name):
		self.name = str(name)
		self.ingredient = []

	#Recipe String -> Void 
	#takes in a string representing the filename, 
	#reads the file, and populates the fields of
	#self with the data in the file. 
	def recipe_read(self, filename):

		#opening file
		with open(filename) as file:
			recipe_index = file.readlines()

		#reseting the ingredient list
		self.ingredient = []

		index = 0
		for val in recipe_index:
			#remove return characters
			recipe_index[index] = val.strip()
			#split into individual words
			line = recipe_index[index].split()
			#if line empty
			if(len(line) == 0):
				continue
			#don't interpret links or comments
			if(line[0] == "link" or line[0] == "#"):
				continue
			#check if ingredients are complete
			if(len(line) < 3): 
				raise Exception("Incomplete Ingredient in file " + filename + " at line " + str(index + 1))
			#add ingredient to list
			self.ingredient.append(Ingredient(line[0], line[1], line[2]))

			index += 1

	#Recipe -> Recipe 
	#adds ingredient to the ingredient list
	def add_ingredient(self, ingredient):
		self.ingredient.append(ingredient)

	#Recipe -> String
	def to_string(self):
		result = str(self.name) + "\n"
		for i in self.ingredient:
			result += i.to_string()
		return result

	#Recipe Recipie -> int
	#takes in two recipes and returns the number of
	#Ingredients that the two recipes have in common
	def in_common(self, recipe):
		return_num = 0

		index = 0
		for i in self.ingredient:
			i2 = recipe.ingredient[index]

			if(i.name == i2.name):
				return_num += 1

			index += 0

		return return_num


	#String->File
	#takes in a String representing the file to be
	#written, writes 
	#def write(filename):

#Examples + testing
#------------------------------------------------------------------
#Recipe("test-toast")

#------------------------------------------------------------------
