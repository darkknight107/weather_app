import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH= 600

def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature: %s' % (name, description, temp)
    except:
        final_str = 'There was a problem retrieving that information. Please enter a valid city.'

    return final_str

def get_weather(city):
    weather_key = '5c93907f138c124935e3075d2fb1cfaa'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID' : weather_key, 'q': city, 'units' : 'imperial'}
    response = requests.get(url, params= params)
    weather = response.json()
    label['text'] = format_response(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file = 'landscape.png')
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

frame = tk.Frame(root, bg = "#80c1ff", bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

entry = tk.Entry(frame, font = ('Courier', 18))
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text = "Get Weather", font = 40, command = lambda : get_weather(entry.get()))
button.place(relx = 0.7, relwidth = 0.3, relheight = 1)

lower_frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

label = tk.Label(lower_frame, font = ('Courier', 18), anchor = 'nw', justify = 'left', bd = 4)
label.place(relwidth = 1, relheight = 1)
root.mainloop()