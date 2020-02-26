import tkinter as tk 
from tkinter import font
import requests # To make API requests 
# Remember to pip install requests and Pillow modules for program to work!


# Formats the JSON data before displaying final output
def format_response(weather_forecast):
    try:
        name = weather_forecast['name']
        description = weather_forecast['weather'][0]['description']
        temperature = weather_forecast['main']['temp']
        humidity = weather_forecast['main']['humidity']
        pressure = weather_forecast['main']['pressure']
        temp_min = weather_forecast['main']['temp_min']
        temp_max = weather_forecast['main']['temp_max']

        final_output = 'City: %s \nConditions: %s \nTemperature: %s (°C) \nHumidity: %s %% \nPressure: %s hpa \nTemperature (min): %s (°C) \nTemperature (max): %s (°C)' % (name, description, temperature, humidity, pressure, temp_min, temp_max)
    except:
        # Catches error if user input is invalid
        final_output = 'There was a problem retreiving that information'
    
    return final_output


# Make API request to openweathermap.org to retrieve weather data based on city
# URL Link: api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}
# Example API key: b6907d289e10d714a6e88b30761fae22
def get_weather(city):
    weather_key = 'b6907d289e10d714a6e88b30761fae22'
    url = 'https://openweathermap.org/data/2.5/weather?q=' + city + ',uk&appid=' + weather_key
    params = {'APPID': weather_key, 'q': city, 'units': 'celsius'}
    response = requests.get(url, params=params)
    weather_forecast = response.json()
    print(weather_forecast)
    
    label['text'] = format_response(weather_forecast)


# The root serves as the foundation layer of the application
root = tk.Tk()
root.title("Minimalistic Weather App")
root.iconbitmap("sun_cloud_icon.ico")

# Variables 
HEIGHT = 500
WIDTH = 600
change_image = 'clouds.png'

# Setting up Canvas
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Setting up background image
background_image = tk.PhotoImage(file='%s' % (change_image))
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Setting up upper frame 
# relwidth and rellheight 'fills the parent'
# relx and rely 'centers' the frame (based on %)
upper_frame = tk.Frame(root, bg='#80c1ff', bd=5)
upper_frame.place(relx=0.5, rely=0.1, relwidth=0.75,relheight=0.1, anchor='n')

# Enables text strings from user
entry = tk.Entry(upper_frame, font=('Courier',18))
entry.place(relwidth=0.65, relheight=1)

# Lamda function gets current state of entry upon clicking the 'Get Weather' button
button = tk.Button(upper_frame, text = "Get Weather", font=('Courier',12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

# Setting up lower frame 
lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,relheight=0.5, anchor='n')

# Setting up label widget
label = tk.Label(lower_frame, font=('Courier',18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

# Execution of program
root.mainloop()