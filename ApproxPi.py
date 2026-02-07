#ApproxPi.py
#Name:Olivia Sulzle
#Date: 2/8/26
#Assignment: Lab 3
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  precision = int(input("Enter the level of precision (up to 10): "))
  if precision > 10:
   precision = 10
 

  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached
  approxPi = 4/1
  sign = -1
  denom = 3
  while round(approxPi, precision) != round(realPi, precision):
    #print(approxPi)
    approxPi = approxPi + (sign * 4 / denom)

    sign = sign * -1
    denom = denom + 2


  end = time.time()

  elapsedTime = end - start
  print(f"Approximated Pi: {approxPi}")
  print(f"Time: {elapsedTime}")

if __name__ == '__main__':
  main()
