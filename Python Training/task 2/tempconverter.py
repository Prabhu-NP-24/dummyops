# a program to convert the temperature

user_celsius = int(input("Enter the Celsius value : "))
user_fahrenheit = int(input("Enter the Fahrenheit value : "))

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Converted Fahrenheit is : ", celsius_to_fahrenheit(user_celsius))
print("Converted Celsius is : ", fahrenheit_to_celsius(user_fahrenheit))
