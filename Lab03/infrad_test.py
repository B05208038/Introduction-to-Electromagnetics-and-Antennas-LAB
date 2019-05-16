import RPi.GPIO as IO
import time 
IO.setwarnings(False)
IO.setmode(IO.BOARD)

IO.setup(12, IO.OUT)
IO.setup(16, IO.OUT)
IO.setup(37, IO.IN)

while 1: 
    if (IO.input(37)==True):
        IO.output(13, True)
        IO.output(15, False)
    if (IO.input(37)==False):
        IO.output(13, False)
        IO.output(15, True)
IO.cleanup()