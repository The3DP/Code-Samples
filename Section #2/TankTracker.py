##################################################################
# The3DP                                                        ##
# d73928430@gmail.com                                           ##
# Version 1.0                                                   ##
# FileName: TankTracker.py                                      ##
# 10/20/2025                                                    ##
# This program will calculate how many gallons are              ##
# left in your car per grocery trip (1.3 miles per trip).       ##
# It will also calculate how much gas is now availiable with    ##
# an additional 5 gallon onboard emergency tank.                ##
##################################################################

##### PSUEDOCODE ########################################
## 1. Prompt user to enter float value for number of
## gallons pumped into car.
##
## 2. Add a trip counter for number of trips.
##
## 3. Use a while loop to show each trip for grocery
## pickup as well as the current status of the 
## gas tank.
##
## 4. When subtracting, ensure that tank_status
## does not go below zero.
##
## 5. Continually output results by understandable text.
##
## 6. Print alert when tank_status is 0.
##
## 7. Provide option for user to apply 
## backup tank.
##
## 8. Show output results for backup tank
## if backup_tank = yes.
###################################################

##1. Prompt user to enter float value for number of gallons pumped into car.
tank_status = float(input("Please enter the number of gallons pumped into car: "))

##2. Add a trip counter for number of trips.
trip_counter = 0

##3. Use while loop to show each trip for grocery pickup and current status of tank.
while tank_status > 0:
    tank_status -= 1.3#Amount of gas per grocery trip.
##4. Ensure that tank_status does not go below zero.
    if tank_status < 0:
        tank_status = 0
    print(tank_status)
    # Count each subtraction from tank_status as 1 trip.
    trip_counter = trip_counter + 1
    # Or: trip_counter += 1

##5. Continually output results by understandable text.
    print("Grocery pickup #", trip_counter, "is complete. You have", tank_status, "gallons remaining!")
    
##6. Print alert when tank_status is 0.
print("Uh oh! It appears your gas tank is empty")

##7. Provide option for user to apply backup tank.
backup_tank = input('''Would you like to use your backup tank (+ 5 gallons)?
[ENTER 'yes' OR 'no'] ''')

# If user enters 'no'...
if backup_tank == "no":
    print("Okay, guess you're stuck out there for good.")
    print("You were able to complete only", trip_counter, "grocery pickups!")

# If user enters 'yes'...
if backup_tank == "yes":
    print("Great! You now have 5 gallons in your tank!")
    print("Calculating grocery trips possible with backup tank ... ")
    tank_status = 5
    while tank_status > 0:
        tank_status -= 1.3 #Amount of gas per grocery trip.
        if tank_status < 0:
            tank_status = 0
        print(tank_status)
        # Count each subtraction from tank_status as 1 trip.
        trip_counter = trip_counter + 1
        # Or: trip_counter += 1

##8. Show output results for backup tank if backup_tank = yes.
    print("Grocery pickup #", trip_counter, "is complete. Unfortuantley, you have", tank_status, "gallons remaining.")
    print("You were able to complete", trip_counter, "grocery pickups!")


    

    
    

    
    







