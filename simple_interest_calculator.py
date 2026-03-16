# the program calcuate the interest

def show_interest(rate = 0.01, period = 10, principal = 10000.00)->(float):
    '''the function calculates the interest'''
    
    #calculation
    interest = principal * rate * period
    
    return interest 
    
     
def main():  
    print('The simple interest will be $',format(show_interest(),',.2f'), sep="")
    
    
if __name__ == "__main__":
    main()
