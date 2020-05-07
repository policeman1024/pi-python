import RPi.GPIO as GPIO
import time




GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
'''while (input() == False)'''#This is a comment
print ("LED ON")
GPIO.output(17,GPIO.HIGH)
time.sleep(1)
print ("LED OFF")
GPIO.output(17,GPIO.LOW)
a=input()
print a
