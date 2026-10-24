import tkinter as tk
import requests

def weather():
    city = entry.get()
    key = "YOUR_API_KEY"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={key}&units=metric"
    data = requests.get(url).json()

    if data.get("main"):
        result.config(text=
            f"Temperature: {data['main']['temp']} °C\n"
            f"Humidity: {data['main']['humidity']}%\n"
            f"Wind Speed: {data['wind']['speed']} m/s\n"
            f"Weather: {data['weather'][0]['description']}"
        )
    else:
        result.config(text="City not found!")

root = tk.Tk()
root.title("India Weather")
root.geometry("300x300")

tk.Label(root, text="Enter Indian City").pack(pady=10)

entry = tk.Entry(root)
entry.pack()
entry.insert(0, "Pune")

tk.Button(root, text="Check Weather", command=weather).pack(pady=10)

result = tk.Label(root, text="Weather details")
result.pack(pady=10)

root.mainloop()