# Infrared obstacle avoidance module

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

  

class CarInfrared(object):
    def __init__(self):
        self.GPIO_Infrared_right = 8  # GPIO setting (BCM coding)
        self.GPIO_Infrared_left = 5
        self.GPIO_Infrared_front = 11

#        self.GPIO_left_tracking = 16
#        self.GPIO_right_tracking = 12

        GPIO.setup(self.GPIO_Infrared_right, GPIO.IN)
        GPIO.setup(self.GPIO_Infrared_left, GPIO.IN)
        GPIO.setup(self.GPIO_Infrared_front, GPIO.IN)

#        GPIO.setup(self.GPIO_left_tracking, GPIO.IN)
#        GPIO.setup(self.GPIO_right_tracking, GPIO.IN)

    def InfraredMeasure(self):
        left_measure = GPIO.input(self.GPIO_Infrared_left)  # if there is an obstacle, GPIO will become 0; else, GPIO_input = 1;
        right_measure = GPIO.input(self.GPIO_Infrared_right)
        front_measure = GPIO.input(self.GPIO_Infrared_front)

        return [left_measure, right_measure, front_measure]

#    def TrackingMreasure(self):
#        left_tracking = GPIO.input(self.GPIO_left_tracking)
#        right_tracking = GPIO.input(self.GPIO_right_tracking)#1黑0白
#
#        return [left_tracking, right_tracking]


if __name__ == '__main__':
    try:
        car = CarInfrared()
        while True:
            [left, right, front] = car.InfraredMeasure()
#            [l, r] = car.TrackingMreasure()
            print(left, right, front)
#            print(l, r)
            time.sleep(0.5)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
