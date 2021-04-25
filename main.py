from func.class_opener import class_open
from func.name_notifier import notify_me
from func.audio_record import record
from func.ss import screenshot

import time
import threading

import cv2
import pyautogui
import numpy as np

def notifiers():
    global meeting_end
    while meeting_end == False:
        notify_me()

def video_recording():
    codec = cv2.VideoWriter_fourcc(*"XVID")

    out = cv2.VideoWriter("Recorded.avi", codec , 19, (1366, 768)) #Here screen resolution is 1366 x 768, you can change it depending upon your need

    cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Recording", 480, 270) #Here we are resizing the window to 480x270 so that the program doesn't run in full screen in the beginning

    while True:
        img = pyautogui.screenshot() #capturing screenshot
        frame = np.array(img) #converting the image into numpy array representation 
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #converting the BGR image into RGB image
        out.write(frame) #writing the RBG image to file
        cv2.imshow('Recording', frame) #display screen/frame being recorded
        if cv2.waitKey(1) == ord('q'): #Wait for the user to press 'q' key to stop the recording
            break


    out.release() #closing the video file
    cv2.destroyAllWindows() #destroying the recording window

def audio_recording():
    record()

def class_end():
    time.sleep(20)
    global meeting_end
    meeting_end = True

def takess():
    global meeting_end
    while meeting_end == False:
        screenshot()
        

meeting_end = False
class_open()

notifier = threading.Thread(target=notifiers, args=())
notifier.start()

video = threading.Thread(target=video_recording, args=())
video.start()

audio = threading.Thread(target=audio_recording, args=())
audio.start()

timer = threading.Thread(target=class_end, args=())
timer.start()

ssk = threading.Thread(target=takess, args=())
ssk.start()


time.sleep(30)
notifier.join()
video.join()

print('Meeting Ended')



