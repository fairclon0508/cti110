# Loop tutorial
# 6/29/2019
# CTI-110 P4T2 - Bug Collector
# Faircloth, N
#

def main():

    #initialize variables
    total = 0
    
    #loop representing 5 days
    for i in range(5):
        bugs = int(input("How many bugs were collected? "))
        total += bugs

    print("The total number of bugs collected is: ", total)

main()
