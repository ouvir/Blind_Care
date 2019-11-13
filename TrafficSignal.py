import RPi.GPIO as GPIO
import time

class SignalLight:
    signal=0
    GPIO.setup(23, GPIO.OUT)#Red
    GPIO.setup(24, GPIO.OUT)#Green
    GPIO.setup(25, GPIO.OUT)#Orange
        
    def LightUP(self,number): #회로의 번호
        GPIO.output(self.number, True)

    def LightDOWN(self,number):
        GPIO.output(self.number, True)
            
    def Operate(self):
        while True:
            if  SignalLight.signal==0:
                G = 'No'
                LightUP(23)
                time.sleep(10)
                LightDOWN(23)
                #Red signal
            if  SignalLight.signal==1:
                G = 'Yes'
                LightUP(23)
                start = time.time()
                time.sleep(10)
                LightDOWN(23)
                SignalColor+=1
                #Green signal
            if  SignalLight.signal==2:
                G = 'No'
                GPIO.output(23, False)    
                GPIO.output(24, False)     
                GPIO.output(25, True)    
                time.sleep(3)
                SignalColor-=1
                #Orange signal
  
    def Gtime():
        if G = 'Yes':
            greentime = time.time-start
            return greentime
            #greentime is the time already used
            #So, remain time is 10-greentime
    
'''How to use?
signal = SignalLight()
signal.Operate()
>>operate
signal.Gtime()
>>time of Green
'''
