#Calculate the profit or loss of stocks

#input/data
print('*'*33)
print('* Enter Information for Stock 1 *')
print('*'*33)
stock1 = input('Enter Stock Name in Uppercase:')
num_sharesbought1 = int(input('Enter Number of Shares:'))
purchase_price1 = float(input('Enter Purchase Price:'))
selling_Price1 = float(input('Enter Selling Price:'))
broker_Commission1 = float(input('Enter Commission (in percent):'))
print('\n')

#Calculations/Processing
amount_paid = num_sharesbought1*purchase_price1
purchase_commission = amount_paid*(broker_Commission1/100)
sell_amount = num_sharesbought1*selling_Price1
selling_commission = sell_amount*(broker_Commission1/100)
profit_loss = (sell_amount - selling_commission) - \
(amount_paid + purchase_commission)

#output
print('-'*60)
print(stock1)
print('')
print('Amount paid for the stock:          $',format(amount_paid, '13,.2f'))
print('Commission paid on the purchase:    $',format(purchase_commission, '13,.2f'))
print('Amount the stock sold for:          $',format(sell_amount, '13,.2f'))
print('Commission paid on the sale:        $',format(selling_commission, '13,.2f'))
print('Profit (or loss if negative):       $',format(profit_loss, '13,.2f'))
print('')
print('-'*60)
print('\n')

#input/data
print('*'*33)
print('* Enter Information for Stock 2 *')
print('*'*33)
stock2 = input('Enter Stock Name in Uppercase:')
num_sharesbought2 = int(input('Enter Number of Shares:'))
purchase_price2 = float(input('Enter Purchase Price:'))
selling_Price2 = float(input('Enter Selling Price:'))
broker_Commission2 = float(input('Enter Commission (in percent):'))
print('\n')

#Calculations/Processing
amount_paid = num_sharesbought2*purchase_price2
purchase_commission = amount_paid*(broker_Commission2/100)
sell_amount = num_sharesbought2*selling_Price2
selling_commission = sell_amount*(broker_Commission2/100)
profit_loss = (sell_amount - selling_commission) - \
(amount_paid + purchase_commission)

#output
print('-'*60)
print(stock2)
print('')
print('Amount paid for the stock:          $',format(amount_paid, '13,.2f'))
print('Commission paid on the purchase:    $',format(purchase_commission, '13,.2f'))
print('Amount the stock sold for:          $',format(sell_amount, '13,.2f'))
print('Commission paid on the sale:        $',format(selling_commission, '13,.2f'))
print('Profit (or loss if negative):       $',format(profit_loss, '13,.2f'))
print('')
print('-'*60)
print('\n')

#input/data
print('*'*33)
print('* Enter Information for Stock 3 *')
print('*'*33)
stock3 = input('Enter Stock Name in Uppercase:')
num_sharesbought3 = int(input('Enter Number of Shares:'))
purchase_price3 = float(input('Enter Purchase Price:'))
selling_Price3 = float(input('Enter Selling Price:'))
broker_Commission3 = float(input('Enter Commission (in percent):'))
print('\n')
