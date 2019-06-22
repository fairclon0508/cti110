# Meal and Tip calculator
# 6/12/2019
# CTI-110 P2HW2 - Meal Tip Calculator
# Faircloth N
#

#user inputs meal price
cost = float(input('Enter the meal cost: $'))

#calculate multiple tip values
tip_low = cost * .15
tip_med = cost * .18
tip_high = cost * .2

#output tip and total cost values
print('15% = ', format(tip_low, ',.2f'), '\tTotal cost = $',  format(cost + tip_low, ',.2f'), \
      '\n18% = ', format(tip_med, ',.2f'), '\tTotal cost = $',  format(cost + tip_med, ',.2f'), \
      '\n20% = ', format(tip_high, ',.2f'), '\tTotal cost = $',  format(cost + tip_high, ',.2f'))
