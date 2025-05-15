#research.py

import re 
line = "Cats are smarter than dogs" 

searchObj = re.search( r'smarter', line, re.M|re.I) 

if searchObj: 
	print ("searchObj.group() : ", searchObj.group()) 
else: 
	print ("No search found!!")