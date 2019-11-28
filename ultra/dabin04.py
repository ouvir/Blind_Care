import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

trig=23
echo=24
buzzer=25

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

try:
    while True:
        GPIO.output(trig, False)
        time.sleep(0.5)
        
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)
        
        while GPIO.input(echo)==0:
            pulse_start=time.time()
            
        while GPIO.input(echo)==1:
            pulse_end=time.time()
            
        pulse_duration=pulse_end-pulse_start
        distance=pulse_duration*17000
        distance=round(distance,2)
        
        if distance < 30 :
            GPIO.output(buzzer, GPIO.HIGH)
            sleep(0.5)
        else :
            GPIO.output(buzzer, GPIO.LOW)
            sleep(0.5)
            
        print("거리 : ", distance, "cm")
        
except Keyboardinterrupt:
    GPIO.cleanup()