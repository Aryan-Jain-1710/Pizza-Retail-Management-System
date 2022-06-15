# Pizza Retail System

## Introduction

This is a pizza retail system which is retail-based and allows a company to place orders, modify menu and keep a tab on their inventory.
This project was built in collboartion with Siddhartha Jaiswal and Manav Jain.


## Repository Information

This repository consists of multiple python files:
- Intialize.py is to intialize the values for the ordering system. 
- main_menu.py is the main file on which the project runs and is used for placing an order for the customers as well as modifying the menu and managing inventory.
- inventory_sql.py is to view the inventory for the company seperately without opening the main menu file


This pizza retail system for companies is terminal-based. The programming language used is Python and SQLlite for database. Even after the python files are closed, the database will persist in a specific machine as it is saved in the SQL Database


## Methods

The retail system has two functions:

- To place an order:
  - This function is for the company staff to take an order from a customer. It consists of options for customer name, customer address, the number of pizzas, the type of crust, the size of the pizza, type of cheese, type of toppings, etc.
- To view inventory and modify menu:
  - This function is used by the company to view their inventory or to modify their menu. This function can be used to view the ingreidents that the restaurant is going to run out of since the inventory is automatically updated after every order is placed. It can also be used to add new inventory with specifications for cost price, sell price, etc.
