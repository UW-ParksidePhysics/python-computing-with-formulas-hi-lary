# length conversion
"""
1 inch = 2.54 cm
1 foot = 12 inches
1 yard = 3 feet
1 brit mile = 1760 yards
"""

initial_length = eval(input('meters:'))
cm = initial_length * 100  # meters to cm
inches = cm / 2.54  # cm to in
feet = inches / 12  # in to ft
yards = feet / 3  # ft to yds
miles = yards / 1760  # yds to brit mile

print(f'Given {initial_length} meters, we get : {inches} inches, {feet} feet,\
 {yards} yards, and {miles} british miles.')
