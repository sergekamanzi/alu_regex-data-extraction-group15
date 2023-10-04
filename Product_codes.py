#!/bin/python3
# product code 

import re


product_code = "007LAVILLA"
pattern = r'^\d{3}[A-Z]+'

if re.match(pattern, product_code):
    print("Valid Product Code")
else:
    print("Invalid Product Code")
    
print("007LAVILLA")
