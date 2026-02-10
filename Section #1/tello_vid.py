import cv2
from djitellopy import Tello
import time

# Initialize the Tello drone
tello = Tello()
tello.connect()
tello.streamon()

#try:
#    # Take off and set an initial height
#    tello.takeoff()
#    tello.move_up(50)  # Adjust initial height as needed
#
#    while True:
#        # Capture video frame-by-frame
#        frame = tello.get_frame_read().frame
#        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
