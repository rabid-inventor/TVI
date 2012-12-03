import os, string
from time import sleep


#load the gpio sub program it has to be run in super user mode 
#that would normally make a mess of the twidge settings
def gpiocheck():
	responce= os.system("sudo python gpio.py")
	print "gpio return" + str(responce)
	return responce

#Dowload recent tweet to text file rcup.txt at path	
def downloadrctweets(path):
	down1 = "twidge lsrecent > " + path + "rcup.txt" 
	print down1
	os.system(down1)
	print "current feed downloaded"

# download recent relpies from twidge and save text to selected path
def downloadreplies(path):
	down1= "twidge lsreplies > " + path +  "repup.txt"
	print down1
	os.system(down1)
	print "replies feed downloaded"

def mainmenu():
	os.system("aplay mainmen.wav")
	sleep(1)
	os.system("aplay rc_tweet.wav")
	ops = gpiocheck()
	#print ops
	if ops == 512:
		os.system("aplay standb.wav")
		downloadrctweets("temp/")
		rccout = devideup(temppath+"rcup.txt")
		postpro(rccout)
		tweetread("temp/ppf",1)
	os.system("aplay rc_ment.wav")
	ops =gpiocheck()
	if ops == 512:
		os.system("aplay standb.wav")
		downloadreplies("temp/")
		rccout = devideup(temppath+"repup.txt")
		postpro(rccout)
		tweetread("temp/ppf",1)
	os.system("aplay opts.wav")
	ops =gpiocheck()
	if ops == 512:
		os.system("aplay disab.wav")
	mainmenu()


def devideup(inputfilepath):
	
	outfile = 0
	startfile=0
	f=open(inputfilepath,'r')
	for line in f:
		#print line
		if line.find("<") == 0:
			#print "move"
			#print line.find("<")
			startfile +=1
			outfile =  "temp/ppf" + str(startfile) + ".txt"
			#print outfile 
			output = open(outfile,'w')
		output.write(line)
		#print startfile
	output.close() 
  	return startfile
	


def cleanup(numtext,remove,replace):
	#print numtext
	cleanfile = "ppf" + str(numtext) + ".txt"
	command = "cat " + temppath + cleanfile + " | sed  's/" + remove + "/" + replace + "/'  >  "  + cleanfile 
	#print command
	os.system(command)
	command = "cp " + cleanfile + " " + temppath + cleanfile
	#print command
	os.system(command)





def postpro(itemstoprocess):
	for numb in range(itemstoprocess):
		cleanup(numb,"<"," ")
		cleanup(numb,">","  tweeted:  ")
		cleanup(numb,"http"," Untranlated weblink")
		#cleanup(numb,"[",":")
		#cleanup(numb,"]",":")


def tweetread(opts,number):
	commandread = "festival --tts " + opts + str(number) + ".txt"
	#print commandread
	os.system("cat " + opts + str(number) +".txt")
	os.system(commandread)
	submenu(number)
	return

def submenu(currentitem):
	os.system("aplay repeat.wav")
	smselect = gpiocheck()
	if smselect == 512:
		print currentitem
		os.system("aplay standb.wav")
		tweetread("temp/ppf",currentitem)
	os.system("aplay continue.wav")
	smselect = gpiocheck()
	if smselect == 512:
		print currentitem
		os.system("aplay standb.wav")
		tweetread("temp/ppf",currentitem +1)
	os.system("aplay rmainmen.wav")
	smselect = gpiocheck()
	if smselect == 512:
		print currentitem
		mainmenu()
	
	submenu(currentitem)
	
	
		
	return 


temppath = "temp/" 
currentfeeditem = 1
rccount = 1
#downloadrctweets("temp/")
while True:
	mainmenu()

#tweetread("temp/ppf",1)

#downloadrctweets("temp/")
#downloadreplies("temp/")

