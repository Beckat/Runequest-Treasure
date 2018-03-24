#Cori Thompson
#3/17/2017

from collections import namedtuple
import random
from random import randint
import sys

#holds the total number of clack coins in the treasure horde
totalClacks = 0
#holds the percentage chance that clack coins were found
clackChance = 75
##holds the total number of silver Lunar coins in the treasure horde
totalLunars = 0
#holds the percentage chance that silver Lunar coins were found
lunarChance = 75
#holds the total number of golden wheel coins in the treasure horde
totalWheels = 0
#holds the percentage chance that golden wheel coins were found
wheelChance = 5
#Holds the list of all gems found as string
gems = "All the gems:\n"
#Holds the percentage chance that gems were found
gemChance = 50
#Holds the number of gems that were found
gemNumber = 0
#Holds the list of all special items found as string
specialItems = "All the special items:\n"
#Holds the percentage chance that special items were found
specialItemChance = 5


#Gets the total treasure factor between all enemies encountered, input is an integer 1 or higher
totalTreasureFactor = int(input("What is the total treasure factor:"))
#Holds the amount of treasure factor left (If initial treasure is greater than 100 the remainder is also turned into treasure in 100 or less increments
currentTreasureFactor = 0

#Gets the treasure factor for each item.
#This is found by "rolling" a d100 and checking to see if it is less than the chance to find
#If it is higher then treasure factor is 0, or none of this treasure
#If the number "rolled" is half the required number the treasure found is doubled
#If the number is 1/4th needed treasure is tripled
#If the number is 1/8th needed treasure is quadrupled
#If the number is 1/10th needed treasure is multiplied by 5
#If the number is 1/20th needed treasure is multiplied by 10
def getTreasureFactor(treasureChance):
    randomRoll = randint(1,100)
    treasureDivisor = 1
    treasureMultiplyer = 1

    if(treasureChance >= randomRoll):
        treasureDivisor = treasureChance / randomRoll
        if treasureDivisor >= 20:
            treasureMultiplyer = 10
        elif treasureDivisor >= 10:
            treasureMultiplyer = 5
        elif treasureDivisor >= 8:
            treasureMultiplyer = 4
        elif treasureDivisor >= 4:
            treasureMultiplyer = 3
        elif treasureDivisor >= 2:
            treasureMultiplyer = 2
        else:
            treasureMultiplyer = 1
    else:
        treasureMultiplyer = 0
    return treasureMultiplyer


#Gets Spells or Special Items
def getSpells():
    #Initial d100 "roll" to find what type of item is found
    randomRoll = randint(1,100)
    spellDescription = ""

    #1-35 are scrolls
    if randomRoll >= 1 and randomRoll <= 35:
        randomRoll2 = randint(1,100)
        if randomRoll2 == 1:
            spellDescription = "Referee's Discretion"
        elif randomRoll2 >= 2 and randomRoll2 <= 15:
            randAtt = randint(1,4)
            if randAtt == 1:
                spellDescription = "Strength Increasing Scroll"
            elif randAtt == 2:
                spellDescription = "Constitution Increasing Scroll"
            elif randAtt == 3:
                spellDescription = "Dexterity Increasing Scroll"
            else:
                spellDescription = "Charisma Increasing Scroll"
        elif randomRoll2 >= 16 and randomRoll2 <= 30:
            spellDescription = "Letter of credit, deed, valuable historical knowledge"
        elif randomRoll2 >= 31 and randomRoll2 <= 50:
            techniqueRaise = 5 * randint(1,4)
            spellDescription = "Secret technique scroll raising weapon skill " + str(techniqueRaise) + " max 75%"
        elif randomRoll2 >= 51 and randomRoll2 <= 65:
            randTech = randint(1,6)
            randPerc = 5 * randint(1,4)
            if randTech == 1:
                spellDescription = "Knowledge increasing scroll " + str(randPerc) + "% max 75%"
            elif randTech == 2:
                spellDescription = "Perception increasing scroll " + str(randPerc) + "% max 75%"
            elif randTech >= 3 and randTech <= 4:
                spellDescription = "Manipulation increasing scroll " + str(randPerc) + "% max 75%"
            else:
                spellDescription = "Stealth increasing scroll " + str(randPerc) + "% max 75%"
        elif randomRoll2 >= 66 and randomRoll2 <= 75:
            spellDescription = "Map to an interesting location "
        else:
            spellDescription = "Useless or unreadable scroll"

    #36-60 are potions
    elif randomRoll >= 36 and randomRoll <= 60:
        randomRoll2 = randint(1,100)
        if randomRoll2 >= 1 and randomRoll2 <= 10:
            spellDescription = "Healing Potion"
        elif randomRoll2 >= 11 and randomRoll2 <= 25:
            randomSpell = randint(1,50)
            spellDescription = "Battle Magic Spell " + str(randomSpell)
        elif randomRoll2 >= 26 and randomRoll2 <= 55:
            poisonPot = 3 + randint(1,6) + randint(1,6)
            spellDescription = "Systemic Poison potency " + str(poisonPot)
        elif randomRoll2 >= 56 and randomRoll2 <= 65:
            poisonPot = 3 + randint(1,6) + randint(1,6)
            spellDescription = "Blade Venom potency " + str(poisonPot)
        elif randomRoll2 >= 66 and randomRoll2 <= 80:
            spellDescription = "Poison Antidote"
        elif randomRoll2 >= 81 and randomRoll2 <= 90:
            spellDescription = "Referee's choice potion"
        else:
            spellDescription = "Spoiled Potion"
    #61-85 are magic spells
    elif randomRoll >= 61 and randomRoll <= 85:
        randomRoll2 = randint(1,50)
        spellDescription = "Battle Magic Matrix " + str(randomRoll2)
    #86-100 are magic crystals
    else:
        spellDescription = getMagicCrystals()
    return spellDescription + "\n"

#Gets magic crystals
def getMagicCrystals():
        magicDescription = ""
        #"Rolls" a d100 to find what type of magic crystal is found
        randomRoll2 = randint(1, 100)
        #1 Creates two magic crystals instead of 1
        if randomRoll2 == 1:
            magicDescription = getMagicCrystals()
            magicDescription += getMagicCrystals()
        #2 gets a power storing crystal of 3d6 + 3 size
        elif randomRoll2 == 2:
            totalPower = 3
            totalPower  += randint(1, 6)
            totalPower  += randint(1, 6)
            totalPower  += randint(1, 6)
            magicDescription = "Power/Spirit Storing Crystal " + str(totalPower)
        #3-5 creates a healing focusing crystal
        elif randomRoll2 >= 3 and randomRoll2 <= 5:
            healingFocus = randint(1,8)
            magicDescription = "Healing Focusing Crystal " + str(healingFocus)
        #6-8 creates a sensitivity crystal
        elif randomRoll2 >= 6 and randomRoll2 <= 8:
            sensitivity = randint(1,8)
            magicDescription = "Sensitivity Crystal " + str(sensitivity)
        #9-11 creates a powerstoring crystal of 1d8 doubled
        elif randomRoll2 >= 9 and randomRoll2 <= 11:
            powerStoring = 2 * randint(1, 8)
            magicDescription = "Power storing Crystal " + str(powerStoring)
        #12-14 creates a power enchancing crystal of strength 1d8
        elif randomRoll2 >= 12 and randomRoll2 <= 14:
            powerEnhancing = randint(1, 8)
            magicDescription = "Power enhancing Crystal " + str(powerEnhancing)
        #15-16 creates a spell reinforcing crystal
        elif randomRoll2 >= 15 and randomRoll2 <= 16:
            spellReinforcing = randint(1,4)
            magicDescription = "Spell reinforcing Crystal " + str(spellReinforcing)
        #17-18 creates a spell strengthening crystal of strength 1d4
        elif randomRoll2 >= 17 and randomRoll2 <= 18:
            spellStrength = randint(1,4)
            magicDescription = "Spell strengthening Crystal " + str(spellStrength)
        #19-20 creates a spell resisting crystal of 1d4 strength
        elif randomRoll2 >= 19 and randomRoll2 <= 20:
            spellResisting = randint(1,4)
            magicDescription = "Spell resisting Crystal " + str(spellResisting)
        #21-22 creates a spirit supporting crystal of 1d4 strength
        elif randomRoll2 >= 21 and randomRoll2 <= 22:
            spiritSupporting = randint(1,4)
            magicDescription = "Spirit supporting Crystal " + str(spiritSupporting)
        #23-24 creates a spell storing crystal of strength 1d4
        elif randomRoll2 >= 23 and randomRoll2 <= 24:
            spellStoring = randint(1,4)
            magicDescription = "Spell storing Crystal" + str(spellStoring)
        #25-30 creates a flawed crystal
        elif randomRoll2 >= 25 and randomRoll2 <= 30:
            magicDescription = "Flawed Crystal"
        #31-100 creates a powerstoring crystal of 2d6 + 3
        else:
            powerStoring = 3
            powerStoring += randint(1,6)
            powerStoring += randint(1,6)
            magicDescription = "Power storing Crystal " + str(powerStoring)

        return  magicDescription + "\n"

#Creates nonmagical gems
def getGems():
    gemDescription = ""
    #"Rolls" a d100 to find what type of gem is created
    randomRoll = randint(1, 100)
    gemValue = 0

    #1 gets a different gem and adds a special item
    if randomRoll == 1:
        gemDescription = getGems()
        global specialItems
        specialItems += getSpells()
    #2 creates a magic crystal instead
    elif randomRoll == 2:
        gemDescription = getMagicCrystals()
    #3 creates a gem of 1d20 * 10000 value
    elif randomRoll == 3:
        gemValue = randint(1,20) * 10000
        gemDescription = "Ancient Treasure " + str(gemValue)
    #4-5 creates a gem of 3d6 * 1000 value
    elif randomRoll >= 4 and randomRoll <= 5:
        gemValue = ((randint(1,6) + randint(1,6) + randint(1,6)) * 1000)
        gemDescription = "Heirloom Treasure " + str(gemValue)
    #6-10 creates a gem worth 1d10 * 1000
    elif randomRoll >= 6 and randomRoll <= 10:
        gemValue = randint(1,10) * 1000
        gemDescription = "Superb Gemstone " + str(gemValue)
    #11-15 creates a gem worth 1d6 * 1000
    elif randomRoll >= 11 and randomRoll <= 15:
        gemValue = randint(1,6) * 1000
        gemDescription = "Excellent Jewelry " + str(gemValue)
    #16-20 creates a gem worth 3d6 * 100
    elif randomRoll >= 16 and randomRoll <= 20:
        gemValue = ((randint(1,6) + randint(1,6) + randint(1,6)) * 100)
        gemDescription = "Excelent Gem " + str(gemValue)
    #21-30 creates a gem worth 12d100
    elif randomRoll >= 21 and randomRoll <= 30:
        gemValue = (randint(1,100) + randint(1,100) + randint(1,100) + randint(1,100) + randint(1,100) + randint(1,100) + randint(1,100) + randint(1,100) + randint(1,100) + randint(1,100) + randint(1,100) + randint(1,100))
        gemDescription = "Very Good Jewelry " + str(gemValue)
    #Creates a gem worth 6d100
    elif randomRoll >= 31 and randomRoll <= 40:
        gemValue = (randint(1,100) + randint(1,100) + randint(1,100) + randint(1,100) + randint(1,100) + randint(1,100))
        gemDescription = "Very Good Gem " + str(gemValue)
    #Creates a gem worth 10d20
    elif randomRoll >= 41 and randomRoll <= 50:
        gemValue = (randint(1,20) + randint(1,20) + randint(1,20) + randint(1,20) + randint(1,20) + randint(1,20) + randint(1,20) + randint(1,20) + randint(1,20) + randint(1,20))
        gemDescription = "Good Jewelry " + str(gemValue)
    #Creates a gem worth 2d100
    elif randomRoll >= 51 and randomRoll <= 60:
        gemValue = randint(1, 100) + randint(1, 100)
        gemDescription = "Good Gem " + str(gemValue)
    #Creates a gem worth 5d20
    elif randomRoll >= 61 and randomRoll <= 70:
        gemValue = (randint(1,20) + randint(1,20) + randint(1,20) + randint(1,20) + randint(1,20))
        gemDescription = "Costume Jewelry " + str(gemValue)
    #Creates a gem worth 1d100
    elif randomRoll >= 71 and randomRoll <= 80:
        gemValue = randint(1, 100)
        gemDescription = "Flawed Gemstone " + str(gemValue)
    #Creates a gem worth 1d20
    elif randomRoll >= 81 and randomRoll <= 90:
        gemValue = randint(1,20)
        gemDescription = "Trade Junk Jewelry " + str(gemValue)
    #Creates a gem worth 1d10
    elif randomRoll >= 91 and randomRoll <= 95:
        gemValue = randint(1,10)
        gemDescription = "Semi-Precious Stones " + str(gemValue)
    #Creates a worthless gem
    else:
        gemDescription = "Rock Candy"
    return gemDescription + "\n"

#Checks to make sure there is still treasure left to generate, finishes once all treasure is created
while totalTreasureFactor > 0:

    #Sets special item number back to the default of 1 in case it was modified in the previous loop iteration
    specialItemsNumber = 1

    #If there is more than 100 treasure run this iteration at 100 and subtract it from treasure remaining
    if(totalTreasureFactor > 100):
        currentTreasureFactor = 100
        totalTreasureFactor -= 100
    #If the treasure is 100 or less this iteration will run on all of it and then finish because total treasure will then be 0
    else:
        currentTreasureFactor = totalTreasureFactor
        totalTreasureFactor -= currentTreasureFactor

    #The current treasure factor determines the chance for each item and the number of gems
    if(currentTreasureFactor > 0 and currentTreasureFactor < 11):
        clackChance = 75
        lunarChance = 75
        wheelChance = 50
        gemChance = 50
        gemNumber = 1
        specialItemChance = 5
    elif (currentTreasureFactor > 10 and currentTreasureFactor < 21):
        clackChance = 85
        lunarChance = 85
        wheelChance = 65
        gemChance = 65
        gemNumber = 1
        specialItemChance = 10
    elif (currentTreasureFactor > 20 and currentTreasureFactor < 31):
        clackChance = 95
        lunarChance = 95
        wheelChance = 75
        gemChance = 75
        gemNumber = 1
        specialItemChance = 15
    elif (currentTreasureFactor > 30 and currentTreasureFactor < 41):
        clackChance = 95
        lunarChance = 95
        wheelChance = 90
        gemChance = 90
        gemNumber = 1
        specialItemChance = 20
    elif (currentTreasureFactor > 40 and currentTreasureFactor < 51):
        clackChance = 95
        lunarChance = 95
        wheelChance = 95
        gemChance = 95
        gemNumber = 1
        specialItemChance = 25
    elif (currentTreasureFactor > 50 and currentTreasureFactor < 61):
        clackChance = 95
        lunarChance = 95
        wheelChance = 95
        gemChance = 95
        gemNumber = 1
        specialItemChance = 30
    elif (currentTreasureFactor > 60 and currentTreasureFactor < 71):
        clackChance = 95
        lunarChance = 95
        wheelChance = 95
        gemChance = 95
        gemNumber = 2
        specialItemChance = 35
    elif (currentTreasureFactor > 70 and currentTreasureFactor < 81):
        clackChance = 95
        lunarChance = 95
        wheelChance = 95
        gemChance = 95
        gemNumber = 2
        specialItemChance = 40
    elif (currentTreasureFactor > 80 and currentTreasureFactor < 91):
        clackChance = 95
        lunarChance = 95
        wheelChance = 95
        gemChance = 95
        gemNumber = 2
        specialItemChance = 45
    else:
        clackChance = 95
        lunarChance = 95
        wheelChance = 95
        gemChance = 95
        gemNumber = 3
        specialItemChance = 50

    #Gets the treaure factor for each type of item (Multiplyer for base values)
    clackTreasureFactor = getTreasureFactor(clackChance)
    lunarTreasureFactor = getTreasureFactor(lunarChance)
    wheelTreasureFactor = getTreasureFactor(wheelChance)
    gemTreasureFactor = getTreasureFactor(gemChance)
    specialTreasureFactor = getTreasureFactor(specialItemChance)

    gemNumber *= gemTreasureFactor
    specialItemsNumber *= specialTreasureFactor

    #Gets gems if there are gems to create
    if gemNumber > 0:
     for x in range(0, gemNumber):
        gems += getGems()

    #Gets special items and spells if there are some to create
    if specialItemsNumber > 0:
        for y in range(0, specialItemsNumber):
            specialItems += getSpells()

    #Adds the number of coins for each type
    if(currentTreasureFactor > 0 and currentTreasureFactor < 11):
        totalClacks += (clackTreasureFactor * randint(1, 100))
        totalLunars += (lunarTreasureFactor * randint(1,10))
        totalWheels += (wheelTreasureFactor * randint(1, 6))
    elif (currentTreasureFactor > 10 and currentTreasureFactor < 21):
        totalClacks += (clackTreasureFactor * randint(1, 100))
        totalLunars += (lunarTreasureFactor * randint(1,100))
        totalWheels += (wheelTreasureFactor * randint(1, 10))
    elif (currentTreasureFactor > 20 and currentTreasureFactor < 31):
        totalClacks += (clackTreasureFactor * (randint(1, 100) + randint(1, 100)))
        totalLunars += (lunarTreasureFactor * (randint(1, 100) + randint(1, 100)))
        totalWheels += (wheelTreasureFactor * randint(1, 10))
    elif (currentTreasureFactor > 30 and currentTreasureFactor < 41):
        for x in range(0, 3):
            totalClacks += (clackTreasureFactor * randint(1, 100))
        for x in range(0, 3):
            totalLunars += (lunarTreasureFactor * randint(1, 100))
        totalWheels += (wheelTreasureFactor * randint(1, 20))
    elif (currentTreasureFactor > 40 and currentTreasureFactor < 51):
        for x in range(0, 8):
            totalClacks += (clackTreasureFactor * randint(1, 100))
        for x in range(0, 4):
            totalLunars += (lunarTreasureFactor * randint(1, 100))
        for x in range(0, 2):
            totalWheels += (wheelTreasureFactor * randint(1, 20))
    elif (currentTreasureFactor > 50 and currentTreasureFactor < 61):
        for x in range(0, 10):
            totalClacks += (clackTreasureFactor * randint(1, 100))
        for x in range(0, 5):
            totalLunars += (lunarTreasureFactor * randint(1, 100))
        for x in range(0, 3):
            totalWheels += (wheelTreasureFactor * randint(1, 20))
    elif (currentTreasureFactor > 60 and currentTreasureFactor < 71):
        for x in range(0, 10):
            totalClacks += (clackTreasureFactor * randint(1, 100))
        for x in range(0, 6):
            totalLunars += (lunarTreasureFactor * randint(1, 100))
        for x in range(0, 5):
            totalWheels += (wheelTreasureFactor * randint(1, 20))
    elif (currentTreasureFactor > 70 and currentTreasureFactor < 81):
        for x in range(0, 20):
            totalClacks += (clackTreasureFactor * randint(1, 100))
        for x in range(0, 10):
            totalLunars += (lunarTreasureFactor * randint(1, 100))
        for x in range(0, 2):
            totalWheels += (wheelTreasureFactor * randint(1, 100))
    elif (currentTreasureFactor > 80 and currentTreasureFactor < 91):
        for x in range(0, 20):
            totalClacks += (clackTreasureFactor * randint(1, 100))
        for x in range(0, 10):
            totalLunars += (lunarTreasureFactor * randint(1, 100))
        for x in range(0, 3):
            totalWheels += (wheelTreasureFactor * randint(1, 100))
    else:
        for x in range(0, 30):
            totalClacks += (clackTreasureFactor * randint(1, 100))
        for x in range(0, 20):
            totalLunars += (lunarTreasureFactor * randint(1, 100))
        for x in range(0, 4):
            totalWheels += (wheelTreasureFactor * randint(1, 100))

#Prints the total list of tresure created
print("Total Clacks " + str(totalClacks) + "\n")
print("Total Lunars " + str(totalLunars) + "\n")
print("Total Wheels " + str(totalWheels) + "\n")
print("Crystals " + str(gems) + "\n")
print("Special Items " + str(specialItems) + "\n")