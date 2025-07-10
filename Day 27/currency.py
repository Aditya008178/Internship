# currency Converter
# API: https://api.exchangerate-api.com/v4/latest/USD
# Goal: Convert a given amount in INR to USD, EUR, etc.

import requests

API = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
data = API.json()

RS = float(input("Enter amount in Indian Rupees: "))
USD_to_INR = data["rates"]["INR"]

USD_amount = RS/USD_to_INR
print(f"{RS} RS = {USD_amount} USD")

print("Other conversions:")
for currency, rate in data["rates"].items():
      amount = RS/USD_to_INR * rate
      print(f"{RS} RS = {amount} {currency}")
