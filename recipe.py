import pytest

#[list of x] [list of x] -> [list of x]
#returns a list that is the intersection of both lists
def intersect(l1, l2):
	return [val for val in l1 if val in l2]

#test
assert intersect([1,2,3], [1,3]) == [1,3]
assert intersect([9],[]) == []
assert intersect(["hi", "1", "4"], ["hi", "1", "f"]) == ["hi", "1"]

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
			recipe_file = file.readlines()

		#reseting the ingredient list
		self.ingredient = []

		for val in recipe_file:
			#remove return characters
			val = val.strip()
			#split into individual words
			line = val.split()
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

		names1 = [r1.name for r1 in self.ingredient]
		names2 = [r2.name for r2 in recipe.ingredient]

		return len(intersect(names1, names2))