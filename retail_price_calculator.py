#validation where user input wholesale prices to calculate retail prices

#initialization
markup = 2.5
again = 'y'
repeat = True

#input
wholesale_c = float(input('Enter the item’s wholesale cost:'))

#calculation/output
while repeat == True:
    if wholesale_c < 0: 
        print('ERROR: the cost cannot be negative')
        wholesale_c = float(input('Enter the item’s wholesale cost:'))
    else:
        retail_price = wholesale_c * markup
        print('Retail price is $',format(retail_price, '.2f'), sep='')
        again = input('Do you have another item? (Enter y for yes):')
        if again == 'y' or again == 'Y':
            wholesale_c = float(input('Enter the item’s wholesale cost:'))   
        else:
            repeat = False
