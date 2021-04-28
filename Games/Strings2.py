s1 = input('Введите первую строку: ')
s2 = input('Введите вторую строку: ')
f = True
for i in range(len(s1)): #Обрезаем концы
    if (s1[i] != s2[i]) and (s1[i] != '*'):
        f = False
        break
    elif s1[i] == '*':
        s1 = s1[i+1 : len(s1)]
        s2 = s2[i : len(s2)]
        break
if f:
    for i in range(1 , len(s1)-1):
        if (s1[-i] != s2[-i]) and (s1[-i] != '*'):
            f = False
            print(11)
            break
        elif s1[-i] == '*':
            s1 = s1[0 : -i]
            s2 = s2[0 : -i + 1]
            break
s = ''
if f:  
    for i in range(len(s1)):
        print('s =  ' + s)
        if (s1[i] == '*' or i == len(s1)-1) and (s in s2):
            s2 = s2[s2.find(s , 0 , len(s2)) + len(s) : len(s2)]
            print('s2 =  ' + s2)
            s = ''
        elif (s1[i] == '*' or i == len(s1)-1) and (s not in s2):
            f = False
            break
        else:
            s += s1[i]    
if f:
    print('Все круто!')
else:
    print('Неправильно!')
