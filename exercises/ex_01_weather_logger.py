import httpx

# Exercise 1. GET Stockholms nuvarande väder(temp)
def get_stockholm_weather():
    """Get Stockholms current weather."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 59.33,      # Stockholms latitud
        "longitude": 18.07,     # Stockholms longitude
        "current_weather": True
    }

    with httpx.Client(timeout=10.0) as client:
        response = client.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
if __name__ == "__main__":
    weather = get_stockholm_weather()
    print(f"Stockholm right now: {weather['current_weather']['temperature']}°C")