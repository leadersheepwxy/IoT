
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

  

class CarServo(object):
    def __init__(self):
        GPIO_Servo = 6  # GPIO setting (BCM coding)
        GPIO.setup(GPIO_Servo, GPIO.OUT)
        self.Servo = GPIO.PWM(GPIO_Servo, 50)
        self.Servo.start(0)



    def SetAngle(self):
        dutyCycle1 = int(1 / 20 * 0 + 3)
        self.Servo.ChangeDutyCycle(dutyCycle1)
        time.sleep(0.2)
        dutyCycle2 = int(1 / 20 * 100 + 3)
        self.Servo.ChangeDutyCycle(dutyCycle2)
        time.sleep(0.2)


#    def TrackingMreasure(self):
#        left_tracking = GPIO.input(self.GPIO_left_tracking)
#        right_tracking = GPIO.input(self.GPIO_right_tracking)#1黑0白
#
#        return [left_tracking, right_tracking]


if __name__ == '__main__':
    try:
        car = CarServo()
        while True:
            car.SetAngle()

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

