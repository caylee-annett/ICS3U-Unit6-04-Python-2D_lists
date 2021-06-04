#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: June 2021
# This program calculates the average of a 2D list

import random


def calculate_average(list_of_numbers):
    # This function calculates the average

    sum_of_numbers = 0

    for row_numbers in list_of_numbers:
        for column_numbers in row_numbers:
            sum_of_numbers = sum_of_numbers + column_numbers
    average = sum_of_numbers / (len(list_of_numbers) * len(row_numbers))

    return average


def main():
    # This function gets column and row numbers and
    #   generates the random numbers

    number_list = []

    # Input
    print("This program calculates the average of a 2D list.")
    print("")
    rows_string = input("How many rows would you like: ")
    columns_string = input("How many columns would you like: ")

    # Process
    while True:
        try:
            rows_integer = int(rows_string)

            if rows_integer > 0:
                break
            else:
                rows_string = input("Must be a positive integer. "
                                    "Enter the number of rows: ")
        except Exception:
            rows_string = input("{} is not a valid input. Enter the number "
                                "of rows: ".format(rows_string))
    while True:
        try:
            columns_integer = int(columns_string)

            if columns_integer > 0:
                print("")
                break
            else:
                columns_string = input("Must be a positive integer. Enter "
                                       "the number of columns: ")
        except Exception:
            columns_string = input("{} is not a valid input. Enter the number "
                                   "of columns: ".format(columns_string))
    for loop_counter_rows in range(0, rows_integer):
        temp_column = []
        for loop_counter_columns in range(0, columns_integer):
            random_number = random.randint(1, 50)
            temp_column.append(random_number)
            print("{} ".format(random_number), end="")
        number_list.append(temp_column)
        print("")

    # Call functions
    answer = calculate_average(number_list)

    # Output
    print("")
    print("The average is: {}".format(answer))
    print("\nDone.")


if __name__ == "__main__":
    main()
