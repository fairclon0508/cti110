# A brief description of the project
# 7/14/2019
# CTI-110 P5T2_FeetToInches
# Faircloth, N
#

def main():
        feet = input('Enter the number in feet: ')
        try:
                feet = float(feet)
        except:
                return 1
        inches = feet_to_inches(feet)
        print(format(feet, ',.2f'), ' ft is ', format(inches, ',.2f'), ' in.')

def feet_to_inches(num1):
        num2 = num1 * 12
        return num2

main()
