import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class RFID:

    def __init__(self):
        GPIO.cleanup()

    def Write(self,T):
        reader = SimpleMFRC522()

        try:
            text = T
            reader.write(text)
            print("Written")
        finally:
            GPIO.cleanup()

    def Read(self):
        reader = SimpleMFRC522()

        try:
            id, text = reader.read()
            print(id)
            print(text)
        finally:
            GPIO.cleanup()


