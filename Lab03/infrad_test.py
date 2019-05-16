import RPi.GPIO as IO
import time 
IO.setwarnings(False)
IO.setmode(IO.BOARD)

IO.setup(18, IO.OUT)
IO.setup(22, IO.OUT)
IO.setup(37, IO.IN)

while 1: 
    if (IO.input(37)==True):
        IO.output(18, True)
        IO.output(22, False)
    if (IO.input(37)==False):
        IO.output(18, False)
        IO.output(22, True)
IO.cleanup()