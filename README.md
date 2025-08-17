WEEK 3 PYTHON ASSIGNMENT
Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

INTERPRETATION OF THE ASSIGNMENT 

The task requires creating a Python function called calculate_discount that determines the final price of an item after applying a discount, with specific conditions. Here's the detailed interpretation:
Function Requirements:

    Function Name: calculate_discount

    Parameters:

        price: The original price of the item (numeric value)

        discount_percent: The discount percentage to be applied (numeric value)

    Logic:

        If the discount percentage is 20% or higher, apply the discount to the original price

        If the discount percentage is less than 20%, return the original price without any discount

    Return Value: The final price after applying the discount (if applicable)

User Interaction Requirements:

    Prompt the user to enter:

        The original price of an item

        The discount percentage

    Use the calculate_discount function to compute the final price

    Print:

        The discounted price if a discount was applied

        The original price if no discount was applied

Example Flow:

    User enters: price = 100, discount_percent = 25

        Function applies 25% discount (since ≥20%)

        Final price = 75

        Output: 75

    User enters: price = 100, discount_percent = 15

        No discount applied (since <20%)

        Output: 100

Implementation Considerations:

    Need to handle numeric input from user

    Should validate that inputs are valid numbers

    Discount calculation formula: final_price = price × (1 - discount_percent/100)

    The function should only apply the discount when discount_percent ≥ 20

This interpretation leads to a straightforward Python implementation that meets all the specified requirements.
Write for me a README.md for the above interpretation above
Discount Calculator
Overview

This Python script provides a function to calculate the final price of an item after applying a discount, with specific conditions. The discount is only applied if it meets or exceeds 20%.
Features

    Calculates discounted prices based on user input

    Applies discount only when the discount percentage is 20% or higher

    Simple command-line interface for user interaction

Functionality

The main function calculate_discount(price, discount_percent) performs the following logic:

    Takes the original price and discount percentage as parameters

    If discount is 20% or higher:

        Applies the discount to the original price

        Returns the discounted price

    If discount is less than 20%:

        Returns the original price without modification

Usage

    Run the script in a Python environment

    When prompted:

        Enter the original price of the item

        Enter the discount percentage

    The program will display either:

        The final price after discount (if discount ≥ 20%)

        The original price (if discount < 20%)

Example
bash

Enter the original price: 100
Enter the discount percentage: 25
The final price after discount is: 75.0



