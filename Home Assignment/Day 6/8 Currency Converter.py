# 8.	Currency Converter
# Function convert_to_usd(inr, rate=83.2) → converts INR to USD (default rate 83.2)

def currency(inr, rate=83.2):
    return inr/rate
print(currency(2500))