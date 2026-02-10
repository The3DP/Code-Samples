##################################################################################################
## longest Lichess (lichess.org) Games played
## (BAGP)
## Made: 1/4/2026
## OBJ: Include a list of longest played games. (not including games against official and unofficial bots)
## Example Username: Matirx
## We will include Matirx's 5 longest games which resulted in victories.
##################################################################################################

# Import time module
import time

### Variable Bank ###
username = "Matirx"
games_number = 5
opponent1 = hendraraira
o_rating1 = 1329 #apply this to later updates
moves1 = 49 #apply this to later updates
variant1 = "Atomic" #apply this to later updates
opponent2 = "USAChamp"
o_rating2 = "1500? (provisional)"
moves2 = 46
variant2 = "Horde"
opponent3 = "Lemonwola"
o_rating3 = 1735
moves3 = 45
variant3 = "Atomic"
opponent4 = "mahatma09"
o_rating4 = 1901
moves4 = 44
variant4 = "Standard"
opponent5 = "C4LTom"
o_rating5 = "2203? (provisional)"
moves5 = 43
variant5 = "Horde"
#####################

print("NOTE: Shows victories in this order: largest to smallest")
time.sleep(0.2)
print(" ...")
time.sleep(0.3)
print("Displaying", games_number, "longest victories for:", username)

print("Victory #1 was against", opponent1, "Their rating was", o_rating1)

print("Victory #2 was against", opponent2, "Their rating was", o_rating2)

print("Victory #3 was against", opponent3, "Their rating was", o_rating3)

print("Victory #4 was against", opponent4, "Their rating was", o_rating4)

print("Victory #5 was against", opponent5, "Their rating was", o_rating5)

## Archived information
#opponent1 = skywalker_luke_be
#rating1 = "1686? (provisional)"
#opponent2 = C4LTom
#rating2 = "2203? (provisional)"
#opponent3 = "Knezwolf"
#rating3 = "1874? (provisional)"
## ====================
