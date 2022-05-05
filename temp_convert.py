#!/usr/bin/env python3

# Created by: Sarah
# Created on: May 5th, 2022.
# This program asks the user to enter a temperature in celsius. It then
# converts the temperature from celsius to fahrenheit using a function.


def calculate_farenheit():
    # get user_cel from user
    user_cel_string = input("Enter the temperature (°C): ")
    print("")

    try:
        # convert string into a float.
        user_cel_float = float(user_cel_string)

        # calculates and displays what celsius is equal to in fahrenheit.
        farenheit_temp = (9.0/5.0) * user_cel_float + 32
        print("{:,.1f}°C is equal to {:,.1f}°F.".
              format(user_cel_float, farenheit_temp))

    # handles error case.
    except Exception:
        print("{} is not a valid celsius value.".format(user_cel_string))


def main():
    # calls function
    calculate_farenheit()


if __name__ == "__main__":
    main()
