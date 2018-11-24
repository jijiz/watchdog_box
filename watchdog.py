import RPi.GPIO as GPIO
import time
import socket
import datetime

pin_relais = 3

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except Exception as e:
        pass
    return False

def main():
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin_relais, GPIO.OUT)
        GPIO.output(pin_relais, GPIO.LOW)
        while(1):
            print(str(datetime.datetime.now())+" Check connexion")
            if is_connected() == False:
                GPIO.output(pin_relais, GPIO.HIGH)
                time.sleep(1)
                print(str(datetime.datetime.now())+"Redemarrage")
                GPIO.output(pin_relais, GPIO.LOW)
                time.sleep(160)
            else:
                print(str(datetime.datetime.now())+" Connexion OK")
            time.sleep(20)
    finally:
        GPIO.cleanup()
if __name__ == '__main__':
    main()
