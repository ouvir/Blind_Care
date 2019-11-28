from __future__ import print_function
from blessings import Terminal
term = Terminal()

import time
import threading
import RPi.GPIO as GPIO


def _setup_buttons():

class ColorSensor(threading.Thread):
    
    def __init__(self, LED, OUT, S3, S2, S1, S0):
        try:
            threading.Thread.__init__(self)
            self._LED = LED
            self._OUT = OUT
            self._S3 = S3
            self._S2 = S2
            self._S1 = S1
            self._S0 = S0


            GPIO.setmode(GPIO.BOARD)
            
            #LED should be set for this project
            GPIO.setup(LED, GPIO.OUT, initial=GPIO.HIGH)
            

            GPIO.setup(S0, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(S1, GPIO.OUT, initial=GPIO.LOW)
            """

            s0 and s1 set the frequency scaling

            f   s0  s1  Frequency scaling
            0   L   L   Off
            1   L   H   2%
            2   H   L   20%
            3   H   H   100%

            initial set :  20%

            """
            GPIO.setup(S2, GPIO.OUT, initial=GPIO.LOW)
            GPIO.setup(S3, GPIO.OUT, initial=GPIO.LOW)

            self.setup(OUT, GPIO.IN, pull_up_down = GPIO.PUD_UP)
            self.set_sample_size(20)
            self.set_update_interval(1.0)

           
            
        except Exception as e:
            print(e)
            print("Color sensor initializing failed...!")







        




    def cancel(self):


    def get_rbg(self, top=255):


    def get_hertz(self):

    def set_black_level(self, rgb):

    def get_black_level(self):

    def set_white_level(self, rgb):

    def get_white_level(self):

    def set_frequency(self, f):

    def get_frequency(self):

    def get_update_interval(self):

    def set_sample_size(self, samples):

    def get_sample_size(self):

    def pause(self):

    def resume(self):

    def _set_filter(self,f):


    def _cbf(self, g, l, t):

    def run(self):

    def _calibrate(self):

    def _reading(self):

    def _led_on(self):

    def _led_off(self):
