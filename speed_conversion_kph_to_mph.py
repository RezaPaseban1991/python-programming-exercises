#the program convert speeds from kph to mph


#input
conversion_factor = 0.6214

#process/output
print('KPH\tMPH')
print('-' * 36)
for speed in range(60,131,10):
    MPH = speed * conversion_factor
    print(speed,'\t',format(MPH, '.2f'))
