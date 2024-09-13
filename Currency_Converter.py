rates = {
    'USD': 1.0,    # US Dollar
    'EUR': 0.93,   # Euro
    'GBP': 0.80,   # British Pound
    'ZAR': 19.00,  # South African Rand
    'JPY': 147.10, # Japanese Yen
    'CAD': 1.34,   # Canadian Dollar
    'AUD': 1.55    # Australian Dollar
}

print("Welcome to the Currency Converter!")
print("Available currencies are: USD, EUR, GBP, ZAR, JPY, CAD, AUD")

fromCurrency = input("Enter the currency you want to convert from: ").upper()
toCurrency = input("Enter the currency you want to convert to: ").upper()

if fromCurrency not in rates or toCurrency not in rates:
    print("Invalid currency entered.")
    
else:
    amount = float(input("Enter the amount:"))
    convertedAmount = amount * rates[toCurrency] / rates[fromCurrency]

    print(amount,"",fromCurrency,"equal to",convertedAmount,"",toCurrency)
