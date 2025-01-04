import serial

serialArduino = serial.Serial("COM14",9600)

opcion=0

# Bandera para bloquear interacciones
def led(fingerUp):
    # Confgura el servo y el piezo según el patrón
    if fingerUp == [0, 0, 0, 0, 0]:
        opcion=0
        serialArduino.write(opcion.encode('ascii'))
    elif fingerUp == [0, 1, 0, 0, 0]:
        opcion=1
        serialArduino.write(opcion.encode('ascii'))
    elif fingerUp == [0, 1, 1, 0, 0]:
        opcion=2
        serialArduino.write(opcion.encode('ascii'))
    elif fingerUp == [0, 1, 1, 1, 0]:
        opcion=3
        serialArduino.write(opcion.encode('ascii'))
    elif fingerUp == [0, 1, 1, 1, 1]:
        opcion=4
        serialArduino.write(opcion.encode('ascii'))
    elif fingerUp == [1, 1, 1, 1, 1]:
        opcion=5
        serialArduino.write(opcion.encode('ascii'))

