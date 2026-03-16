#This program Calculate the profit or loss of stocks

#input
income = int(input('Enter income as an integer with no commas: '))

#calculation/output

while income >= 0:
#Old income tax brackets (2017 and older)
    if income <= 9325:
        tax_2017 = income * 0.1
    elif income > 9325 and income <= 37950:
        tax_2017 = (9325 * 0.1) + ((income - 9325) * .15)
    elif income > 37950 and income <= 91900:
        tax_2017 = (9325 * 0.1) + ((37950 - 9325) * .15) + ((income - 37950) * .25)
    elif income > 91900 and income <= 191650:
        tax_2017 = (9325 * 0.1) + ((37950 - 9325) * .15) + ((91900 - 37950) * .25) + \
              ((income - 91900) * .28)
    elif income > 191650 and income <= 416700:
        tax_2017 = (9325 * 0.1) + ((37950 - 9325) * .15) + ((91900 - 37950) * .25) + \
              ((191650 - 91900) * .28) + ((income - 191650) * .33)
    elif income > 416700 and income <= 418400:
        tax_2017 = (9325 * 0.1) + ((37950 - 9325) * .15) + ((91900 - 37950) * .25) + \
              ((191650 - 91900) * .28) + ((416700 - 191650) * .33) + ((income - 416700) * .35)
    else:
        tax_2017 = (9325 * 0.1) + ((37950 - 9325) * .15) + ((91900 - 37950) * .25) + \
              ((191650 - 91900) * .28) + ((416700 - 191650) * .33) + ((418400 - 416700) * .35) + ((income - 418400) * .396)
#New income tax brackets (2018 and newer)
    if income <= 9525:
        tax_2018 = income * 0.1
    elif income > 9525 and income <= 38700:
        tax_2018 = (9525 * 0.1) + ((income - 9525) * .12)
    elif income > 38700 and income <= 82500:
        tax_2018 = (9525 * 0.1) + ((38700 - 9525) * .12) + ((income - 38700) * .22)
    elif income > 82500 and income <= 157500:
        tax_2018 = (9525 * 0.1) + ((38700 - 9525) * .12) + ((82500 - 38700) * .22) + \
              ((income - 82500) * .24)
    elif income > 157500 and income <= 200000:
        tax_2018 = (9525 * 0.1) + ((38700 - 9525) * .12) + ((82500 - 38700) * .22) + \
              ((157500 - 82500) * .24) + ((income - 157500) * .32)
    elif income > 200000 and income <= 500000:
        tax_2018 = (9525 * 0.1) + ((38700 - 9525) * .12) + ((82500 - 38700) * .22) + \
              ((157500 - 82500) * .24) + ((200000 - 157500) * .32) +((income - 200000) * .35)
    else:
        tax_2018 = (9525 * 0.1) + ((38700 - 9525) * .12) + ((82500 - 38700) * .22) + \
              ((157500 - 82500) * .24) + ((200000 - 157500) * .32) + ((500000 - 200000) * .35) + ((income - 500000) * .37)
    Difference = tax_2018 - tax_2017
    if tax_2017 == 0:
        Difference_percent = 0.00
    elif tax_2017 > tax_2018:
        Difference_percent = -1 * (Difference / tax_2017) * 100
    else: 
        Difference_percent = (Difference / tax_2017) * 100
    print('Income:',format(income, '.2f'))
    print('2017 tax:',format(tax_2017, '.2f'))
    print('2018 tax:',format(tax_2018, '.2f'))
    print('Difference:',format(Difference, '.2f'))
    print('Difference (percent):',format(Difference_percent, '.2f'))
    income = int(input('\nEnter income as an integer with no commas: '))
