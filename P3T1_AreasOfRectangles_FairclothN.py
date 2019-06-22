# CH 3 Tutorial
# 6/12/2019
# CTI-110 P3T1 - Ch3 Tutorial
# Faircloth N
#

#collect user input
len1 = int(input('Enter length of rectangle 1: '))
wid1 = int(input('Enter width of rectangle 1: '))
len2 = int(input('Enter length of rectangle 2: '))
wid2 = int(input('Enter width of rectangle 2: '))

#calculate area of rectangles
area1 = len1 * wid1
area2 = len2 * wid2

#determine comparative status of rectangles and output result
if area1 > area2:
    print('The area of rectangle 1 is greater than the area of rectangle 2')
elif area1 < area2:
    print('The area of rectangle 1 is less than the area of rectangle 2')
else:
    print('The area of the two rectangles is equal')
