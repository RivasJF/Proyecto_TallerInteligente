import pyfirmata

comport='COM14'

board=pyfirmata.Arduino(comport)

servo = board.get_pin('d:6:s')

def move_servo(v):
    servo.write(v)
    board.pass_time(1)

def led(fingerUp):
    if  fingerUp==[0,1,1,1,1]:
        move_servo(0)
    elif fingerUp==[1,1,1,1,1]:
        move_servo(90)