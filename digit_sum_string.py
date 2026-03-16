#the program gives a single-digit number display the sum of all
#the single digit numbers in the single-digit string.

import random
#input
def string_total(number_string: str) -> int:
    '''The function gives a single-digit number and calculates 
    the total sum of all digits in intiger.'''
    total = 0
for num in range(len(num_user)):
    number = int(num_user[num])
    total = total + number
    return total


#Input/Output
def main():
    # Get a string of numbers as input from the user.
    number_string = input('Enter a sequence of digits with nothing separating them: ')

    # Call string_total function, and store the total.
    total = string_total(number_string)

    # Display the total.
    print('The total of the digits in the string you entered is', total)

    
if __name__ == "__main__":
    main()
