# Car's movement control (forward, back, left, right, brake)
# motor control

import RPi.GPIO as GPIO
import time





class CarMove(object):
    def __init__(self):
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO_ENA = 13   
        GPIO_IN1 = 19
        GPIO_IN2 = 16
        GPIO_ENB = 20
        GPIO_IN3 = 21
        GPIO_IN4 = 26

        GPIO.setup(GPIO_ENA, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(GPIO_ENB, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(GPIO_IN1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(GPIO_IN2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(GPIO_IN3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(GPIO_IN4, GPIO.OUT, initial=GPIO.LOW)


        self.ENA = GPIO.PWM(GPIO_ENA, 500)
        self.ENB = GPIO.PWM(GPIO_ENB, 500)                                                                                                                                                                                                                                                                                                                                                       
        self.IN1 = GPIO.PWM(GPIO_IN1, 500)
        self.IN2 = GPIO.PWM(GPIO_IN2, 500)
        self.IN3 = GPIO.PWM(GPIO_IN3, 500)
        self.IN4 = GPIO.PWM(GPIO_IN4, 500)
        
        self.ENA.start(0)
        self.ENB.start(0)
        self.IN1.start(0)
        self.IN2.start(0)
        self.IN3.start(0)
        self.IN4.start(0)

#    def Motor_Forward():
#        print('mOTOR FORWARD')
#
#        GPIO.output(ENA, False)  # GPIO input/output definiation
#        GPIO.output(ENB, False)
#        GPIO.output(IN1, False)
#        GPIO.output(IN2, False)
#        GPIO.output(IN3, False)
#        GPIO.output(IN4, False)

    def forward(self, speed):
        self.ENA.ChangeDutyCycle(speed)
        self.ENB.ChangeDutyCycle(speed)
        self.IN1.ChangeDutyCycle(speed)
        self.IN2.ChangeDutyCycle(0)
        self.IN3.ChangeDutyCycle(speed)
        self.IN4.ChangeDutyCycle(0)
        
    def left(self, speed, speed_H, speed_L):
        self.ENA.ChangeDutyCycle(speed)
        self.ENB.ChangeDutyCycle(speed)
        self.IN1.ChangeDutyCycle(speed_H)
        self.IN2.ChangeDutyCycle(0)
        self.IN3.ChangeDutyCycle(speed_L)
        self.IN4.ChangeDutyCycle(0)
        
    def right(self, speed, speed_H, speed_L):
        self.ENA.ChangeDutyCycle(speed)
        self.ENB.ChangeDutyCycle(speed)
        self.IN1.ChangeDutyCycle(speed_L)
        self.IN2.ChangeDutyCycle(0)
        self.IN3.ChangeDutyCycle(speed_H)
        self.IN4.ChangeDutyCycle(0)
    
        
    def back(self, speed):
        self.ENA.ChangeDutyCycle(speed)
        self.ENB.ChangeDutyCycle(speed)
        self.IN1.ChangeDutyCycle(0)
        self.IN2.ChangeDutyCycle(speed)
        self.IN3.ChangeDutyCycle(0)
        self.IN4.ChangeDutyCycle(speed)
    
    def Motor_Back(self, speed):
        self.ENA.ChangeDutyCycle(speed)
        self.ENB.ChangeDutyCycle(speed)
        self.IN1.ChangeDutyCycle(speed)
        self.IN2.ChangeDutyCycle(0)
        self.IN3.ChangeDutyCycle(speed)
        self.IN4.ChangeDutyCycle(0)
    
    
        
    def MotorStop(self):
        self.ENA.stop()
        self.ENB.stop()
        self.IN1.stop()
        self.IN2.stop()
        self.IN3.stop()
        self.IN4.stop()
        


if __name__ == '__main__':
    try:
        car = CarMove()
        while (True):
#           car.left(100,50) #turn left
            car.right(100,80,0) #turn left
#            car.back(80) #turn left
#            car.brake()
#            car.left(100, 80,40)
           

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        car.MotorStop()
        GPIO.cleanup()

