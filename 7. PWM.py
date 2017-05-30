import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
my_pwm=GPIO.PWM(11,100)

my_pwm.start(50)
my_pwm.ChangeDutyCycle(1)
my_pwm.ChangeDutyCycle(100)
my_pwm.ChangeFrequency(1000)
my_pwm.stop()

GPIO.cleanup()

