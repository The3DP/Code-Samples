##################################################################
#                                                 ##
#                                        ##
#                                     ##
# Version 1.0                                                   ##
#          ##
# 9/4/2025                                                      ##
#                               ##
#                            ##
##################################################################

##################### OBJECTIVE #################################
## Write a program that uses nested loops to print
## a multiplication grid from 1 to 10.
##
## The outer loop should iterate through
## numbers from 1 to 10 (the rows).
##
## The inner loop should iterate through
## 1 to 10 (the columns).
##
## Print the product in a formatted grid.
##
## Example output:
## 1 2 3 4 5 6 7 8 9 10
## 2 4 6 8 10 12 14 16 18 20
## 3 6 9 12 15 18 21 24 27 30
## …
## 10 20 30 40 50 60 70 80 90 100
##################################################################



user_input = input("Would you like too see the multiplication table? (y or n) ")

if user_input == 'n':
    print("Okay")
if user_input == 'y':
    print("Great!")
    print("Running multiplication table: ")
    for a in range(1, 11, 1): #1-10
        for b in range(1, 10, 1): #1-9
            print("===", a, b, "===")

mult_put = input("Would you like too see them multiplied? (y or n) ")

if mult_put == 'y':
    print("Awesome!")
    print("===", a * b, "===")
if mult_put == 'n':
    print("Okay... ")
            





