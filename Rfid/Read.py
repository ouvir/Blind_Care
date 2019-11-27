#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class RFID_READ:
    def __init__(self):
        self.reader = SimpleMFRC522()
    def Read(self):
        try:
            id, text = self.reader.read()
            print(id)
            print(text)
            #Tell a text, and Count the text

        finally:
            GPIO.cleanup()

'''
import read as rd
while true:
    x=rd.RFID_READ()
    x.Read()
'''
x=RFID_READ()
x.Read()
