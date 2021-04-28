#Самая длинная последовательность Коллатца
def posled(n):
    l = []
    l.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        l.append(n)
    return l


max_num = 0
chec = 0
a = 0
#print(posled(837799)) - наиб число
for i in range(500000 , 1000000):
    a = posled(i)
    if max_num < a:
        chec = i
        max_num = a
print('Макс число = ' + str(max_num))
print('Само число = ' + str(chec))