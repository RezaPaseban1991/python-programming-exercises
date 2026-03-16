#This program calculates a salesperson's pay 

def get_sales() -> (float):
    '''Function to get monthly sales'''
    sales = float(input('Enter the monthly sales:'))         
    return sales
                    

def get_advanced_pay() -> (float):
    '''Function to get advanced pay'''
    print('Enter the amount of advanced pay, or')
    print('enter 0 if no advanced pay was given.')
    advanced_pay = float(input('Advanced pay:'))
    return advanced_pay


def determine_comm_rate(sales) -> (float):
    '''Function to determine commission rate'''
    if sales < 10000.00:
        comm_rate = 0.10
    elif sales > 10000.00 and sales < 14999.99:
        comm_rate = 0.12
    elif sales > 15000.00 and sales < 17999.99:
        comm_rate = 0.14
    elif sales > 18000.00 and sales < 21999.99:
        comm_rate = 0.16
    elif sales > 21999.99:
        comm_rate = 0.18
    return comm_rate


# This program calculates a salesperson's pay
def main():
     # Get the amount of sales from user
     sales = get_sales()
     
     # Get the amount of advanced pay from user.
     advanced_pay = get_advanced_pay()
     
     # Determine the commission rate.
     comm_rate = determine_comm_rate(sales)
     
     # Calculate the pay.
     pay = sales * comm_rate - advanced_pay
     
     # Display the amount of pay.
     print('The pay is $', format(pay, ',.2f'), sep='')
     
     # Determine whether the pay is negative.
     if pay < 0:
     print('The salesperson must reimburse')
     print('the company.'))
     

if __name__ == "__main__":
    main()
