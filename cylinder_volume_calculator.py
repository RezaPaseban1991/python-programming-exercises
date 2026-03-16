#Calculate the valume and area of a cylinder 

#input/data
radius = float(input('Enter the radius of a cylinder:'))
length = float(input('Enter the length of a cylinder:'))
pi = 3.141

#Calculations/Processing
base_area = radius * radius * pi
volume = base_area * length

#Output
print('The base area is', format(base_area, '.5f' ))
print('The volume of cylinder is', format(volume, '.3f'))
