# Loops
# 7/5/2019
# CTI-110 P4HW1 - Calories Burned
# N Faircloth
#

#description of algorithm
#start counting calories in 1 minute increments
#count until reaching the desired set points
#display set points

def main():
    # 5 calories/minute burn, init to zero.
    min = 0
    while min < 60:
        #calculate calories
        cal = 5 * min
        #log values at 20, 35, 45 minute intervals
        if min == 20:
            print("20 Minutes = ", cal, " calories burned.")
        if min == 35:
            print("35 Minutes = ", cal, " calories burned.")
        if min == 45:
            print("45 Minutes = ", cal, " calories burned.")
        #increment minute
        min  += 1

main()
