#calculate gravity on a user

#input/data
mass_u= float(input('Enter a mass in kg:'))
universal_gravitational = 6.67300 * 10**-11
radius_Earth = 6378 * 10**3
mass_Earth = 5.9742 * 10**24

#Calculations/Processing
acceleration_g = ((universal_gravitational * mass_Earth * mass_u) / (radius_Earth ** 2))/ mass_u

#output
print('')
print('The resulting value of g is', format( acceleration_g, '.4f') ,'which \
is close to the earth’s gravitational force.')
