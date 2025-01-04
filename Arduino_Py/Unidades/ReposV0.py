"""
import pyfirmata
comport='COM13'

board=pyfirmata.Arduino(comport)

led_1=board.get_pin('d:8:o')
led_2=board.get_pin('d:9:o')
led_3=board.get_pin('d:10:o')
led_4=board.get_pin('d:11:o')
led_5=board.get_pin('d:12:o')
servo = board.get_pin('d:6:s')
PIEZO_PIN = board.get_pin('d:3:p')

def move_servo(v):
    servo.write(v)
    board.pass_time(0.1)


def led(fingerUp):
    if fingerUp==[0,0,0,0,0]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
        PIEZO_PIN.write(0)
        move_servo(0)
    elif fingerUp==[0,1,0,0,0]:
            led_1.write(1)
            led_2.write(0)
            led_3.write(0)
            led_4.write(0)
            led_5.write(0)
    elif fingerUp==[0,1,1,0,0]:
            led_1.write(1)
            led_2.write(1)
            led_3.write(0)
            led_4.write(0)
            led_5.write(0)
            PIEZO_PIN.write(0)  
    elif fingerUp==[0,1,1,1,0]:
            led_1.write(1)
            led_2.write(1)
            led_3.write(1)
            led_4.write(0)
            led_5.write(0)
            PIEZO_PIN.write(0.8)
    elif fingerUp==[0,1,1,1,1]:
            led_1.write(1)
            led_2.write(1)
            led_3.write(1)
            led_4.write(1)
            led_5.write(0)
            move_servo(0)
    elif fingerUp==[1,1,1,1,1]:
            led_1.write(1)
            led_2.write(1)
            led_3.write(1)
            led_4.write(1)
            led_5.write(1)
            move_servo(90)
"""