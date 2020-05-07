import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

for i in range (0,3):
#while (input() == True):
    #GPIO.output(7,True)
    print ('LED_ON')
    time.sleep(1)
    #GPIO.output(7,False)
    print ('LED_OFF')
    time.sleep(1)
GPIO.cleanup() 

