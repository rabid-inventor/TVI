#listings.py for building preprocessed voice files for TVI 
#Writting By Gee Bartlett 

import os


menuitems = ("Stand By","Recent Tweets","Recent Mentions","Main Menu","Options","Read Speed","Quick Read","Strip Web Address", "Voice Select","Number Of Tweets","Enable","Disable","5","10","20","Slow","Medium","Fast")
print "please select" 
for item in menuitems:
	print item
inopt = raw_input("select")

if inopt == 1:
	os.system("python processing.py recent")
 		
	

