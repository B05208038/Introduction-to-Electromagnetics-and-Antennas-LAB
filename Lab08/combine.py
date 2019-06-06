import RPi.GPIO as GPIO
import time 
import curses
from curses import wrapper

trigger_pin = 20
echo_pin = 21
real_distance = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
p = GPIO.PWM(16, 50)
p.start(0)
time.sleep(2)

#define distance
def send_trigger_pulse():
    GPIO.output(trigger_pin, True)
    time.sleep(0.001)
    GPIO.output(trigger_pin, False)

def wait_for_echo(value, timeout):
    count = timeout
    while GPIO.input(echo_pin) != value and count > 0:
        count = count - 1

def get_distance():
    send_trigger_pulse()
    wait_for_echo(True, 5000)
    start = time.time()
    wait_for_echo(False, 5000)
    finish = time.time()
    pulse_len = finish - start
    #real_distance = distance_cm
    distance_cm = pulse_len * 340 * 100 /2
    distance_in = distance_cm / 2.5
    return (distance_cm, distance_in)

#write number
try:
    print("cm = %f\tinches = %f" % get_distance())
    while True: 
        #print 'PLZ input a or s or d or f or g'
        distance = get_distance()[0]
        print("cm = %f\tinches = %f" % get_distance()) 
        if distance <= 10:
            p.ChangeDutyCycle(2.5)
            print '0 now\t'
            time.sleep(0.2)
        if distance <= 30 and distance >10:
            p.ChangeDutyCycle(5)
            print '+45 now\t'
            time.sleep(0.2)        
        if distance <= 60 and distance >30:
            p.ChangeDutyCycle(7.5)
            print '+90 now\t'
            time.sleep(0.2)
        if distance <= 100 and distance >60:
            p.ChangeDutyCycle(10)
            print '-45 now\t'
            time.sleep(0.2)
        if distance <= 200 and distance >100:
            p.ChangeDutyCycle(12.5)
            print '-90 now\t'
            time.sleep(0.2)

except KeyboardInterrupt: 
    GPIO.cleanup()