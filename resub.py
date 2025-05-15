#resub.py

import re 
phone = "2004-959-559 # This is Phone Number" 

# Delete Python-style comments 
num = re.sub(r'#.*$', "", phone) 
print ("Phone Num : ", num)

num1 = re.sub(r'\D', "", num)
print("Phone Num: ", num1)