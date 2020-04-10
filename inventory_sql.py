import sqlite3

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

string1 = "***** VIEW INVENTORY & MODIFY MENU *****".center(160, ' ')

print('\n')
prYellow(string1)

# id, ingredient, qty
string1 = "***** VIEW INVENTORY & MODIFY MENU *****".center(160, ' ')
print('\n')
prYellow(string1)
# id, ingredient, qty

def inventory():
        connection = sqlite3.connect("Order_Placed.db")
        crsr = connection.cursor()
        while True:
            print('\n\n')
            prCyan("------------------------------------------------------------------------")
            prCyan("|  ID |        INGREDIENT        | QUANTITY | COST PRICE | SELL PRICE  |")
            prCyan("------------------------------------------------------------------------")
            cursor = connection.execute("SELECT * from inventory")
            for row in cursor:
                print(" |", row[0], " "*(3 - len(str(row[0]))),
                "|", row[1], " "*(23 - len(row[1])),
                "|", row[2], " "*(7 - len(str(row[2]))),
                "|", row[3], " "*(9 - len(str(row[3]))),
                "|", row[4], " "*(9 - len(str(row[4]))),"|")
            prCyan("------------------------------------------------------------------------")
            print('\n')
            prCyan("\nWould you like to modify the menu  \n\nEnter 'YES' or 'NO':   ")
            print()
            menu_input = input()
            if menu_input.lower() == "yes" :
                prCyan("\nPlease enter the ingredient you would like to add: ")
                print()
                new_ingredient = input()
                print('\n\n')
                if new_ingredient.isdigit() or new_ingredient == "":
                    prRed("\nInvalid Input")
                prCyan("\nPlease enter the new cost price of the ingredient: ")
                print()
                new_cp = input()
                print('\n\n')
                if new_cp.isalpha() or new_cp == "":
                    prRed("\nInvalid Input")
                prCyan("\nPlease enter the new selling price of the ingredient: ")
                print()
                new_sp = input()
                print('\n\n')
                if new_sp.isalpha() or new_sp == "":
                    prRed("\nInvalid Input")
                prCyan("\nPlease enter the name of the ingredient you would like to replace: ")
                print()
                old_ingredient = input()
                print('\n\n')
                if old_ingredient.isdigit() or old_ingredient == "":
                    prRed("\nInvalid Input")
                crsr.execute("UPDATE inventory SET ingredient = ?, qty = 100, cost_price = ?, sell_price = ? WHERE  ingredient = ?",(new_ingredient,float(new_cp),float(new_sp),old_ingredient))
            elif menu_input.lower() == "no":
                prPurple("\n\nHave a good day. \nThank you.")
                break
            else:
                prRed("\nInvalid Input")
        connection.commit()
        connection.close()
inventory()
