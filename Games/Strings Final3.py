s1 = input('Введите первую строку: ')
s2 = input('Введите вторую строку: ')
f = True
a = 0
ss1 = ''
ss2 = ''
# Надо обрезать конец или обозначить их неравенство! Иначе ошибка в моем методе!
a = max(len(s1) , len(s2))
for i in range(1 , a):
    if (('*' not in s1) and ('*' not in s2)) or ((ss1 != ss2) and (s1[-i] != '*' or s2[-i] != '*')):
        f = False
        break
    elif s1[-i] == '*' or s2[-i] == '*':
        break
    else:
        ss1 += s1[-i]
        ss2 += s2[-i]
print(f)
while 1 == 1:
    ss1 = ''
    ss2 = ''
    if s1 == '' or s2 == '':
        break
    for i in range(len(s1)):
        if s1[i] == '*':
            s1 = s1[0 : s1.find('*' , 0 , len(s1))] + s1[s1.find('*' , 0 , len(s1)) + 1 : len(s1)]
            print('s1 = ' + s1)
            break
        elif i == len(s1):
            break
        else:
            ss1 += s1[i]
    for i in range(len(s2)):
        if s2[i] == '*':
            s2 = s2[0 : s2.find('*' , 0 , len(s2))] + s2[s2.find('*' , 0 , len(s2)) + 1 : len(s2)]
            print('s2 = ' + s2)
            break
        elif i == len(s2):
            break
        else:
            ss2 += s2[i]
   # print('ss1: ' + ss1)
   # print('ss2: ' + ss2)
    if (ss1 in ss2) and (len(ss1) <= len(ss2)):
        s1 = s1[s1.find(ss1 , 0 , len(s1)) + len(ss1) : len(s1)]
        s2 = s2[s2.find(ss1 , 0 , len(s2)) + len(ss1) : len(s2)]
        continue
   #    print('s1: ' + s1)
   #   print('s2: ' + s2)
    elif (ss2 in ss1) and (len(ss2) < len(ss1)): 
        s1 = s1[s1.find(ss2 , 0 , len(s1)) + len(ss2) : len(s1)]
        s2 = s2[s2.find(ss2 , 0 , len(s2)) + len(ss2) : len(s2)]
   #     print('s1: ' + s1)
   #     print('s2: ' + s2)
    else:
        f = False
    if not f:
        break
if f:
    print('Все правильно')
else:
    print('Неправильно!')