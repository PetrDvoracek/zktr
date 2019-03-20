import Adafruit_BBIO.GPIO as GPIO
import time


GPIO.setup("P8_9",GPIO.OUT)
GPIO.output("P8_9",GPIO.OUT)
while(True):
    GPIO.setup("P8_10",GPIO.OUT)
    GPIO.output("P8_10",GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output("P8_10",GPIO.LOW)
    time.sleep(0.1)
    

