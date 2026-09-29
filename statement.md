# Project Statement

## Project Title

**Currency Converter**

## Problem Statement

Converting an amount from one currency to another can require users to manually find an exchange rate and perform the required calculation. This can be inconvenient and can lead to calculation errors.

The Currency Converter project provides a simple command-line solution for converting amounts between multiple supported currencies. The program stores predefined exchange rates relative to the Indian Rupee (INR), accepts the user's source currency, target currency, and amount, and calculates the equivalent value in the selected currency.

The project is designed to demonstrate basic programming concepts such as dictionaries, user input, conditional statements, arithmetic operations, validation, and formatted output.

## Scope of the Project

The project is limited to currency conversion using a predefined set of exchange rates.

The current scope includes:

* Supporting 21 currencies.
* Accepting currency codes as user input.
* Accepting a numerical amount for conversion.
* Validating the entered currency codes.
* Validating that the amount is greater than zero.
* Calculating the converted amount using predefined exchange rates.
* Displaying the conversion details and final result.
* Running the application through a command-line interface.

The project does not currently include live exchange-rate retrieval, online services, databases, user accounts, payment processing, or persistent conversion history.

## Target Users

The application is intended for:

* Students learning basic programming and Python.
* Users who need a simple currency conversion calculation.
* Beginners who want to understand how currency conversion can be implemented using basic programming concepts.
* Users who prefer a lightweight command-line application.

## High-Level Features

### 1. Currency Selection

The user enters the currency code they currently have and the currency code they want to convert to.

### 2. Amount Input

The user enters the amount that needs to be converted.

### 3. Currency Validation

The program checks whether both entered currencies are included in the list of supported currencies.

### 4. Amount Validation

The program checks that the entered amount is greater than zero.

### 5. Currency Conversion

The program calculates the converted amount using predefined exchange rates relative to INR.

### 6. Conversion Details

The program displays:

* Source currency name and code.
* Target currency name and code.
* Original amount.
* Converted amount.
* A complete conversion summary.

### 7. Command-Line Execution

The application can be executed directly from a terminal using Python and does not require a graphical interface.

## Technologies Used

* Python
* Python dictionaries
* Command-line interface
* Git and GitHub

## Limitations

The application uses fixed exchange rates stored in the source code. Therefore, the results do not automatically reflect current market exchange rates.

The current version also does not store conversion history or retrieve data from an external service.

## Future Scope

The project can be expanded by integrating a live exchange-rate API, adding more currencies, introducing a graphical interface, supporting multiple conversions in a single session, and adding conversion history.
