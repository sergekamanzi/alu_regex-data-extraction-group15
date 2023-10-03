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
