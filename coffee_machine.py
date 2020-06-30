# Write your code here
water = 400
milk = 540
beans = 120
cups = 9
cash = 550

action = ''
while action != 'exit':

    action = input("Write action (buy, fill, take, remaining, exit):")

    if action == 'buy':
        buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")

        if buy == '1':
            if water < 250:
                print("Sorry, not enough water!")
            elif beans < 16:
                print("Sorry, not enough coffee beans!")
            elif cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                water -= 250
                beans -= 16
                cups -= 1
                cash += 4
            print()

        elif buy == '2':
            if water < 350:
                print("Sorry, not enough water!")
            elif milk < 75:
                print("Sorry, not enough milk!")
            elif beans < 20:
                print("Sorry, not enough coffee beans!")
            elif cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                water -= 350
                milk -= 75
                beans -= 20
                cups -= 1
                cash += 7
            print()

        elif buy == '3':
            if water < 200:
                print("Sorry, not enough water!")
            elif milk < 100:
                print("Sorry, not enough milk!")
            elif beans < 12:
                print("Sorry, not enough coffee beans!")
            elif cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a coffee!")
                water -= 200
                milk -= 100
                beans -= 12
                cups -= 1
                cash += 6
            print()

        else:
            continue

    elif action == 'fill':
        water1 = int(input("Write how many ml of water do you want to add:"))
        milk1 = int(input("Write how many ml of milk do you want to add:"))
        beans1 = int(input("Write how many grams of coffee beans do you want to add:"))
        cups1 = int(input("Write how many disposable cups of coffee do you want to add:"))
        print()
        water += water1
        milk += milk1
        beans += beans1
        cups += cups1

    elif action == 'take':
        print("I gave you $" + str(cash))
        print()
        cash = 0

    elif action == 'remaining':
        print()
        print("The coffee machine has:")
        print(str(water) + " of water")
        print(str(milk) + " of milk")
        print(str(beans) + " of coffee beans")
        print(str(cups) + " of disposable cups")
        print('$' + str(cash) + " of money")
        print()
