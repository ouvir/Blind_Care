import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import threading

def UltraSensor(trig, echo, buzzer):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(trig,GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)
    GPIO.setup(buzzer, GPIO.OUT)
    while True:
        GPIO.output(trig, False)
        time.sleep(0.3)
        
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
            print("buzzer")
            time.sleep(0.5)
        else :
            GPIO.output(buzzer, GPIO.LOW)
            time.sleep(0.5)
                
        print("distance : ", distance, "cm")
    GPIO.cleanup(trig)
    GPIO.cleanup(echo)
    GPIO.cleanup(buzzer)

def RFID_READ(SDA,SCK,MOSI,MISO,RST):
    reader = SimpleMFRC522()
    while True:
        id, text = reader.read()
        print(id)
        print(text)
        #Tell a text, and Count the text

def stupid():
    while True:
        print("fuck")

def lslsls():
    while True:
        print("lsls")



if __name__== "__main__":
    #RFID_READ(24,23,19,21,22)
    #UltraSensor(36,38,40)
   # a=threading.Thread(target=stupid,name="lflflflf",args=())
   # b=threading.Thread(target=lslsls,name="lfjkjijg",args=())
    x=threading.Thread(target=RFID_READ,name="RFID",args=(24,23,19,21,22))
    y=threading.Thread(target=UltraSensor,name="UltraSensor",args=(36,38,40))
    #a.start()
    #b.start()
    x.start()
    y.start()

