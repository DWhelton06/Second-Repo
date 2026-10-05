import math

#PArt A
survey_angle = float(input("Enter the survey angle in degrees: "))
shadow_length = float(input("Enter the shadow length in meters: "))

survey_distance = shadow_length / (math.cos(math.radians(survey_angle)))

print(f"The survey distance is: {survey_distance:.2f} meters")

#Part B

ph = float(input("Enter the pH of the water: "))

if ph < 6.5:
    print("The water is acidic.")
elif ph <= 8.5 and ph >= 6.5:
    print("The water is neutral.")
elif ph > 8.5:
    print("The water is alkaline.")

