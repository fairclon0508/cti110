# CTI-110
# P3HW1 - Color Mixer
# Faircloth N
# 6/22/2019
#

#prompt user for input of red, blue, or yellow; make lowercase
color1 = str.lower(input('Enter first primary color: '))
color2 = str.lower(input('Enter second primary color: '))

#logic to test user input and accept/reject it
if color1 != 'red':
    if color1 != 'blue':
        if color1 != 'yellow':
            print('Error color 1: Colors must be red, blue, or yellow.')
            quit()
if color2 != 'red':
    if color2 != 'blue':
        if color2 != 'yellow':
            print('Error color 2: Colors must be red, blue, or yellow.')
            quit()
if color1 == color2:
    print('Colors must be different.')
    quit()

#determine correct output based on input
if color1 == 'red' and color2 == 'blue':
    print('Purple')
if color1 == 'blue' and color2 == 'red':
    print('Purple')
if color1 == 'red' and color2 == 'yellow':
    print('Orange')
if color1 == 'yellow' and color2 == 'red':
    print('Orange')
if color1 == 'yellow' and color2 == 'blue':
    print('Green')
if color1 == 'blue' and color2 == 'yellow':
    print('Green')
