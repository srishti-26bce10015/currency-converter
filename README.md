# Currency Converter

## Overview

Currency Converter is a Python-based command-line application that converts an amount from one supported currency to another using predefined exchange rates with respect to INR.

The user enters the currency they have, the currency they want, and the amount to be converted. The program validates the input and displays the converted amount.

## Features

* Supports 21 currencies.
* Accepts uppercase and lowercase currency codes.
* Validates supported currency codes.
* Checks that the entered amount is greater than zero.
* Displays currency names, codes, original amount, and converted amount.
* Runs directly through the command line.

## Technologies Used

* Python
* Python dictionaries
* Command-line interface
* Git and GitHub

No external Python libraries are required.

## Installation and Setup

1. Install Python 3 on your system.
2. Clone this repository
3. Open the project folder


## How to Run

Run the following command in the terminal:

python currency_converter.py

If your system uses `python3`:

python3 currency_converter.py

The program will ask for:

* The currency you have
* The currency you want
* The amount to convert

## Testing

The program can be tested using:

* Valid currency codes such as USD, EUR, INR, etc.
* Lowercase currency codes such as `usd` and `eur`.
* Unsupported currency codes.
* Zero or negative amounts.
* Conversions between different supported currencies.

Example:

Enter the currency you have: USD
Enter the currency you want: INR
Enter the amount: 100

The program should display the corresponding converted amount based on the predefined exchange rates.

## Project Structure

currency-converter/
├── README.md
├── statement.md
└── currency_converter.py

## Note

The exchange rates used in this project are predefined in the program and are not retrieved from a live exchange-rate API.

## Future Improvements

* Add live exchange rates using an API.
* Add more currencies.
* Add repeated conversions in one session.
* Improve input error handling.
* Add a graphical user interface.
* Add conversion history.
