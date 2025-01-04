import pyfirmata
import pyfirmata.util

# Configuración de la puerto COM
comport = 'COM14'

# Inicialización de la placa
board = pyfirmata.Arduino(comport)
pyfirmata.util.Iterator(board).start()

# Configuracion de Pines
sensor = board.get_pin('d:7:i')
sensor.enable_reporting()
led_0 = board.get_pin('d:4:o')
led_1 = board.get_pin('d:8:o')
led_2 = board.get_pin('d:9:o')
led_3 = board.get_pin('d:10:o')
led_4 = board.get_pin('d:11:o')
led_5 = board.get_pin('d:12:o')
led_6 = board.get_pin('d:5:o')
servo = board.get_pin('d:6:s')


# Bandera para bloquear interacciones
block_interaction = False
alarma=0

# Función para mover el servo
def move_servo(v):
    servo.write(v)
    board.pass_time(0.1)

#iniciar el servo en 90 grados
move_servo(90)

def turn_on_all_leds():
    #Enciende todos los LEDs
    led_0.write(1)
    led_1.write(0)
    led_2.write(1)
    led_3.write(1)
    led_4.write(1)
    led_5.write(1)

def turn_off_all_leds():
    #Apaga todos los LEDs
    led_0.write(0)
    led_1.write(0)
    led_2.write(0)
    led_3.write(0)
    led_4.write(0)
    led_5.write(0)

# Función para controlar los LEDs y el servo
def led(fingerUp):
    global block_interaction
    global alarma

    if block_interaction:
        # Si las interacciones están bloqueadas, apaga todos los LEDs y mueve el servo a 90 grados
        if fingerUp == [1, 0, 0, 0, 1]:
            block_interaction = False
            turn_off_all_leds()
            move_servo(90)#
            alarma=0
            led_6.write(0)
        return

    # Detecta si hay vibraacion
    while True:
        if alarma==3:
            print("Sismo detectado")
            block_interaction = True
            turn_on_all_leds()
            move_servo(0)#
            led_6.write(1)
            return
        elif sensor.read():
            print("Vibracion Detectada No: ",alarma)
            alarma=alarma+1
            break
        else:
            break
    

    # Configura el servo y el piezo según el patrón
    if fingerUp == [0, 0, 0, 0, 0]:
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [0, 1, 0, 0, 0]:
        led_2.write(1)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [0, 1, 1, 0, 0]:
        led_2.write(1)
        led_3.write(0)
        led_4.write(1)
        led_5.write(0)
    elif fingerUp == [0, 1, 1, 1, 0]:
        led_2.write(1)
        led_3.write(1)
        led_4.write(1)
        led_5.write(1)
    elif fingerUp == [0, 1, 1, 1, 1]:
        led_1.write(1)
        move_servo(0)
    elif fingerUp == [1, 1, 1, 1, 1]:
        led_1.write(0)
        move_servo(90)

