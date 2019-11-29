import RPi.GPIO as GPIO
import time
import Transponder as Tp




signal = 0

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)#Red
    GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)#Orange
    GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)#Green
def loop():   
    global signal
    while True:
        if  signal==0:
            GPIO.output(23, GPIO.HIGH)
            time.sleep(10)
            #Red signal
            signal+=1
            
            
        elif signal==1:
            GPIO.output(24, GPIO.HIGH)
            time.sleep(5)
            #Orange signal
            signal+=1
            
        elif  signal==2:
            
            GPIO.output(26, GPIO.HIGH)
            k=10
            for i in range(10):
                time.sleep(1)
                k-=1
                string = str(k)
                number = Tp.RFID()
                number.Write(string)
                
            #Green signal
            signal-=2
        GPIO.cleanup()
        setup()   
        

def endprogram():
     GPIO.cleanup()


if __name__=='__main__':
     setup()

     try:
        loop()
     except KeyboardInterrupt:
        endprogram()


GPIO.cleanup()
