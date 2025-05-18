# TemperatureConverter class for converting temperatures
class TemperatureConverter:
    
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit"""
        return (celsius * 9/5) + 32  # formula to convert

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):  # fixed spelling
        """Convert Fahrenheit to Celsius"""
        return round((fahrenheit - 32) * 5/9, 2)  # formula to convert

# Celsius to Fahrenheit conversion
c = 34
f = TemperatureConverter.celsius_to_fahrenheit(c)
print(f"{c}°C = {f}°F")  # Output in proper format

# Fahrenheit to Celsius conversion
f = 34
c = TemperatureConverter.fahrenheit_to_celsius(f)
print(f"{f}°F = {c}°C")  # Output in proper format
