#the program shows the codes to do items a to f based on given sets)

set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

set4 = set1 ^ set2
list4 = list(set4)
list4.sort()
set4 = set(list4)
print('a.',set4)

set5 = set1 - ( set2 | set3 ) | set2 - ( set1 | set3 ) | set3 - ( set1 | set2)
list5 = list(set5)
list5.sort()
set5 = set(list5)
print('b.',set5)

set6 = ( set1 & set2 ) - set3 | ( set2  & set3 ) - set1 | ( set1 & set3 ) - set2
list6 = list(set6)
list6.sort()
set6 = set(list6)
print('c.',set6)

list7 = list()
for num in range(1, 26):
   list7.append(num)
set7 = set(list7)
set7_1 = set7 - set1
print('d.',set7_1)

list8 = list()
for num in range(1, 26):
   list8.append(num)
set8 = set(list8)
set8_1 = set8 - (set1 | set2 | set3)
print('e.',set8_1)

list9 = list()
for num in range(1, 26):
   list9.append(num)
set9 = set(list9)
set9_1 = set9 - (set1 & set2 & set3)
print('f.',set9_1)
