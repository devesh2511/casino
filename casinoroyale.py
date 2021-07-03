import random
from time import sleep
import math
import os

totalMoney = 10000
continuer = True

while continuer :
    print("\nYou start the game with!", totalMoney, '$ \n')
    numeroMise = -1

    # choose the square on which we put
    while numeroMise < 0 or numeroMise > 50:
        try:
            print("Choose the bet number[0,50]")
            numeroMise = int(input("What is your choice? ..."))
        except ValueError:
            print("you haven't introduced anything.")
            numeroMise = -1
        if numeroMise < 0:
            print("you must choose a number greater than 0.")
        elif numeroMise > 50:
            print("you must choose a number less than 50.")

    print("You chose", numeroMise)

    # choose the amount to bet on the number
    mise = 0
    while mise <= 0 or mise > totalMoney:
        mise = input("\nWhat is your stake?")
        try:
            mise = int(mise)
        except ValueError:
            print("you did not choose your stake.")
        if mise <= 0:
            print("The bet is negative or zero.")
        if mise > totalMoney:
            print("You don't have enough agent. You have", totalMoney)

    # start roulette
    print("\nThe croupier launches the roulette wheel ...")
    numeroGagnant = random.randrange(0, 50)
    sleep(2)
    print("the roulette wheel stops on", numeroGagnant)

    # processing
    if numeroGagnant == numeroMise:
        print("\nYou bet on the right number, you win", mise *3, '$')
        totalMoney += mise * 3
    elif numeroGagnant % 2 == numeroMise % 2:
        print("\nYou bet on the right color, you win", math.ceil(mise * 0.5), '$')
        totalMoney += math.ceil(mise * 0.5)
    else:
        print("\nSorry you lost", mise, '$')
        totalMoney -= mise

    # Game over
    if totalMoney <= 0:
        print("\nYou're ruined, it's the end of the party")
        continuer = False
    else:
        print("\nyou have now", totalMoney, '$')
        quitter = input("\nDo you want to quit the game(o/n)?")
        if quitter == 'o' or quitter == 'O':
            print("\nYou leave the casino with", totalMoney, '$')
            continuer = False
print("\nTry out more games by restarting the terminal")
os.system("pause")
