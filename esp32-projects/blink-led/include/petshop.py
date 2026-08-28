#Pet Store variables
currentPetCount = 7
maxPetCapacity = 24
petPrices = 65
petTypes = ["Dog", "Cat", "Bird", "Lizard", "Fish", "Turtle", "Hamster" ]
foodTotal = 60
costPerUnit = 10
totalCost = foodTotal * costPerUnit

def NewPet():
    global currentPetCount
    print("Aqcuiring new pet - Starting...")
    if currentPetCount >= maxPetCapacity:
        print(f"you can not have any more pets!")
    else:
        currentPetCount += 1
        print(f"Current pet count is now: {currentPetCount}")

def DisplayTypes():
    print("Pet Types:")
    print(" - ".join(petTypes))

def PetFood(foodTotal=60, costPerUnit=10):
    totalCost = foodTotal * costPerUnit
    return totalCost

def main():
    while(True):
        message = '''
        Please select from the following options
        1. Add new pet
        2. Display Pet Types
        3. Total Food Cost
        0. Exit the menu
        '''
        selection = int(input(message))
        if selection == 1:
            NewPet()
        elif selection == 2:
            DisplayTypes()
        elif selection == 3:
            foodTotal = float(input(f"Total Food: "))
            costPerUnit = float(input(f"Cost per Unit: "))
            print(f"the cost of the food is: {PetFood(foodTotal, costPerUnit)}")
        elif selection == 0:
            print("Exiting with expected code.")
            exit(202)
            break
        else:
            print("Bad selection!")

main()