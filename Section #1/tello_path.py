from djitellopy import Tello

#Create a tello Object
drone = Tello()

# Connect to Tello Drone
drone.connect()

# Get battery status
print("Battery:", drone.get_battery())

# Take off
drone.takeoff()

# Fly up 5 seconds
drone.move_up(100)

# Fly down 2.5 seconds
drone.move_down(50)
