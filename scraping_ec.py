import re
import requests

def scrape_prices(url, pattern):
    response = requests.get(url)
    content = response.text
    prices = re.findall(pattern, content)
    return prices

def convert_to_float(price):
    try:
        return float(price)
    except ValueError:
        return None

# Recopilar precios de KFC
kfc_url = "https://www.kfc.com.ec/menu/combos-8D1AC979-D94D-E611-80CF-0050568602D0.html"
kfc_pattern = r"\$\d+(?:\.\d+)?"
kfc_prices = scrape_prices(kfc_url, kfc_pattern)
kfc_prices = [convert_to_float(price[1:]) for price in kfc_prices if price]

print("Precios recopilados de KFC:")
for price in kfc_prices:
    print(price)

# Recopilar precios de Campero
campero_url = "https://campero.ec/menu/promociones-a8aebdee-f014-4542-84c0-8050f47f9e29.html"
campero_pattern = r"\$\d+(?:\.\d+)?"
campero_prices = scrape_prices(campero_url, campero_pattern)
campero_prices = [convert_to_float(price[1:]) for price in campero_prices if price and convert_to_float(price[1:]) > 0]

print("\nPrecios recopilados de Campero:")
for price in campero_prices:
    print(price)

# Comparar precios y variedad
def compare_prices(prices1, prices2):
    unique_prices1 = set(prices1)
    unique_prices2 = set(prices2)
    
    print("\nComparación de precios:")
    print("-" * 50)
    print("KFC:")
    print(f"Cantidad de precios únicos: {len(unique_prices1)}")
    print(f"Precios únicos: {unique_prices1}")
    print(f"Precio más económico: ${min(prices1)}")
    print(f"Precio más caro: ${max(prices1)}")
    print("-" * 50)
    print("Campero:")
    print(f"Cantidad de precios únicos: {len(unique_prices2)}")
    print(f"Precios únicos: {unique_prices2}")
    print(f"Precio más económico: ${min(prices2)}")
    print(f"Precio más caro: ${max(prices2)}")
    print("-" * 50)
    
    if len(unique_prices1) > len(unique_prices2):
        print("KFC tiene más variedad de precios.")
    elif len(unique_prices2) > len(unique_prices1):
        print("Campero tiene más variedad de precios.")
    else:
        print("Ambos tienen la misma variedad de precios.")

    avg_price1 = sum(prices1) / len(prices1) if prices1 else 0
    avg_price2 = sum(prices2) / len(prices2) if prices2 else 0

    if avg_price1 < avg_price2:
        print("KFC es más económico en promedio.")
    elif avg_price2 < avg_price1:
        print("Campero es más económico en promedio.")
    else:
        print("Ambos tienen el mismo precio promedio.")

compare_prices(kfc_prices, campero_prices)
