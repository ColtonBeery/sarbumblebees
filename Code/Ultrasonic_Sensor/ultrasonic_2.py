# -----------------------
# Import required Python libraries
# -----------------------
from __future__ import print_function
import time
import RPi.GPIO as GPIO

# -----------------------
# Define some functions
# -----------------------
def measure():
  # This function measures a time
  GPIO.output(GPIO_TRIGGER, True)
  # Wait 10us
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  
  # My attempt to port pulseIn(URECHO, LOW) from arduino,
  # which measures how long the low pulse is and returns the time
  
  #Timer counts from start to end of low pulse ------______----- 
  while GPIO.input(GPIO_ECHO)==1:
    start = time.time() 

  while GPIO.input(GPIO_ECHO)==0:
    stop = time.time()

  elapsed = (stop-start)*1000000 #Converts from seconds to microseconds 
  return elapsed

def measure_average():
  # This function takes 3 measurements and
  # returns the average.

  time1=measure()
  time.sleep(0.1)
  time2=measure()
  time.sleep(0.1)
  time3=measure()
  averagetime = (time1 + time2 + time3) / 3
  return averagetime

# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO    = 24

print("Ultrasonic Measurement")
#print("Speed of sound is",speedSound/100,"m/s at ",temperature,"deg")

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

#Initialize sensor
GPIO.output(GPIO_TRIGGER, True)
time.sleep(.5)
print("Init the sensor.")

# Wrap main content in a try block so we can
# catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent
# the user seeing lots of unnecessary error
# messages.
try:
  while True:
    GPIO.output(GPIO_TRIGGER, False)
    GPIO.output(GPIO_TRIGGER, True)
    
    LowLevelTime = measure_average()
    if (LowLevelTime >= 50000): #Reading is invalid
      Print("Invalid.")
    else:
      distance = LowLevelTime /50 # Every 50 us = 1 cm of distance
      print("Distance : {0:5.1f} cm".format(distance))
    time.sleep(.2)
    
    
    

except KeyboardInterrupt:
  # User pressed CTRL-C
  # Reset GPIO settings
  GPIO.cleanup()
