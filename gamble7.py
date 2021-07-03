import random
# START MENUE
print(" ")
print(" ~~GET THE FEEL OF CASINO AT YOUR TERMINAL.. TRY HACKING IT!!~~")
print("         THE GAMBLING BOT      ")
print(" ")
print("  GOLD      DIAMOND      SILVER  ")
print("         |           |         ")
print(" 2    3  |           |  8    9 ")
print("         |           |         ")
print("    4    |     7     |    10    ")
print("         |           |         ")
print(" 5    6  |           |  11    12")
print("-- HEY GUYS -- !! \n  WE ARE PRESENTING THE MOST SURPRISING AND INNOVATIVE \n"
      "    GAMBLING GAME OF ALL TIMES FOR YOU"
      "\n   RULES OF THE GAME "
      "\n 1] There are 3 CLANS namely.. 'GOLD', 'DIAMOND', and 'SILVER' .. As shown above "
      "\n 2] Two dice are rolling simultaneously .. "
      "\n 3] Dice rolling will stop once you choose a clan to bid in"
      "\n 4] Sum of the numbers shown by the dice will be the 'Lucky Number"
      "\n 5] Choose any one clan that you predict can contain the 'Lucky Number' "
      "\n 6] Enter the amount of money you like to bid in a clan"
      "\n 7] If you predicted the right clan containing the Lucky Number .. 'Your money will be DOUBLED' .. "
      "\n or else you will loose your money.. Special Case for 7 as here your money gets TRIPLED"
      "\n GET STARTED !! HOPE YOU LIKE IT!!"
      "\n -----------------------------------"
    )
# THE MAIN CODE OF GAME
Money=int(input("Enter the amount of money you would like to bid:"))
print("Choose any one clan from the below three as 'g' or 'd' or 's' ")
print(" g) GOLD  \n d) DIAMOND \n s) SILVER")
g="Clan GOLD"
d="Clan DIAMOND"
s="Clan SILVER"
print(" ")
print("  GOLD     DIAMOND      SILVER ")
print("         |           |         ")
print(" 2    3  |           |  8    9 ")
print("         |           |         ")
print("    4    |     7     |    10    ")
print("         |           |         ")
print(" 5    6  |           |  11    12")
options=input("Enter the option number you want to take :")
number=random.choice([2,3,4,5,6,7,8,9,10,11,12])
print("The lucky number is",number)
if options== "g":
  if number <= 6:

        print("YAY!! Your Money is Doubled!!:" ,Money*2)
  else:
         print("OOPS! Your Money is Lost :" ,Money*0)
if(options=="d"):
 if(number==7):
      print("YAY!! Your Money is Doubled:" ,Money*3)
 else:
      print("OOPS! Your Money is Lost:" ,Money*0)
if(options=="s"):
 if(7<number<=12):
      print("YAY!! Your money is Doubled:" ,Money*2)
 else:
      print("OOPS! Your money is Lost:" ,Money*0)