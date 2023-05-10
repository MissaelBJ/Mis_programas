import RPi.GPIO as GPIO

GPIO.setup(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

pwm = GPIO.PWM(2, 50)
pwm.start(2.5)

continuar = True
while continuar:
    dato = input("Digite el dc para el servo: ")
    if dato == "z":
        continuar = False
    else:
        pwm.ChangeDutyCicle(float(dato))
pwm.stop()
GPIO.cleanup()
print("FIn del programa")

