#!/bin/python3 
#  Social media usernames

import re 

username_string = "@LaVILLA007"
username = re.search(r'@([a-zA-Z0-9_]+)', username_string)
if username:
    print("Username:", username.group(1))
