import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

try:
    while True:
        GPIO.output(2,GPIO.HIGH)
        time.sleep(0.4)
        GPIO.output(2,GPIO.LOW)
        time.sleep(0.2)
except:
    print("Fin del programa")
    GPIO.cleanup()
