import random

# ANSI sequences for formatting of output
ENDC = '\033[0m'
BOLD = '\033[1m'
GREEN = '\033[92m'
RED = '\033[91m'

# Display program info
print(f'''{BOLD}{GREEN}
************************************
*     Role Playing Game - Dices    *
*               by                 *
*  (c) 2022 Karl-Henry Martinsson  *
*  License: MIT                    *
************************************
{ENDC}
Dice supported: D4, D6, D8, D10, D12 and D20
''')

# Continue to roll new dices until rollAgain is set to false
rollAgain = True
while rollAgain:
    # Get the combination to use, e.g 3D6 or 2D8
    diceCombination = input("\nEnter dice combination (X to exit):")
    if diceCombination.upper()=="X":
        # User entered X, set rollAgaint to false and exit
        rollAgain = False
        break
    # Split the entered combination into number of rolls to make
    # and number of sides on the dice to use. 
    values = diceCombination.upper().split("D")
    # If there are not exactly two values, the correct format was not used
    if len(values)!=2:
        print("Use the format xDn, where x is the number of times to roll")
        print("and n is the number of sides on the dice.")
        print("Examples: 3D6, 1D8, 2D10")
    else:
        # Set min and max values for the dice
        diceMin = 1
        diceMax = int(values[1])
        # Set the number of times to roll the dice
        numRoll = int(values[0])
        # Store the aggregated total for all rolls in rollTotal
        rollTotal = 0
        rollTracker = ""
        # Roll the selected dice the specified number of times and aggregate the results
        for i in range(numRoll):
            roll = random.randint(diceMin, diceMax)
            rollTotal += roll 
            # Keep track of each roll, to display later to the users.
            # For the first roll only: use upper case D
            # Add comma between each roll, except for before the last one
            if i==0:
                rollTracker += "Dice "
            elif i < numRoll-1:
                rollTracker += ", dice "
            else:
                rollTracker += " and dice "
            rollTracker += str(i+1)+" rolled "+BOLD+str(roll)+ENDC
        # Display the result of the roll(s) to the user
        print(f"Your {diceCombination.upper()} rolled the value {BOLD}{rollTotal}{ENDC} as follows:")
        print(rollTracker+"\n")
