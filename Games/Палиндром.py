s1 = input('Введите строку: ')
f = True
for i in range(len(s1)):
    #print(s1[i] , s1[-i - 1]) #Вычитаю 1 т.к. i начинается с 0, а значит минус i был бы тоже 0
    if i > len(s1)/2:
        break
    if s1[i] != s1[-i - 1]:
        f = False
if f:
    print('Строка - палиндром')
else:
    print('Строка - не палиндром') 