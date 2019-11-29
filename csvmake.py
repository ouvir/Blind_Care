import RPi.GPIO as GPIO
import time
import turtle as t



def ColorSensor(LED,S0,S1,signal):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(S0, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(S1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    t.colormode(255)
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


