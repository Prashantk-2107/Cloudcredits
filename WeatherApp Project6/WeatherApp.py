import requests

def get_weather(api_key,city):
    try:
        url= f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response=requests.get(url)
        data=response.json()
        
        if response.status_code==200:
            weather_info={
                "City":data['name'],
                "Temperature":data['main']['temp'],
                "Weather":data['weather'][0]['description'],
                "Humidity":data['main']['humidity'],
                "Wind Speed":data['wind']['speed']
            }
            return weather_info
        else:
            print("Error: ",data.get("message","Failed to retrieve data"))
            return None
        
    except Exception as e:
        #Tell all errors
        print("Error: ",e)
        return None
    
# Example usage
if __name__=="__main__":
    api_key="007b22227331ca0a44c6659b5911c584"
    
    while True:
        city=input("\nEnter city name (or 'exit' to quit): ").lower()
        
        if city=='exit':
            break
        weather=get_weather(api_key,city)
        
        if weather:
            print(f"\nCity: {weather['City']}")
            print(f"Temperature: {weather['Temperature']}°C")
            print(f"Weather: {weather['Weather']}")
            print(f"Humidity: {weather['Humidity']}%")
            print(f"Wind Speed: {weather['Wind Speed']} m/s")
            
    