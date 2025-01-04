import pyfirmata

DELAY = 1
MIN = 0
MAX = 180
MID = 90

board = pyfirmata.Arduino('COM13')

servo = board.get_pin('d:9:s')
 
def move_servo(v):
    servo.write(v)
    board.pass_time(DELAY)

move_servo(MIN)
move_servo(MAX)
move_servo(MID)


board.exit()