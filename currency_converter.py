# CURRENCY CONVERTER

#dictionary for available currencies with their exchange rates with respect to INR

exchange_rates = {
    "INR": 1.0,
    "USD": 95.82,
    "GBP": 126.86,
    "CHF": 115.91,
    "EUR": 109.14,
    "SGD": 75.00,
    "CAD": 67.88,
    "AUD": 67.42,
    "NZD": 54.29,
    "AED": 26.09,
    "SAR": 25.55,
    "MYR": 23.52,
    "BRL": 17.65,
    "CNY": 14.27,
    "HKD": 12.22,
    "MXN": 5.51,
    "ZAR": 5.48,
    "THB": 2.87,
    "RUB": 1.13,
    "JPY": 0.61,
    "KRW": 0.07
}

#names of available currencies with their codes

currency_names = {
    "INR": "Indian Rupee",
    "USD": "United States Dollar",
    "GBP": "British Pound Sterling",
    "CHF": "Swiss Franc",
    "EUR": "Euro",
    "SGD": "Singapore Dollar",
    "CAD": "Canadian Dollar",
    "AUD": "Australian Dollar",
    "NZD": "New Zealand Dollar",
    "AED": "United Arab Emirates Dirham",
    "SAR": "Saudi Riyal",
    "MYR": "Malaysian Ringgit",
    "BRL": "Brazilian Real",
    "CNY": "Chinese Yuan",
    "HKD": "Hong Kong Dollar",
    "MXN": "Mexican Peso",
    "ZAR": "South African Rand",
    "THB": "Thai Baht",
    "RUB": "Russian Ruble",
    "JPY": "Japanese Yen",
    "KRW": "South Korean Won"
}


# Process to convert the currency
print("========================================")
print("          CURRENCY CONVERTER")
print("========================================")


# Get input from user
print("\n========================================")

from_currency = input("Enter the currency you have (eg: EUR/USD/INR etc): ").upper()

to_currency = input("Enter the currency you want (eg: EUR/USD/INR etc): ").upper()

amount = float(input("Enter the amount: "))


# Check whether currencies are supported
if from_currency not in exchange_rates:
    print("\nInvalid currency code.")

elif to_currency not in exchange_rates:
    print("\nInvalid currency code.")

elif amount <= 0:
    print("\nAmount must be greater than zero.")

elif from_currency in exchange_rates and to_currency in exchange_rates:
    print("\nBoth currencies are supported.")

    # Currency conversion
    from_rate = exchange_rates[from_currency]
    to_rate = exchange_rates[to_currency]

    converted_amount = amount * from_rate / to_rate

    # Display result
    print("\n========== CONVERSION DETAILS ==========")

    print("Conversion from:",currency_names[from_currency],"(" + from_currency + ")")

    print(
        "Conversion to:",
        currency_names[to_currency],
        "(" + to_currency + ")"
    )

    print(
        "Amount entered:",
        f"{amount:.2f}",
        from_currency
    )

    print(
        "Converted amount:",
        f"{converted_amount:.2f}",
        to_currency
    )

    print("\nConversion Summary:")

    print(
        f"{amount:.2f} {currency_names[from_currency]} "
        f"is equivalent to {converted_amount:.2f} "
        f"{currency_names[to_currency]}."
    )

    print("========================================")