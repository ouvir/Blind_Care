import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class RFID:

    def Write(self,T):
        reader = SimpleMFRC522()
        text = T
        reader.write(text)
        print("Written")

    def Read(self):
        reader = SimpleMFRC522()
        id, text = reader.read()
        print(id)
        print(text)


