import cv2
#import controller as cnt
from cvzone.HandTrackingModule import HandDetector
import pyfirmata


comport = 'COM13'
board = pyfirmata.Arduino(comport)

# Pines configurados
led_1 = board.get_pin('d:8:o')
led_2 = board.get_pin('d:9:o')
led_3 = board.get_pin('d:10:o')
led_4 = board.get_pin('d:11:o')
led_5 = board.get_pin('d:12:o')
led_6 = board.get_pin('d:7:o')
servo = board.get_pin('d:6:s')
PIEZO_PIN = board.get_pin('d:3:p')

detector=HandDetector(detectionCon=0.8,maxHands=1)

video=cv2.VideoCapture(0)

block_interaction = False

def move_servo(v):
    servo.write(v)
    board.pass_time(0.1)


while True:
    ret,frame=video.read()
    frame=cv2.flip(frame,1)
    hands,img=detector.findHands(frame)
    if hands:
        lmList=hands[0]
        fingerUp=detector.fingersUp(lmList)

        print(fingerUp)
        #cnt.led(fingerUp)
        if fingerUp==[0,0,0,0,0]:
            cv2.putText(frame,'Finger count:0',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            led_1.write(0)
            led_2.write(0)
            led_3.write(0)
            led_4.write(0)
            led_5.write(0)
        elif fingerUp==[0,1,0,0,0]:
            cv2.putText(frame,'Finger count:1',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)    
            led_1.write(0)
            led_2.write(1)
            led_3.write(0)
            led_4.write(0)
            led_5.write(0)
        elif fingerUp==[0,1,1,0,0]:
            cv2.putText(frame,'Finger count:2',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            led_1.write(0)
            led_2.write(1)
            led_3.write(1)
            led_4.write(0)
            led_5.write(0)
        elif fingerUp==[0,1,1,1,0]:
            cv2.putText(frame,'Finger count:3',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            led_1.write(0)
            led_2.write(1)
            led_3.write(1)
            led_4.write(1)
            led_5.write(0)
            PIEZO_PIN.write(0.8)
        elif fingerUp==[0,1,1,1,1]:
            cv2.putText(frame,'Finger count:4',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            led_1.write(0)
            led_2.write(1)
            led_3.write(1)
            led_4.write(1)
            led_5.write(1)
            PIEZO_PIN.write(0)
            move_servo(0)
        elif fingerUp==[1,1,1,1,1]:
            cv2.putText(frame,'Finger count:5',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            led_1.write(1)
            led_2.write(1)
            led_3.write(1)
            led_4.write(1)
            led_5.write(1)
            move_servo(90)
    cv2.imshow("frame",frame)
    k=cv2.waitKey(1)
    if k==ord("k"):
        break

video.release()
cv2.destroyAllWindows()
