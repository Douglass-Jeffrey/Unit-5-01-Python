#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program turns celsius to fahrenheit


def temperature():

    # This function turns celsius to fahrenheit
    try:
        # input
        celsius = int(input("Input a celsuis temperature of your choice: "))

        # process
        fahrenheit = (celsius * 1.8) + 32

        # output
        print("The celsuis temperature " + str(celsius) + "° is "
              + str(fahrenheit) + "° in Fahrenheit")
    except Exception:
        print("Please input only valid integer numbers")


def main():
    temperature()


if __name__ == "__main__":
    main()
