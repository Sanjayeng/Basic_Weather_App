import requests  # Import the requests library to talk to APIs

# ------ CONFIGURATION ------
API_KEY = 'f28f5146bb82f51af7078e306c991d42'  # Paste your OpenWeatherMap API key here

def get_weather(city_name):
    # API endpoint URL with city and API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(url)               # Make the HTTP request
    if response.status_code == 200:            # If the request was successful
        data = response.json()                 # Get data in JSON format

        # Extract what you want
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather_description = data["weather"][0]["description"]

        # Show results
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {weather_description.capitalize()}")

    else:
        print("Error details:", response.text)

def main():
    print("Simple Weather App")
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
