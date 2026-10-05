power_hp = float(input("Enter the power in horsepower: "))  # Takes an input from the user for power in horsepower
                                                            # Converts the input to a float for calculations   

power_kW = power_hp * 0.7457            # Converts the power from horsepower to kilowatts using the conversion factor 1 hp = 0.7457 kW

print(f"The power in kilowatts is: {power_kW:.2f} kW")      # Prints the power in kilowatts.
