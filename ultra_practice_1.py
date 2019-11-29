import RPi.GPIO as GPIO
import time
import sys
import signal

TRIG = 23
ECHO = 24

MAX_DISTANCE_CM = 300
MAX_DURATION_TIMEOUT = (MAX_DISTANCE_CM * 2 * 29.1)

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    GPIO.cleanup()
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def distanceInCm(duration):
    return (duration/2)/29.1

def print_distance(distance):
    if distance == 0:
        distanceMsg = 'Distance : out of range    \r'
    else:
        distanceMsg = 'Distance : ' + str(distance) + 'cm' + '   \r'
    sys.stdout.write(distanceMsg)
    sys.stdout.flush()
    
def main():
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    print('To Exit, Press the CTRL+C Keys')
    
    GPIO.output(TRIG, False)
    print('Waiting For Sensor To Ready')
    time.sleep(1)
    
    print('Start!')
    while True:
        fail = False
        time.sleep(0.1)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        timeout = time.time()
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
            if ((pulse_start - timeout)*1000000) >= MAX_DURATION_TIMEOUT:
                fail = True
                break
            
        if fail:
            continue
            
        timeout = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
            if ((pulse_end - pulse_start)*1000000) >= MAX_DURATION_TIMEOUT:
                print_distance(0)
                fail = True
                break
            
        if fail:
            continue
            
        pulse_duration = (pulse_end - pulse_start) * 1000000
            
        distance = distanceInCm(pulse_duration)
        distance = round(distance, 2)            
            
        print_distance(distance)
            
    GPIO.cleanup()
        
if __name__ == '__main__':
    main()