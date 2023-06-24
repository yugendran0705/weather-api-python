import requests #importing requests module

def get_weather_forecast(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&limit=5&appid={api_key}"  # Get the 5-day weather forecast for the city
    
    try:
        response = requests.get(url)  # Send a GET request to the API endpoint
        data = response.json()  # Convert the response data to a JSON object

        print(f"Weather forecast for {city}:") # Get the city name

        forecasts = data["list"][:5]  # Get the first 5 forecasts (3-hour intervals for 5 days)
        for forecast in forecasts:
            timestamp = forecast["dt_txt"]
            weather_description = forecast["weather"][0]["description"]
            temperature = forecast["main"]["temp"]
            humidity = forecast["main"]["humidity"]
            wind = forecast["wind"]
            wind_speed = wind["speed"]
            wind_direction = wind["deg"]

            print("Timestamp:", timestamp)
            print("Description:", weather_description)
            print("Temperature:", temperature, "K")
            print("Humidity:", humidity, "%")
            print("Wind Speed:", wind_speed, "m/s")
            print("Wind Direction:", wind_direction, "degrees")
            print("")

    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching weather data:", e)

if __name__ == "__main__":
    api_key = "f9b86dc15e0482daf3e1e81cd9f74efd"
    city = input("Enter a city name: ")
    get_weather_forecast(api_key, city)