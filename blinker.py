import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
try:
	while True:
		print("LED on")
		GPIO.output(18,GPIO.HIGH)
		time.sleep(1)
		print("LED off")
		GPIO.output(18,GPIO.LOW)
		time.sleep(1)
except KeyboardInterrupt:
	print("Goodbye")
	GPIO.cleanup()


