s1 = input('Введите первую строку: ')
s2 = input('Введите вторую строку: ')
for i in range(len(s1)):
    if s1[i] == s2[i]:
        f = True
    elif s1[i] == '*':
    	#index = i
    	break
    else: 
        f = False
        break
if f:
    for i in range(len(s1)-1):
        if s1[-i] == s2[-i]:
            f = True
        elif s1[-i] == '*':
        	break
        else: 
            f = False
            break
if f:
    print('Все кул!')
