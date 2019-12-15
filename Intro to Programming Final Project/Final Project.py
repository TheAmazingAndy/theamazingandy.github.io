# Andrew Mitchell
# Car Sales Final Project

def outputWelcomeMessage():
    print("\nWelcome to Andy's Car Customizer!\n")


def getVehicleMake():
    userMakeChoice = None

    print("Which make of vehicle would you like to purchase? ")
    print("1. Ford")
    print("2. Chevrolet")
    print("3. Toyota")
    print("4. Honda")

    while userMakeChoice == None or userMakeChoice <= 0 or userMakeChoice > 3:
        try:
            userMakeChoice = int(input())
        except:
            print("Plese enter a valid number (1-3)")
            continue
        
        if userMakeChoice == 1:
            return "Ford"
        elif userMakeChoice == 2:
            return "Chevrolet"
        elif userMakeChoice == 3:
            return "Toyota"
        elif userMakeChoice == 4:
            return "Honda"
        else:
            print("Plese enter a valid number (1-4)")

def getVehicleType():
    userVehicleChoice = None

    print("Which type of vehicle would you like to purchase? ")
    print("1. Car - Base Cost = $20,000")
    print("2. Truck - Base Cost = $50,000")
    print("3. SUV - Base Cost = $30,000")

    while userVehicleChoice == None or userVehicleChoice <= 0 or userVehicleChoice > 3:
        try:
            userVehicleChoice = int(input())
        except:
            print("Plese enter a valid number (1-3)")
            continue
        
        if userVehicleChoice == 1:
            return "car"
        elif userVehicleChoice == 2:
            return "truck"
        elif userVehicleChoice == 3:
            return "SUV"
        else:
            print("Plese enter a valid number (1-3)")
    
    

    

def getVehicleOptions():
    optionsList = {}
    userOptionsChoice = None

    print("What additional options would you like to add?")
    print("0. None")
    print("1. Sun Roof - $400")
    print("2. Leather Interior - $900")
    print("3. Bluetooth Audio Package - $600")
    print("4. A/C - 300")
  
    while True:
        try:
            userOptionsChoice = int(input())
        except:
            print("Please enter a valid number (0-4)")
            continue
                  
        if userOptionsChoice == 0:
            return optionsList
        elif userOptionsChoice == 1:
            optionsList.update(Engine = 400)
        elif userOptionsChoice == 2:
            optionsList.update(Exhaust = 900)
        elif userOptionsChoice == 3:
            optionsList.update(Interior = 600)
        elif userOptionsChoice == 4:
            optionsList.update(Exterior = 300)
        else:
            print("Please enter a valid number (0-4)")

        print("Would you like any additional options? ")
            

def getVehicleColor():
    userColorChoice = None
    print("Retreiving current color options from our file:\n")
    text_file = open("colors.txt", "r")
    lines = text_file.readlines()
    for line in lines:
        print(line)
    text_file.close()

    print("What color paint would you like? ")
    print("1. Red")
    print("2. White")
    print("3. Black")
    print("4. Blue")
    print("5. Yellow")
    
    while userColorChoice == None or userColorChoice <= 0 or userColorChoice > 3:
        try:
            userColorChoice = int(input())
        except:
            print("Plese enter a valid number (1-5)")
            continue
        
        if userColorChoice == 1:
            return "red"
        elif userColorChoice == 2:
            return "white"
        elif userColorChoice == 3:
            return "black"
        elif userColorChoice == 4:
            return "blue"
        elif userColorChoice == 5:
            return "yellow"
        
        else:
            print("Plese enter a valid number (1-5)")
    
    
def calculateTotal(discountType, vehicleType, optionsList):

    totalAmount = 0
    discountAmount = 0

    if vehicleType == "car":
        totalAmount += 20000
    elif vehicleType == "truck":
        totalAmount += 50000
    elif vehicleType == "SUV":
        totalAmount += 30000

    if len(optionsList) != 0:
        for k,v in optionsList.items():
            totalAmount += v

    if discountType == "v":
        discountAmount = 0.2
        totalAmount = totalAmount - (totalAmount * discountAmount)
    elif discountType == "s":
        discountAmount = 0.15
        totalAmount = totalAmount - (totalAmount * discountAmount)

    
    return totalAmount, discountAmount

def outputTotal(vehicleMake, vehicleChoice, vehicleColor, optionChoice, totalAmount, discountAmount):
    print("Here is the total: $" + str(totalAmount) + " including a " + str(discountAmount * 100) + "% discount")
    print("You chose a " + vehicleColor + " " + vehicleMake + " " + vehicleChoice)
    if len (optionChoice) != 0:
            print("With the following options:")
            for k,v in optionChoice.items():
                print(k)
    input("\n Missouri sales tax is 4.225%. Press enter to calculate sales tax.")
    withTax = totalAmount * 1.04
    withTax = round(withTax, 2)
    print("Your total with tax is: $" + str(withTax))
    print("Thank you for shopping with us")
        
            
vehicleMake = None
vehicleChoice = None
vehicleColor = None
optionChoice = None
totalAmount = None
discountAmount = None
userExit = False

outputWelcomeMessage()

while userExit == False:
    vehicleMake = getVehicleMake()
    vehicleChoice = getVehicleType()
    optionChoice = getVehicleOptions()
    vehicleColor = getVehicleColor()
    

    discountType = input("Are you a (V)eteran, or an (S)enior Citizen (or n for none)? ")

    while True:
        if discountType.lower() == "v":
            totalAmount, discountAmount = calculateTotal("v", vehicleChoice, optionChoice)
            break
        elif discountType.lower() == "s":
            totalAmount, discountAmount = calculateTotal("s", vehicleChoice, optionChoice)
            break
        elif discountType.lower() == "n" or discountType.lower() == "none":
            totalAmount, discountAmount = calculateTotal("n", vehicleChoice, optionChoice)
            break
        else:
            discountType = input("Please enter v (for veteran), s (for senior citizen), or none? ")

    #print(str(totalAmount))
    #print(str(discountAmount * 100) + "%")
    outputTotal(vehicleMake, vehicleChoice, vehicleColor, optionChoice, totalAmount, discountAmount)

    userExitChoice = input("Would you like to purchase another vehicle?")

    if userExitChoice.lower() == "n" or userExitChoice.lower() == "no":
        userExit = True
