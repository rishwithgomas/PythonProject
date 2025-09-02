temparature = (float(input("Enter temperature: ")))
scale = input('Enter scale factor "C"/"F"/"K" : ') .strip() .upper()

celsius_to_fahrenheit = ((temparature * 9) / 5) + 32
celsius_to_kelvin = temparature + 273.15
fahrenheit_to_celsius = (temparature - 32) * 5/9
fahrenheit_to_kelvin = (temparature - 32) * 5/9 + 273.15
kelvin_to_celsius = (temparature  - 273.15)
kelvin_to_fahrenheit = (temparature - 32) * 9/5 - 273.15

c = celsius_to_fahrenheit , celsius_to_kelvin
f = fahrenheit_to_celsius, fahrenheit_to_kelvin
k = kelvin_to_celsius, kelvin_to_fahrenheit

if scale == "C":
    print(f"the temparature in fahrenheit = {celsius_to_fahrenheit}F")
    print(f"the temparature in kelvin = {celsius_to_kelvin}K")
elif scale == "F":
    print(f"the temparature in celsius = {fahrenheit_to_celsius}C")
    print(f"the temparature in kelvin = {fahrenheit_to_kelvin}K")
elif scale == "K":
    print(f"the temparature in celsius = {kelvin_to_celsius}C")
    print(f"the temparature in fahrenheit = {kelvin_to_fahrenheit}F")

else :
    print("Invalid scale")






