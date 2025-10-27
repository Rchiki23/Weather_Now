import requests
API_KEY = "b9b3ee80d95e6e8b1aad6b56f854f2fb"
city = input("Enter City Name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    print(f"\n City: {data['name']}")
    print(f" Temp: {data['main']['temp']}C")
    print(f" Humidity: {data['main']['humidity']}%")
    print(f" Weather : {data['weather'][0]["description"].capitalize()}")
else:
    print("\n City not found pr invalid API key!")