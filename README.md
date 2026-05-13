Banking System: Inheritance Project
Overview
This is a Python project created for my computer science coursework to demonstrate Object-Oriented Programming (OOP) concepts. The goal was to build a base banking system and then create a specialized savings account with specific rules.

Features
Parent Class (Account): Handles the basic attributes like the account owner and the balance.

Child Class (SavingsAccount): Inherits from the Account class.

Custom Attributes: Added a $100 withdrawal limit specifically for savings accounts.

Method Overriding: Overrode the default withdraw behavior to enforce the $100 limit rule.

Requirements
Add an attribute called withdraw_limit of $100 to the savings amount.

Override the withdrawal behavior so that the withdrawal amount cannot be more than the withdrawal limit.

How it Works
When a user tries to withdraw money from a SavingsAccount, the code first checks if the amount is less than or equal to $100. If it is, the transaction proceeds; otherwise, an error message is displayed.
