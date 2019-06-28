# CTI-110
# P3HW2 - MealTipTax
# Faircloth, N
# 6/27/2019
#

#user inputs meal price
cost_str = input('Enter the meal cost: $')

#today I learned about exceptions
#attempt to convert string input to float, if unsuccessful output error and end program.
try:
    cost = float(cost_str)
except:
    print('Error: Meal cost must be a number.')
    quit()

#user inputs tip %
tip_str = input('Enter tip % (15, 18, or 20):')

#attempt to convert string input to float, if unsuccessful output error and end program.
try:
    tip = float(tip_str)    
except:
    print('Error: Tip % must be a number')
    quit()

#validate tip amount
if tip != 15:
    if tip != 18:
        if tip != 20:
            print('Error: Tip % must be 15, 18, or 20')
            quit()

#divide by 100 and multiply to cost to find tip
tip = tip / 100 * cost

#calculate tax value at 7%
tax = cost * .07

#calculate total
total = cost + tip + tax

#output calculated values
print('Tip: $', format(tip, ',.2f'), '\tTax: $', format(tax, ',.2f'), '\tTotal: $', format(total, ',.2f'))



