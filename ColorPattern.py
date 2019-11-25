import RPi.GPIO as GPIO
import time


JudgeConstant = 3000
LED = 31
signal = 29
S3 = 15
S2 = 13
S1 = 11
S0 = 7
VCC = 1
GND = 6

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

def loop():
    temp = 1
    while(1):

        GPIO.output(S2, GPIO.LOW)
        GPIO.output(S3, GPIO.LOW)
        time.sleep(0.1)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        red = NUM_CYCLES / duration
        print("red value - ", red)
        

        GPIO.output(S2,GPIO.LOW)
        GPIO.output(S3,GPIO.HIGH)
        time.sleep(0.1)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() -start
        blue = NUM_CYCLES / duration
        print("blue value - ", blue)

        GPIO.output(S2, GPIO.HIGH)
        GPIO.output(S3, GPIO.HIGH)

        time.sleep(0.1)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        green = NUM_CYCLES / duration
        print("green value - ", green)
        

        offsetRB = red - blue
        offsetRG = red - green
        offsetBG = blue - green
        offsetBR = -offsetRB
        offsetGR = -offsetRG
        offsetGB = -offsetBG
        if offsetRB > JudgeConstant and offsetRG > JudgeConstant:
            print("this is red")

        else:
            if offsetBR > JudgeConstant and offsetBG > JudgeConstant:
                print("this is blue")
            else:
                if offsetGB > JudgeConstant and offsetGR > JudgeConstant:
                    print("this is Green")
                else:
                    print("Cannot determine")
        
        time.sleep(2)



def endprogram():
     GPIO.cleanup()


if __name__=='__main__':
     setup()

     try:
        loop()
     except KeyboardInterrupt:
        endprogram()


