#using <CoffeeDispenser.h>

def recipes(coffee,milk,sweetener,ice):
    sweetener_dict = {"sugar": 25, "artificial sweetener": 30, "no sweetener": 0}
    drink_dict = {"espresso" : 150, "latte": 100, "cappuccino": 100, "coffee": 75}
    milk_dict = {"half&half": 75, "2% milk": 85, "almond milk": 55, "no milk": 0}
    if ice == "cold": ice_val = 50
    else: ice_val = 0
    return drink_dict[coffee], milk_dict[milk], sweetener_dict[sweetener], ice_val

def main():
    run_num = 0
    while True:
        if run_num == 0:
            sweetener_tup = ("sugar", "artificial sweetener", "no sweetener")
            drink_tup = ("espresso", "latte", "cappuccino", "coffee")
            milk_tup = ("half&half", "2% milk", "almond milk", "no milk")
            current_coffee = 2000
            current_sugar = 1000
            current_asweetener = 500
            current_handh = 1000
            current_2milk = 1000
            current_amilk = 650
            current_ice = 1000
        i_o = input("Press 1 to review an ingredients report, 2 to end the program, or any other key to continue: \n")
        if i_o == '1':
            print("There is currently " + str(current_coffee) + " grams of coffee")
            print("There is currently " + str(current_2milk) + " ml of 2% milk")
            print("There is currently " + str(current_handh) + " ml of half&half")
            print("There is currently " + str(current_amilk) + " ml of almond milk")
            print("There is currently " + str(current_sugar) + " grams of sugar")
            print("There is currently " + str(current_asweetener) + " grams of artificial sweetener")
            print("There is currently " + str(current_ice) + " grams of ice")
            continue
        elif i_o == '2':
            break
        else:
            try:
                drink = int(input("What would you like to drink?\nEnter 1 for espresso, 2 for latte, 3 for cappuccino, or 4 for regular coffee:")) - 1
                if (drink < 0) | (drink > 3):
                    print("That's not an option.")
                    continue
            except ValueError as e:
                print("That's not an option.")
                continue
            except Exception as e:
                print(str(e))
                continue
            try:
                ice = int(input("Enter 1 for a hot drink or 2 for a cold drink:"))
                if (ice < 1) | (ice > 2):
                    print("That's not an option.")
                    continue
                else:
                    if ice == 1:
                        ice_str = "hot"
                    else:
                        ice_str = "cold"
            except ValueError as e:
                print("That's not an option.")
                continue
            except Exception as e:
                print(str(e))
                continue
            try:
                milk = int(input("What kind of milk would you like?\nEnter 1 for half&half, 2 for 2% milk, 3 for almond milk, or 4 for no milk:")) - 1
                if (milk < 0) | (milk > 3):
                    print("That's not an option.")
                    continue
            except ValueError as e:
                print("That's not an option.")
                continue
            except Exception as e:
                print(str(e))
                continue
            try:
                sweetener = int(input("How would you like your drink sweetened?\nEnter 1 for sugar, 2 for artificial sweetener, or 3 for unsweetened:")) - 1
                if (sweetener < 0) | (sweetener > 2):
                    print("That's not an option.")
                    continue
            except ValueError as e:
                print("That's not an option.")
                continue
            except Exception as e:
                print(str(e))
                continue

        print("\nYou have chosen a " + ice_str + " " + drink_tup[drink] + " with " +milk_tup[milk] + " and " + sweetener_tup[sweetener] + ".\n")

        if (drink_tup[drink] == "latte" or drink_tup[drink] == "cappuccino") and milk_tup[milk] == "no milk":
            print("\nIts hard to make a " + drink_tup[drink] + " without milk. I'd strongly reconsider my life decisions if I were you.\n")

        dgrounds, dmilk, dsweetener, dice = recipes(drink_tup[drink],milk_tup[milk],sweetener_tup[sweetener], ice_str)

        if milk_tup[milk] == "half&half":
            if current_handh - dmilk >= 0:
                current_handh -= dmilk
            else:
                print("Sorry, I dont have enough half&half to make that.\nTry entering another order.")
                continue
        elif milk_tup[milk] == "2% milk":
            if current_2milk - dmilk >= 0:
                current_2milk -= dmilk
            else:
                print("Sorry, I dont have enough 2% milk to make that.\nTry entering another order.")
                continue
        elif milk_tup[milk] == "almond milk":
            if current_amilk - dmilk >= 0:
                current_amilk -= dmilk
            else:
                print("Sorry, I dont have enough almond milk to make that.\nTry entering another order.")
                continue
        if sweetener_tup[sweetener] == "sugar":
            if current_sugar - dsweetener >= 0:
                current_sugar -= dsweetener
            else:
                print("Sorry, I dont have enough sugar to make that.\nTry entering another order.")
                continue
        elif sweetener_tup[sweetener] == "artificial sweetener":
            if current_asweetener - dsweetener >= 0:
                current_asweetener -= dsweetener
            else:
                print("Sorry, I dont have enough artificial sweetener to make that.\nTry entering another order.")
                continue
        if current_coffee - dgrounds >= 0: current_coffee -= dgrounds
        else:
            print("Sorry, I dont have enough coffee to make that.\nTry entering another order.")
            continue
        if current_ice - dice >=0: current_ice -= dice
        else:
            print("Sorry, I dont have enough ice to make that.\nTry entering another order.")
            continue
        print("\nHere is your " + ice_str + " " + drink_tup[drink] + " with " + milk_tup[milk] + " and " + sweetener_tup[sweetener] + "!\n\nHave a great day!\n")
        run_num += 1


if __name__ == '__main__':
    main()

