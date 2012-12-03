
from time import sleep
import os
import RPi.GPIO as GPIO
import sys 
GPIO.setmode(GPIO.BCM)
GPIO.setup(11, GPIO.IN)
GPIO.setup(9, GPIO.IN)
#GPIO.setup(18, GPIO.IN)
 
while True:
        print GPIO.input(11)
        if ( GPIO.input(11) == True ):
                print "1"
                sys.exit(2)
                
        if ( GPIO.input(9) == True):
                print "2"
                sys.exit(1)
        #if ( GPIO.input(18)== False):
                #print "3"
        sleep(0.5)
