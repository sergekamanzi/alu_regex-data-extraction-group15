product_code = "007LAVILLA"
pattern = r'^\d{3}[A-Z]+'

if re.match(pattern, product_code):
    print("Valid Product Code")
else:
    print("Invalid Product Code")
