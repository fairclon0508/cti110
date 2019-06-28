# CTI-110
# P3LAB
# Faircloth, N
# 6/27/2019
#

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    #take user input
    score = input('Enter grade: ')
    
    #test user input
    try:
        score = float(score)
    except:
        print('Error: grade must be a number')
        quit()

    if score >= A_score:
        print('Your grade is: A')
    elif A_score >= score >= B_score:
        print('Your grade is: B')
    elif B_score >= score >= C_score:
        print('Your grade is: C')
    elif C_score >= score >= D_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F')

# program start
main()
