import requests

city = input('Input the city name: ')

# Display the message
print('Displaying Weather report for: ' + city)

# Fetch the weather details for today only
url = 'https://wttr.in/{}?1'.format(city)
res = requests.get(url)

# Check if the request was successful
if res.status_code == 200:
    print(res.text)
else:
    print('Failed to fetch weather information. Please check the city name and try again.')
