#!/bin/python3

import re
# Restaurant names and cuisine types
api_response = "LaVILLA CAFE - Chinesse food"
pattern = r"^(.*?)\s-\s(.*?)$"
match = re.match(pattern, api_response)
if match:
    restaurant_name = match.group(1)
    cuisine_type = match.group(2)
    print("Restaurant Name:", restaurant_name)
    print("Cuisine Type:", cuisine_type)

# Social media usernames

username_string = "@LaVILLA007"
username = re.search(r'@([a-zA-Z0-9_]+)', username_string)
if username:
    print("Username:", username.group(1))


# Ingredient lists from recipes
    ingredient_list = "water,vegetable oil,honey,steak,green onions,ginger,baking soda,pepper"
ingredients = re.split(r',\s*', ingredient_list)
print("Ingredients:", ingredients)

# Product codes
product_code = "007LAVILLA"
pattern = r'^\d{3}[A-Z]+'

if re.match(pattern, product_code):
    print("Valid Product Code")
else:
    print("Invalid Product Code")

# News headlines

date_time_string = "Oct 02, 2023 - 05:30 PM"
pattern = r"([a-zA-Z]{3}\s\d{2},\s\d{4})\s-\s(\d{2}:\d{2}\s[APap][Mm])"
match = re.match(pattern, date_time_string)
if match:
    event_date = match.group(1)
    event_time = match.group(2)
    print("Event Date:", event_date)
    print("Event Time:", event_time)


