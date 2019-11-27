import RPi.GPIO as GPIO
import time
import turtle as t
import csv

JudgeConstant = 16
LED = 31
signal = 29
S3 = 15
S2 = 13
S1 = 11
S0 = 7
VCC = 1
GND = 6

nocount = 0
redcount = 0
bluecount = 0 
greencount = 0
blackcount = 0
yellowcount = 0

NUM_CYCLES = 10
class ColorSensor:
    def __init__(self, 

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(S0, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(S1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print("setup done...\n")
    t.colormode(255)

    #time for initialize as white
    time.sleep(1)

def judge(red, green, blue, JudgeConstant):
    offsetRB = red - blue
    offsetRG = red - green
    offsetBG = blue - green
    offsetBR = -offsetRB
    offsetGR = -offsetRG
    offsetGB = -offsetBG
    
    if offsetRB > JudgeConstant and offsetRG > JudgeConstant:
        return 1
    elif offsetBR > JudgeConstant and offsetBG > JudgeConstant:
        return 2
    elif offsetGB > JudgeConstant and offsetGR > JudgeConstant:
        return 3
    elif offsetRB > JudgeConstant and offsetGB > JudgeConstant and abs(offsetRG)< 5:
        return 4
    elif red<30 and blue<30 and green<30
        return 5
    elif red>200 and blue>200 and green>200
        return 6
    else:
        return 7

def loop():

    temp = 1
    nocount = 0
    redcount = 0
    bluecount = 0 
    greencount = 0
    blackcount = 0
    yellowcount = 0

    while(1):

        whilecount = 0
        
        #red filter set
        GPIO.output(S2, GPIO.LOW)
        GPIO.output(S3, GPIO.LOW)
        time.sleep(0.1) #delay 0.1sec
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        red =int(NUM_CYCLES / duration)
        red = red - 2000 #offset due to abnormally high red light
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

        red=int(red/145)
        blue=int(blue/145)
        green=int(green/145)
        if red > 255:
            red = 255
        if blue > 255:
            blue = 255
        if green > 255:
            green = 255

        t.pen(pensize = "20")
        t.pencolor(red,green,blue)
        t.goto(0,0)
        t.forward(40)

        offsetRB = red - blue
        offsetRG = red - green

        offsetBG = blue - green
        offsetBR = -offsetRB

        offsetGR = -offsetRG
        offsetGB = -offsetBG

        if offsetRB > JudgeConstant and offsetRG > JudgeConstant:
            print("this is red")
            redcount = redcount + 1
        else:
            if offsetBR > JudgeConstant and offsetBG > JudgeConstant:
                print("this is blue")
                bluecount = bluecount + 1
            else:
                if offsetGB > JudgeConstant and offsetGR > JudgeConstant:
                    print("this is Green")
                    greencount = greencount + 1
                else:
                    if  offsetRB > JudgeConstant and offsetGB > JudgeConstant and abs(offsetRG)< 5:
                        print('this is yellow')
                        yellowcount = yellowcount + 1
                    else:
                        print("No valid color detected(White)")
                        nocount = nocount + 1

        if red < 30 and green < 30 and blue < 30:
            blackcount = blackcount + 1

        time.sleep(0.2)
        whilecount = whilecount + 1
        if whilecount is 10:
            whilecount  = 0
            if redcount > bluecount + 3 and redcount > greencount + 3 and redcount> yellowcount + 3 :
                print('red:', redcount)
            elif bluecount > redcount + 3 and bluecount > greencount + 3 and bluecount > yellowcount + 3:
                print('blue:', bluecount)
            elif yellowcount > redcount + 3 and yellowcount > bluecount + 3 and yellowcount > greencount + 3:
                print('yellow', yellowcount)
            elif greencount > redcount + 3 and greencount > bluecount + 3 and greencount > yellowcount + 3:
                print('green', greencount)
            else:
                print('white', nocount)

def endprogram():
     GPIO.cleanup()

if __name__=='__main__':
     setup()

     try:
        loop()
     except KeyboardInterrupt:
        endprogram()


