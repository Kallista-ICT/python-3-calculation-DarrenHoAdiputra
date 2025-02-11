# 
distance = float(input("Enter the distance (in meters):"))
time = float(input("Enter the time (in seconds):"))

# the code in line 6 has the function to do mathematical operations, which is division.
# it divides the value of distance over the value of time, which then the results is a velocity.
# however the results does not have a unit (since it is just an ordinary number).
velocity = distance/time

# the code in line 9 has the function to add the units from the results done in code in line 6.
print(f"The velocity is {velocity:.2f} m/s.")