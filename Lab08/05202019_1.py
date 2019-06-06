import RPi.GPIO as GPIO
import time 
import curses
from curses import wrapper

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
p = GPIO.PWM(40, 50)
p.start(0)
time.sleep(2)

stdscr = curses.initscr()
stdscr.clear()

try:
    while True: 
        print 'PLZ input a or s or d or f or g'
        time.sleep(2)
        ch = stdscr.getkey()
        if ch == "a":
            p.ChangeDutyCycle(7.5)
            print '0 now'
            time.sleep(0.2)
        if ch == "s":
            p.ChangeDutyCycle(10)
            print '+45 now'
            time.sleep(0.2)        
        if ch == "d":
            p.ChangeDutyCycle(12.5)
            print '+90 now'
            time.sleep(0.2)
        if ch == "f":
            p.ChangeDutyCycle(5)
            print '-45 now'
            time.sleep(0.2)
        if ch == "g":
            p.ChangeDutyCycle(2.5)
            print '-90 now'
            time.sleep(0.2)

except KeyboardInterrupt: 
    GPIO.cleanup()