# Kilometer converter
# 7/14/2019
# CTI-110 P5T1_KilometerConverter
# Faircloth, N
#

def main():
        km = input('Enter a distance in kilometers: ')
        try:
                km = float(km)
        except:
                print('Input must be a number.')
                return 1
        miles = convert(km)
        print(format(km, ',.2f'), 'kilometers is ', format(miles, ',.2f'), 'miles.')
        
# convert kilometers to miles
def convert(num1):
        miles = num1 * 0.6214
        return miles

main()
