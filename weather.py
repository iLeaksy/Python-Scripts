import requests

# Replace YOUR_API_KEY with your actual API key
api_key = "01989ea21d984720b38170005221612"

# Specify the API endpoint and pass in the API key as a header
api_endpoint = "https://api.openweathermap.org/data/2.5/weather?q=Kumanovo,MK&units=metric&appid=" + api_key
response = requests.get(api_endpoint, headers={"x-api-key": api_key})

# Parse the response as a JSON object
data = response.json()

# Extract the data you need from the JSON object
current_time = data["dt"]
weather = data["weather"][0]["main"]
temperature = data["main"]["temp"]

# Display the data on the console
print("Current time:", current_time)
print("Weather:", weather)
print("Temperature:", temperature)