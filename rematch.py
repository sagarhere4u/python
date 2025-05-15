#rematch.py
import re 
line = "Cats are smarter than dogs" 

#. --> Any Single Character
#* --> One or More of preceding characters
#.* --> Any length of string 

matchObj = re.match( r'(.*) are (.*?) (.*)', line, re.M|re.I) 

#(.*) are (.*?) .*
#Cats are smarter than dogs
#(.*)  --> Cats 
#are --> are   
#nongreedy  
#(.*?)  --> smarter 
#.* --> than dogs 

if matchObj: 
	print ("matchObj.group() : ", matchObj.group()) 
	print ("matchObj.group(1) : ", matchObj.group(1))
	print ("matchObj.group(2) : ", matchObj.group(2))
	print ("matchObj.group(3) : ", matchObj.group(3))
else: 
	print ("No match!!")