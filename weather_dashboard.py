import requests
import json

# Replace with your own API key
API_KEY = 'cfda4a9cf8411b41a925a0c34b034414'
CITY = 'Mumbai'
URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

response = requests.get(URL)
data = response.json()

# Print data for debugging
print(json.dumps(data, indent=2))



main_data = data['main']
weather_data = {
    'Temperature': main_data['temp'],
    'Feels Like': main_data['feels_like'],
    'Min Temp': main_data['temp_min'],
    'Max Temp': main_data['temp_max'],
    'Humidity': main_data['humidity']
}

# Visualisatiin Dashboard
import matplotlib.pyplot as plt
import seaborn as sns

# Convert data to lists
labels = list(weather_data.keys())
values = list(weather_data.values())

# Bar chart using seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x=labels, y=values, palette="Blues_d")
plt.title(f'Weather Report for {CITY}')
plt.ylabel('Value')
plt.show()
