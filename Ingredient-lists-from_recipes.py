#!/bin/python3


# Ingredient lists from recipes
    ingredient_list = "water,vegetable oil,honey,steak,green onions,ginger,baking soda,pepper"
ingredients = re.split(r',\s*', ingredient_list)
print("Ingredients:", ingredients)
