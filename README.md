# Pizza Retail Management System

A terminal-based pizza retail management system that allows a company to place orders, modify menus and keep a tab on their inventory.


## Table of Contents
- [Purpose](#purpose)
- [Technologies and Libraries Used](#technologies-and-libraries-used)
- [Setup](#setup)
- [Repository Information](#repository-information)
- [Functions](#functions)
- [Usage](#usage)
- [Output](#output)


## Purpose
This project was created as the final project for the Computer Science course in my junior year of high school. The purpose was to showcase an application of the knowledge gained in the course. Thus, it was created using the knowledge of Python and Databases (SQLite) and implementing Python-SQL integration. The project was created to be used by any pizza company to manage their orders, inventory, and menu.

## Technologies and Libraries Used
- Programming Language
  - Python
- Database
  - SQLite
- Libraries
  - sqlite3 
  - datetime


## Setup
Make sure to git clone this repository. After cloning, make sure the latest version of Python and all mentioned packages are installed and the project is ready for use!


## Repository Information
This repository consists of multiple Python files:
- Intialize.py is to initialize the values for the ordering system. 
- main_menu.py is the main file on which the project runs and is used for placing an order for the customers as well as modifying the menu and managing inventory.
- inventory_sql.py is to view the inventory for the company separately without opening the main menu file


This pizza retail system for companies is terminal-based. The programming language used is Python and SQLlite for the database. Even after the Python files are closed, the database will persist in a specific machine as it is saved in the SQL Database


## Functions
The retail system has two functions:

- To place an order:
  - This function is for the company staff to take an order from a customer. It consists of options for customer name, customer address, the number of pizzas, the type of crust, the size of the pizza, the type of cheese, the type of toppings, etc.
- To view inventory and modify the menu:
  - This function is used by the company to view its inventory or to modify its menu. This function can be used to view the ingredients that the restaurant is going to run out of since the inventory is automatically updated after every order is placed. It can also be used to add new inventory with specifications for cost price, sell price, etc.


## Usage
- To run the program, run the main_menu.py file. 
- The program will then ask the user to choose between two options: place an order or view inventory and modify the menu. The user can choose the option by entering the number corresponding to the option. 
- The user can then follow the instructions on the screen to place an order or view inventory and modify the menu. 


## Output
<details>
<summary>Click to expand</summary>
<br>
<kbd><img src="readme_images/pic1.png" width="700"></kbd>
<br>
<kbd><img src="readme_images/pic2.png"></kbd>
<br>
<kbd><img src="readme_images/pic3.png"></kbd>
<br>
<kbd><img src="readme_images/pic4.png"></kbd>
<br>
<kbd><img src="readme_images/pic5.png"></kbd>
<br>
<kbd><img src="readme_images/pic6.png"></kbd>
<br>
<kbd><img src="readme_images/pic7.png"></kbd>
<br>
<kbd><img src="readme_images/pic8.png"></kbd>
<br>
<kbd><img src="readme_images/pic9.png" width="800"></kbd>
<br>
<kbd><img src="readme_images/pic10.png"></kbd>
<br>
<kbd><img src="readme_images/pic11.png"></kbd>
<br>
<kbd><img src="readme_images/pic12.png"></kbd>

</details>
