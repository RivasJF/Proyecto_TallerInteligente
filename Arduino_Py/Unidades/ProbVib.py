
from pyfirmata import Arduino,util
from time import sleep


comport = 'COM13'
board =Arduino(comport)

it = util.Iterator(board)
it.start()

sensor = board.get_pin('d:2:i')
led_6 = board.get_pin('d:13:o')

while True:
    alarma=sensor.read()
    print(alarma)
    sleep(0.5)


# Ejemplo de uso
# fingerUp = [0, 1, 1, 1, 0]
# led(fingerUp)

