#Существует только одна тройка Пифагора, для которой a + b + c = 1000.
#Найдите произведение abc

# a^2 + b^2 + c^2 = 2(a^2 + b^2)

# c^2 = a^2 + b^2
# c = 1000 - a - b
# a + b = 1000 - c
# (a + b)^2 = c^2 + 2ab
# abc = ab(a^2+b^2)^(1/2)
# abc = ab(1000 - a - b)


# попробуем умножить на abc:
# (c^2 - b^2)bc + (c^2 - a^2)ac + (a^2 + b^2)ab = 1000abc

# (a + b + c)^2 = 10^6
# a^2 + b^2 + c^2 + 2ab + 2ac + 2bc = 10^6
# 2a^2 + 2b^2 + 2ab + (a + b)*2*c = 10^6



# Хз, пишу такой костыль:
a = 1
while a < 1000:	
    b = a
    while b < 1000:
        c = (a**2 + b**2)**(1/2)
        p = c.is_integer()
        if a + b + c == 1000 and p:
            pr = a*b*c
            print('Ответы: a = ' + str(a) + ' b= ' + str(b) + ' c= ' + str(c))
            print('Их произведение: ' + str(pr))
        b = b + 1
    a = a + 1     
print('Конец вычислений!')

