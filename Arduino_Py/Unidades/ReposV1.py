"""
import pyfirmata
import serial

serialArduino = serial.Serial("COM14",9600)

comport = 'COM13'
board = pyfirmata.Arduino(comport)

# Pines configurados
led_1 = board.get_pin('d:8:o')
led_2 = board.get_pin('d:9:o')
led_3 = board.get_pin('d:10:o')
led_4 = board.get_pin('d:11:o')
led_5 = board.get_pin('d:12:o')
servo = board.get_pin('d:6:s')
PIEZO_PIN = board.get_pin('d:3:p')

# Bandera para bloquear interacciones
block_interaction = False

def move_servo(v):
    servo.write(v)
    board.pass_time(0.1)

def turn_on_all_leds():
    """Enciende todos los LEDs."""
    led_1.write(1)
    led_2.write(1)
    led_3.write(1)
    led_4.write(1)
    led_5.write(1)

def turn_off_all_leds():
    """Apaga todos los LEDs."""
    led_1.write(0)
    led_2.write(0)
    led_3.write(0)
    led_4.write(0)
    led_5.write(0)

def led(fingerUp):
    global block_interaction

    if block_interaction:
        # Si las interacciones están bloqueadas, solo permite continuar si todos los dedos están abajo
        if fingerUp == [0, 0, 0, 0, 0]:
            block_interaction = False
            turn_off_all_leds()
            PIEZO_PIN.write(0)
            move_servo(0)
        return

    # Detecta si hay 3 dedos levantados
    if fingerUp == [1, 0, 0, 0, 1]:
        block_interaction = True
        turn_on_all_leds()
        PIEZO_PIN.write(0.8)
        move_servo(90)
        return

    # Configura el servo y el piezo según el patrón
    if fingerUp == [0, 0, 0, 0, 0]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [0, 1, 0, 0, 0]:
        led_1.write(0)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
        PIEZO_PIN.write(0)
    elif fingerUp == [0, 1, 1, 0, 0]:
        led_1.write(0)
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [0, 1, 1, 1, 0]:
        led_1.write(0)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
        serialArduino.write(cad.encode('ascii')) 
    elif fingerUp == [0, 1, 1, 1, 1]:
        led_1.write(0)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
        PIEZO_PIN.write(0)
        move_servo(0)
    elif fingerUp == [1, 1, 1, 1, 1]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
        move_servo(90)

# Ejemplo de uso
# fingerUp = [0, 1, 1, 1, 0]
# led(fingerUp)
"""
