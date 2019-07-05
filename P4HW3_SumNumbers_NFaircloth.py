# Loops
# 7/5/2019
# CTI-110 P4HW3 - Sum of Numbers
# N Faircloth
#

#desc of algorithm:
#run input loop and a running total sum of positive number inputs
#detect negative number input
#output totalled number

def main():
    total = 0
    print("Enter a positive number to add or a negative number to end: ")
    while True:
        temp = input(":: ")

        #attempt to convert input to float without crashing
        try:
            temp = float(temp)
        except:
            #if non-number input, cleanly end program
            print("Error: input must be a number")
            temp = -1
            
        if temp < 0:
            print("Total: ", format(total, ",.2f"))
            break
        else:
            total += temp

main()
