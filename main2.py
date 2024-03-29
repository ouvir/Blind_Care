import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import threading
import turtle as t
DISTANCE=0
GPIO.setwarnings(False)

def ColorSensor(LED,S2,S3,signal,buz):
    global DISTANCE
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(S2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(S3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(buz,GPIO.OUT)
    p = GPIO.PWM(buz,5)
    NUM_CYCLES = 10
    redcount=0
    greencount=1
    bluecount=0
    whitecount=0
    blackcount=0
    JudgeConstant = 30
    p.ChangeDutyCycle(70)
    while(1):
        GPIO.output(buz,GPIO.LOW)
        #red filter set
        GPIO.output(S2, GPIO.LOW)
        GPIO.output(S3, GPIO.LOW)

        time.sleep(0.1) #delay 0.1sec
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        red =int(NUM_CYCLES / duration)
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

        #calibration
        white_level= 18000
        black_level= 5000
        raw_rgb = [red, green, blue]
        rgb = [0,0,0]
        x = (white_level - black_level) / 255
        x=int(x)

        for i in range(3):
            rgb[i] =(int)((raw_rgb[i]-black_level)/x)
        for i in range(3):
            if rgb[i] > 255:
                rgb[i] = 255
            elif rgb[i] < 0:
                rgb[i] = 0
        '''
        print("red:", rgb[0], "green:",rgb[1], "blue:",rgb[2])
        print("rawRGB:", raw_rgb)
        '''
        offsetRB = rgb[0] - rgb[2]
        offsetRG = rgb[0] - rgb[1]
        offsetBG = rgb[2] - rgb[1]

        offsetBR = -offsetRB
        offsetGR = -offsetRG
        offsetGB = -offsetBG
        average=int((rgb[0]+rgb[1]+rgb[2])/3)
        if average < 30:
            p.start(25)
            blackcount = blackcount + 1
            print("black!")
            time.sleep(1)
        elif average > 230:
            whitecount = whitecount + 1
        elif rgb[0] > rgb[1] and rgb[0] > rgb[2]:
            redcount += 1
            if offsetRG > JudgeConstant and offsetRB > JudgeConstant:
                print("this is red")
        elif rgb[1] > rgb[0] and rgb[1] > rgb[2]:
            greencount+=1
            if offsetGB > JudgeConstant and offsetGR > JudgeConstant:
                print("this is green")
        elif rgb[2] > rgb[0] and rgb[2] > rgb[1]:
            bluecount+=1
            if offsetBR > JudgeConstant and offsetBG > JudgeConstant:
                print("this is blue")
        else:
            print("Undefined")
        p.stop()
        GPIO.output(buz,GPIO.LOW)

        if greencount > bluecount +5 and greencount > redcount +5:
            print("green dominant")
            redcount = 0
            bluecount = 0
            greencount = 0
            balckcount = 0
            whitecount = 0
            DISTANCE = 1

        elif bluecount > greencount + 5 and bluecount > redcount + 5:
            print("blue dominant")
            redcount = 0
            bluecount = 0
            greencount = 0
            blackcount = 0
            whitecount = 0
            DISTANCE = 2

        elif redcount > bluecount + 5 and redcount > greencount + 5:
            print("red dominant")
            redcount = 0
            bluecount = 0
            greencount = 0
            blackcount = 0
            whitecount = 0
            DISTANCE= 3






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

def RFID_READ(SDA,SCK,MOSI,MISO,RST,BUZ):
    GPIO.setmode(GPIO.BOARD)
    reader = SimpleMFRC522()
    GPIO.setup(BUZ,GPIO.OUT)
    p = GPIO.PWM(BUZ,5)
    while True:
        time.sleep(0.5)
        id, text = reader.read()
        print(text)
        T=int(text)
        remainT=T
        p.ChangeDutyCycle(70)
        i=0
        while remainT > 0:
            time.sleep(1)
            print(remainT)
            if remainT < 5 :
                p.start(25)
            remainT-=1
            i+=1
        p.stop()
        GPIO.output(BUZ,GPIO.LOW)

        #Tell a text, and Count the text


if __name__== "__main__":
    x=threading.Thread(target=RFID_READ,name="RFID",args=(24,23,19,21,22,16))
    y=threading.Thread(target=UltraSensor,name="UltraSensor",args=(36,38,40))
    z=threading.Thread(target=ColorSensor,name="ColorSensor",args=(31,13,15,29,12))
    x.start()
    y.start()
    z.start()
