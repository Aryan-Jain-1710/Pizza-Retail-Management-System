import sqlite3

connection = sqlite3.connect("Order_Placed.db")

crsr = connection.cursor()


# Creating Inventory and Menu Table
sql_command = """CREATE TABLE inventory (
menu_id INTEGER NOT NULL,
ingredient VARCHAR(20) NOT NULL,
qty INTEGER(3) NOT NULL,
cost_price integer(4) NOT NULL,
sell_price integer(4) not null);"""

crsr.execute(sql_command)

# Inserting default values into Inventory table
sql_command = """INSERT INTO inventory
VALUES
(1, '10" - Thin', 100, 60 , 69),
(2, '10" - Regular', 100, 50 , 57.5),
(3, '10" - Cheezy', 100, 70 , 80.5),


(4, '12" - Thin', 100, 70 , 69),
(5, '12" - Regular', 100, 60 , 57.5),
(6, '12" - Cheezy', 100, 80 , 80.5),

(7, '14" - Thin', 100, 80 , 69),
(8, '14" - Regular', 100, 70 , 57.5),
(9, '14" - Cheezy', 100, 90 , 80.5),

(10, "Cheese -> Fat - Free" , 100, 50, 57.5),
(11, "Cheese -> Vegan", 100, 40, 46),
(12, "Cheese -> Extra", 100, 30, 34.5),
(13, "Cheese -> Regular", 100, 20, 23),

(14, "Onion", 100, 10 , 11.5 ),
(15, "Olives", 100, 10 , 11.5 ),
(16, "Jalapeno", 100, 15 , 17.25 ),
(17, "Red Paprika", 100, 15 , 17.25 ),
(18, "Tomato", 100, 5 , 5.75 ),
(19, "Corn", 100, 5 , 5.75 ),
(20, "Capsicum", 100, 5 , 5.75 ),
(21, "Mushroom", 100, 10 , 11.5 );"""

crsr.execute(sql_command)

# Creating Pizza Order Table
sql_command = """CREATE TABLE pizza (
customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(20) NOT NULL,
address VARCHAR(100) NOT NULL,
pizza_size INTEGER(2) NOT NULL,
crust CHAR(7) NOT NULL,
topping_1 CHAR(11),
topping_2 CHAR(11),
topping_3 CHAR(11),
cheese CHAR(10) NOT NULL,
quantity INTEGER(2) NOT NULL,
order_date DATE NOT NULL);"""

crsr.execute(sql_command)


connection.commit()

connection.close()
