#the program using list and highlighting the largest number
 

def readvalues()->(list):
    '''this function reads in a series of string
    values by the user into a list'''
    num_list = []
    values = 'Q'
    print('Please enter values, Q to quit :')
    values = input()
    while values.upper() != 'Q':
        num_list.append(values)
        values = input()
         
    return num_list


def findLargest(num_list)->(float):
    '''this function passes the list into
    the function and find largest'''
    if len(num_list) > 0:
        large = float(num_list[0])
        for values in num_list:
            if float(values) > large:
                large = float(values)
        return large
    else:
        large = 0
        return large


def display(num_list,large)->None:
    '''display the list and highlight the largest'''
    print()
    if len(num_list) > 0:
        print('Here are the numbers in the list')
        for values in num_list:
            if float(values) != large:
                print(values)
            else:
                print(values, ' <==this is the largest number', sep='')
            

def main():
    num_list = readvalues()
    large = findLargest(num_list) 
    display(num_list,large)
    

if __name__ == "__main__":
    main()
