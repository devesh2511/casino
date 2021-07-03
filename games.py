print('')
print('~~WELCOME TO THE CASINO TERMINAL.... '
      '\n ..THE ALL NEW GAMING PLATFORM! ')
a = str(input('\n ~~Please enter your name: '))
print("\n ~~HELLO",a,'Hope you have good luck today and return with a heavier bag :) \n ')
print('Enter 1 for Playing the gambling 7UP 7DOWN Game \n')
print('Enter 2 for Playing Blackjack Game\n')
print('Enter 3 for Playing Roulette Wheel Game\n')
choice = int(input('Enter your choice:'))
if (choice == 1):
    exec(open('gamble7.py').read())
if (choice == 2):
    exec(open('blackjack.py').read())
if (choice == 3):
        exec(open('casinoroyale.py').read())
else:
    print('Please enter a valid option')
