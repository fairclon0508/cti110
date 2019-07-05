# Loops to convert weights
# 7/5/2019
# CTI-110 P4HW2 - Pounds to Kilos Table
# N Faircloth
#

#desc of algorithm:
#count from 100 to 300 using 10 unit increments
#do math at each increment
#display output of math at each increment in table
#increment

def main():
    #start table
    print("Pounds\tKilos")
    #counts starting at 100, ends at 300+1, increment of 10
    for pounds in range(100, 310, 10):
        kilos = round(pounds / 2.2046, 2)
        print(pounds, "\t", kilos)       

main()
