#TempConvert.py
#Name: Olivia Sulzle
#Date: 2/8/26
#Assignment: Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  tempF = float(input("Enter temperature in Farenheit: "))
  #Convert that temperature to celsius, rounding to 1 decimal percision
  tempC = (tempF - 32) * 5 / 9
  tempC_rounded = round(tempC, 1)
  #Output converted temperature.
  print(tempF, "is", tempC_rounded, "degrees Celsius.")

if __name__ == '__main__':
  main()
