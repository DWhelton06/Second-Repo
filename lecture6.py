data = "TEMP=23.5|HUM=65|PRESS=1013"

split_data = data.split("|")
split_data = [item.split("=") for item in split_data]
split_data = [float(item[1]) for item in split_data]

print(f"Temperature: {split_data[0]} °C")
print(f"Humidity: {split_data[1]} %")
print(f"Pressure: {split_data[2]} hPa")