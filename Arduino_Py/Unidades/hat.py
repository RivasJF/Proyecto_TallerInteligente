import serial

serialArduino = serial.Serial("COM13",9600)


while True:
    opcion = input('Que opción desea: ').upper()
    if opcion=='1':
        serialArduino.write(opcion.encode('ascii'))
    elif opcion=='0':
        serialArduino.write(opcion.encode('ascii'))
    elif opcion=='x':
        print("Saliendo del sistema...\n")
        serialArduino.close()
        break     




