
import sqlite3

connection = sqlite3.connect("myTable.db")

crsr = connection.cursor()

# id, ingredient, qty

sql_command = """CREATE TABLE inventory (
menu_id INTEGER PRIMARY KEY NOT NULL,
ingredient VARCHAR(20) NOT NULL,
qty INTEGER(3) NOT NULL,
cost_price integer(4) NOT NULL,
sell_price integer(4) not null);"""


#crsr.execute(sql_command)

sql_command = """Insert into inventory
values(1, "CRUST -> Thin", 100, 60 , 69),
(2, "CRUST -> Regular", 100, 50 , 57.5),
(3, "CRUST -> Cheesy", 100, 70 , 80.5),

(4, "CHEESE -> Fat Free", 100, 50, 57.5),
(5, "CHEESE -> Vegan", 100, 40, 46),
(6, "CHEESE -> Extra", 100, 30, 34.5),
(7, "CHEESE -> Regular", 100, 20, 23),

(8, "TOPPING -> Onion", 100, 10 , 11.5 ),
(9, "TOPPING -> Olives", 100, 10 , 11.5 ),
(10, "TOPPING -> Jalapeno", 100, 15 , 17.25 ),
(11, "TOPPING -> Red Paprika", 100, 15 , 17.25 ),
(12, "TOPPING -> Tomato", 100, 5 , 5.75 ),
(13, "TOPPING -> Corn", 100, 5 , 5.75 ),
(14, "TOPPING -> Capsicum", 100, 5 , 5.75 ),
(15, "TOPPING -> Mushroom", 100, 10 , 11.5 );"""


crsr.execute(sql_command)

cursor = connection.execute("SELECT * from inventory")
for row in cursor:
    print("\n")
    print("ID = ", row[0])
    print("INGREDIENT = ", row[1])
    print("QUANTITY = ", row[2])
    print("COST PRICE = ", row[3])
    print("SELL PRICE = ", row[4], "\n")
