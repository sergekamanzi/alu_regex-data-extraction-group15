#!/bin/python3


import re

# Ingredient list from recipes
ingredient_list = "water,vegetable oil,honey,steak,green onions,ginger,baking soda,pepper"
ingredients = re.split(r',\s*', ingredient_list)
print("Ingredients:", ingredients)
