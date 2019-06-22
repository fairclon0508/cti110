# Convert pounds to kilograms
# 6/12/2019
# CTI-110 P2HW1 - Pounds to Kilograms Converter
# Faircloth N
#

#take input from user
pounds = float(input('Enter weight in pounds: '))

#convert pounds to kilograms
kilos = pounds / 2.2046

#output kilogram value
print(format(pounds, ',.2f'), 'lbs = ', format(kilos, ',.2f'), 'kgs')
