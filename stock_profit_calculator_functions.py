#This program Calculate the profit or loss of stocks

def load() -> ( str, int, float, float, float):
    '''The load() function asks the user to enter values'''
    name_stock = input('Enter Stock name : ')
    Num_shares = int(input('Enter Number of shares : '))
    Purchase_p = float(input('Enter Purchase price : '))
    selling_p = float(input('Enter selling price : '))
    Commission = float(input('Enter Commission : '))
    return name_stock, Num_shares, Purchase_p, selling_p,Commission
    

def calc( Num_shares : int, Purchase_p : float, selling_p: float, Commission : float ) -> (float, float, float, float, float):
    '''The calc() function performs all calculations'''
    amount_P =  Num_shares *  Purchase_p
    amount_C_paid = amount_P * (Commission/100)
    amount_S = Num_shares * selling_p
    amount_C_sold = amount_S * (Commission/100)
    Profit_loss = (amount_S - amount_C_sold) - ( amount_P + amount_C_paid)
    return amount_P, amount_C_paid, amount_S, amount_C_sold, Profit_loss


def output(name_stock : str ,amount_P : float, amount_C_paid :float, amount_S:float, amount_C_sold :float,Profit_loss : float) ->None:
    '''The output() function displays the results of one stock transaction.'''
    print('Stock name :', name_stock)
    print('Amount paid for the stock:          $',format(amount_P, '13,.2f'))
    print('Commission paid on the purchase:    $',format(amount_C_paid, '13,.2f'))
    print('Amount the stock sold for:          $',format(amount_S, '13,.2f'))
    print('Commission paid on the sale:        $',format(amount_C_sold, '13,.2f'))
    print('Profit (or loss if negative):       $',format(Profit_loss, '13,.2f'))
    

def main():
    '''The main() function controls the entire program flow'''
    again = input('Enter your stock information? Type ''y'' for yes, or ''n'' for no: ')
    print()
    while again.lower() == 'y':
        name_stock, Num_shares, Purchase_p, selling_p,Commission = load()
        print('\n')
        amount_P, amount_C_paid, amount_S, amount_C_sold, Profit_loss = calc( Num_shares, Purchase_p, selling_p,Commission)
        output(name_stock, amount_P, amount_C_paid, amount_S, amount_C_sold, Profit_loss)
        print('\n')
        again = input('Enter your stock information? Type ''y'' for yes, or ''n'' for no: ')


if __name__ == "__main__":
    main()
