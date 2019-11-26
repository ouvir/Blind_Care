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

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(S0, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(S1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(S2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(S3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print("setup done...\n")
    t.colormode(255)
    f.close()
    #time for initialize as white
    time.sleep(1)
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

        GPIO.output(S2, GPIO.LOW)
        GPIO.output(S3, GPIO.LOW)
        time.sleep(0.1)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        red =int( NUM_CYCLES / duration)
        red = red - 2000
        if red <= 0:
            red = 0

        print("red value - ", red)
        

        GPIO.output(S2,GPIO.LOW)
        GPIO.output(S3,GPIO.HIGH)
        time.sleep(0.1)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() -start
        blue =int( NUM_CYCLES / duration)
        print("blue value - ", blue)

        GPIO.output(S2, GPIO.HIGH)
        GPIO.output(S3, GPIO.HIGH)

        time.sleep(0.1)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        green =int( NUM_CYCLES / duration)
        print("green value - ", green)

        
        red =(int)( red / 145)
        blue =(int)( blue / 145)
        green =(int)( green / 145)
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
        time.sleep(0.2)
        whilecount = whilecount + 1
        if whilecount is 10:
            whilecount  = 0
            if redcount > bluecount + 3 and redcount > greencount + 3 and redcount> yellowcount + 3 :
                print('red')
            elif bluecount > redcount + 3 and bluecount > greencount + 3 and bluecount > yellowcount + 3:
                print('blue')
            elif yellowcount > redcount + 3 and yellowcount > bluecount + 3 and yellowcount > greencount + 3:
                print('yellow')
            elif greencount > redcount + 3 and greencount > bluecount + 3 and greencount > yellowcount + 3:
                print('green')
            else:
                print('white')
        else:

def endprogram():
     GPIO.cleanup()

if __name__=='__main__':
     setup()

     try:
        loop()
     except KeyboardInterrupt:
        endprogram()


