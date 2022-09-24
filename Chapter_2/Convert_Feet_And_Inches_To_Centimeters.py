"""
Write a python program to convert height in feet and inches to centimeters.
Convert height of 5 feet 2 inches to centimeters.
. First convert 5 feet to inches: 5 feet X 12 inches/foot = 60 inches
. Add up our inches: 60 + 2 = 62 inches
. Convert inches to cm: 62 inches X 2.54 cm/inch = 157.48 cm
"""

feet = 5
inches = 2
feet_To_Inches = feet*12
total_Inches = feet_To_Inches + inches
inches_To_cm = total_Inches*2.54
result = inches_To_cm
print(feet,"feet ",inches,"inches  is  equal  to: ",result,"cm")