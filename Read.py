#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import threading
class RFID_READ(threading.Thread):
    def __init__(self,SDA,SCK,MOSI,MISO,RST):
        threading.Thread.__init__(self)
        self.reader = SimpleMFRC522()
        self._SDA = SDA
        self._SCK = SCK
        self._MOSI = MOSI
        self._MISO = MISO
        self._RST = RST
        self.setDaemon(True)
        self.start()
    def Read(self):
        id, text = self.reader.read()
        print(id)
        print(text)
        #Tell a text, and Count the text
''' 
import read as rd
while true:
    x=rd.RFID_READ()
    x.Read()
'''
