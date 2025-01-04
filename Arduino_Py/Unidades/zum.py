import pyfirmata
import math

board = pyfirmata.Arduino("/dev/ttyACM0")

# connect piezo to pin 9 to use PWM
SENSOR_PIN = 0
PIEZO_PIN = board.get_pin('d:9:p')

it = pyfirmata.util.Iterator(board)
it.start()

board.analog[SENSOR_PIN].enable_reporting()

# check buzzer is working
PIEZO_PIN.write(0.2)
board.pass_time(0.5)
PIEZO_PIN.write(0.6)
board.pass_time(0.5)
PIEZO_PIN.write(0.8)
board.pass_time(0.5)
PIEZO_PIN.write(0)

while True:
        PIEZO_PIN.write(0.2)
        board.pass_time(0.5)
        PIEZO_PIN.write(0.6)
        board.pass_time(0.5)
        PIEZO_PIN.write(0.8)
        board.pass_time(0.5)
        PIEZO_PIN.write(0) 