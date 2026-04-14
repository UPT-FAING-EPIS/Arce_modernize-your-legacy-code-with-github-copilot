import httpx

def get_exchange_rate(currency_code):
    """
    Fetches the current exchange rate for a given currency code against USD.
    """
    try:
        response = httpx.get(f"https://open.er-api.com/v6/latest/USD")
        response.raise_for_status()
        data = response.json()
        rates = data.get("rates", {})
        if currency_code in rates:
            return rates[currency_code]
        else:
            return None
    except httpx.RequestError as e:
        print(f"Error fetching exchange rate: {e}")
        return None

def convert_currency(amount, currency_code):
    rate = get_exchange_rate(currency_code)
    if rate:
        return amount * rate
    return None

if __name__ == "__main__":
    usd_amount = 100
    target_currency = "EUR"
    converted_amount = convert_currency(usd_amount, target_currency)
    if converted_amount:
        print(f"{usd_amount} USD is approximately {converted_amount:.2f} {target_currency}")
    else:
        print("Conversion failed.")