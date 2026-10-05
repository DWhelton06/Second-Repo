import random

temps = []

for i in range(20):
    new_temp = random.randint(-10, 40)
    temps.append(new_temp)

print(temps)
average_temp = sum(temps) / len(temps)

print(f"The average temperature is: {average_temp:.2f} degrees Celsius")