import RPi.GPIO as GPIO
import time
from time import sleep
import threading
GPIO.setwarnings(False)

class UltraSensor(threading.Thread):
    def __init__(self, trig, echo, buzzer):
        self._trig=trig
        threading.Thread.__init__(self)

        self._echo=echo
        self._buzzer=buzzer
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(trig,GPIO.OUT)
        GPIO.setup(echo, GPIO.IN)
        GPIO.setup(buzzer, GPIO.OUT)
        self.setDaemon(True)
        self.start()

    def ultra(self):
        GPIO.output(self._trig, False)
        time.sleep(0.3)
        
        GPIO.output(self._trig, True)
        time.sleep(0.00001)
        GPIO.output(self._trig, False)
        
        while GPIO.input(self._echo)==0:
            pulse_start=time.time()
                
        while GPIO.input(self._echo)==1:
            pulse_end=time.time()
            
        pulse_duration=pulse_end-pulse_start
        distance=pulse_duration*17000
        distance=round(distance,2)
        self._distance = distance

        if distance < 30 :
            GPIO.output(self._buzzer, GPIO.HIGH)
            print("buzzer")
            sleep(0.5)
        else :
            GPIO.output(self._buzzer, GPIO.LOW)
            sleep(0.5)
                
        print("distance : ", distance, "cm")
    def __del__(self):
        GPIO.cleanup(self._trig)
        GPIO.cleanup(self._echo)
        GPIO.cleanup(self._buzzer)

