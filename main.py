import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import threading



def ColorSensor(LED,S2,S3,signal):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(S2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(S3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    NUM_CYCLES = 10

    while(1):

        
        #red filter set
        GPIO.output(S2, GPIO.LOW)
        GPIO.output(S3, GPIO.LOW)
        time.sleep(0.1) #delay 0.1sec
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        red =int(NUM_CYCLES / duration)
        red = red - 1000 #offset due to abnormally high red light
        if red <= 0:
            red = 0



        #blue filter set
        GPIO.output(S2,GPIO.LOW)
        GPIO.output(S3,GPIO.HIGH)
        time.sleep(0.1)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() -start
        blue =int(NUM_CYCLES / duration)
        if blue <= 0:
            blue = 0

        #green filter set
        GPIO.output(S2, GPIO.HIGH)
        GPIO.output(S3, GPIO.HIGH)

        time.sleep(0.1)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        green =int(NUM_CYCLES / duration)
        if green <= 0:
            green = 0

        red=int(red/70)
        blue=int(blue/70)
        green=int(green/70)
        if red > 255:
            red = 255
        if blue > 255:
            blue = 255
        if green > 255:
            green = 255
        print("red:", red, "blue:",blue, "green:",green)

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
        time.sleep(0.5)
        id, text = reader.read()
        print(id)
        print(text)
        #Tell a text, and Count the text


if __name__== "__main__":
    x=threading.Thread(target=RFID_READ,name="RFID",args=(24,23,19,21,22))
    y=threading.Thread(target=UltraSensor,name="UltraSensor",args=(36,38,40))
    z=threading.Thread(target=ColorSensor,name="ColorSensor",args=(31,7,11,29))
    x.start()
    y.start()
    z.start()
