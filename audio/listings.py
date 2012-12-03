#listings.py for building preprocessed voice files for TVI 
#Writting By Gee Bartlett 

import os, sys



pprotext = ("Stand By","Recent Tweets","Recent Mentions","Main Menu","Options","Read Speed","Quick Read","Strip Web Address", "Voice Select","Number Of Tweets","Enable","Disable","5","10","20","Slow","Medium","Fast","Repeat Last Tweet","Continue","Return To Main Menu")
pprofile = ("standb.wav","rc_tweet.wav","rc_ment.wav","mainmen.wav","opts.wav","readsp.wav","quickrd.wav","stripweb.wav","voicesel.wav","numtw.wav","enab.wav","disab.wav","5.wav","10.wav","20.wav","slow.wav","med.wav","fast.wav","repeat.wav","continue.wav","rmainmen.wav")
#text and output file names for vocal preprocessing by festival 
voice = int(sys.argv[1])
print voice

if voice == 1:
	voicesel = '-eval "(voice_don_diphone)" '
if voice == 2:
	voicesel = '-eval "(voice_rab_diphone)" '

print voicesel
for x in range(0,18):
#debug lists
	print pprotext[x]
	print pprofile[x]

#debuging test
question = raw_input("Do What?")

def update_static_text(voice):
#edit range if extra files are need 
	for x in range(0,21):

#building command for bash
#build text file command  text to wave needs a text file to process from make string to create text file
		crtemptext = "echo " + pprotext[x] + " > streamtemp.txt" 
		#build text2wave command
		t2woutputst= 'text2wave ' + voicesel + "streamtemp.txt "  +"-o "+ pprofile[x]
		print "processing ",x
#run bash text file maker 
		os.system(crtemptext)
#run text2wave 
		os.system(t2woutputst)
		print "finished ",x 	
	print "done"
	return	

#more debug
if question == "hello":
	update_static_text(1)
   
	

