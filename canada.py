import requests
from bs4 import BeautifulSoup


def get_weather_data(city):
    try:
        search_url = f"https://www.google.com/search?q=weather+{city}+canada"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(search_url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            temperature = soup.find('div', class_='BNeawe').text
            condition = soup.find('div', class_='BNeawe tAd8D AP7Wnd').text
            return {
                'city': city,
                'temperature': temperature,
                'condition': condition
            }
        else:
            print(f"Error: Unable to fetch data for {city}")
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

# List of cities
cities = ['Ottawa', 'Toronto', 'Montreal']

# Get weather data for each city
for city in cities:
    weather_data = get_weather_data(city)
    if weather_data:
        print(f"Weather in {weather_data['city']}:")
        print(f"Temperature: {weather_data['temperature']}")
        print(f"Condition: {weather_data['condition']}")
        print("----------------------------")
        print("hello")