import RPi.GPIO as GPIO
import time
import Transponder as Tp

def LightUP(number): #회로의 번호
    GPIO.output(self.number, True)

def LightDOWN(number):
    GPIO.output(self.number, False)
            

        
start=0
signal=0
GPIO.setup(23, GPIO.OUT)#Red
GPIO.setup(24, GPIO.OUT)#Orange
GPIO.setup(25, GPIO.OUT)#Green
   
while True:
        if  signal==0:
            LightUP(23)
            time.sleep(10)
            #Red signal
            signal+=1
            
        elif  signal==1:
            LightUP(24)
            time.sleep(5)
            #Orange signal
            Signal+=1
            
        elif  signal==2:
            LightUP(25)
            k=10
            for i in range(10):
                time.sleep(1)
                k-=1
                number = Tp.RFID()
                number.Write(k)
            #Green signal
            Signal-=2
        else:
            
        LightDOWN(23)
        LightDOWN(24)
        LightDOWN(25)
    
