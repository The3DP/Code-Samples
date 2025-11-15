from djitellopy import Tello
import time
#Create an instance of the Tello class
tello = Tello()
# Connect to the Tello drone
tello.connect()
# Check battery level (optional)
battery = tello.get_battery()
print(f"Battery level: {battery}%")
tello.takeoff
tello.rotate_clockwise(360)
send_command("camera bottom")
