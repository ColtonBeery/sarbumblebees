
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
pir=8
led=10
GPIO.setup(pir,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
while True:
    i=GPIO.input(pir)
    if i==0:
        print ("No person detected")
        GPIO.output(led,0)
        time.sleep(1)
    elif i==1:
        print ("Person detected!")
        GPIO.output(led,1)
        time.sleep(1)
        
            
