# Import modules
import requests

# Define constants
api_endpoint = "https://api.apilayer.com/fixer/convert"
api_key = "qWTAuolq2NRFvmWiVgktw8zV3v24q0IV"

# Take input from user
from_currency = input("Enter the currency you want to convert from: ").upper()
to_currency = input("Enter the currency you want to convert to: ").upper()
amount = float(input("Enter the amount you want to convert: "))

# Make API Request
payload = {
    "from": from_currency,
    "to": to_currency,
    "amount": amount
}
headers = {
    "apikey": api_key
}
response = requests.get(api_endpoint, headers=headers, params=payload)
result = response.json()

# Print raw response
print("\n\n-------------------\n\n")
print("Raw Response:")
print(result)
print("\n\n-------------------\n\n")

# Print proper response
converted_value = result["result"]
date = result["date"]
rate = result["info"]["rate"]

print("{} {} = {} {} as on {} (rate: {})".format(
    amount, from_currency, converted_value, to_currency, date, rate))
