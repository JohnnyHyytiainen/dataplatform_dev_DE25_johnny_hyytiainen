import httpx

# EXERCISE 2: Get Stockholm weather för nästa 2, 3, 5... ...  dagar
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 59.33,
    "longitude": 18.07,
    "daily": "temperature_2m_max,temperature_2m_min",  # Max/min temp
    "forecast_days": 5,
    "timezone": "Europe/Stockholm"  # Svensk tid
}

with httpx.Client(timeout=10.0) as client:
    response = client.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    print("5-dagars forecast:")
    for i, date in enumerate(data['daily']['time']):
        max_temp = data['daily']['temperature_2m_max'][i]
        min_temp = data['daily']['temperature_2m_min'][i]
        print(f"{date}: {max_temp}C som varmast, {min_temp}C som kallast")
