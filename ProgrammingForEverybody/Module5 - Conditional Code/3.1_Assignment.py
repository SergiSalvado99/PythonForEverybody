# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly
# Desired Output -> 498.75

extra_rate = 0
extra_hours = 0

print("Hello! Enter the hours:")

hours = int(input())
    
print("Perfect! Now enter the rate:")
rate = float(input())

if (hours > 40) : 
    extra_hours = hours - 40
    extra_rate = rate * 1.5

pay = ((hours -extra_hours) * rate) + (extra_hours * extra_rate)

print(str(pay))
