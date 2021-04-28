#I - 1
#V - 5
#X - 10
#L - 50
#C - 100
#D - 500
#M - 1000
def rim(a):
    rim_letter = ['I' , 'V' , 'X' , 'L' , 'C' , 'D' , 'M']
    rim_number = [1 , 5 , 10 , 50 , 100 , 500 , 1000]
    b = []
    for i in a:
        b.append(i)
    j = 0
    g = 0
    arab = 0
    while j < len(a):
        f = 0
        g = j
        while g < len(a):   # Второй цикл нужен для определения есть ли дальше большее значение (см. правило записи римских чисел)
            if rim_letter.index(b[j]) < rim_letter.index(b[g]):
                num = rim_number[rim_letter.index(b[j])] * (-1)
                f = 1
                break
            g = g + 1
        if f == 0:
            num = rim_number[rim_letter.index(b[j])]
        arab += num
        j = j + 1
    return arab
    
a = input('Введите римское число:  ')
b = rim(a)
print(b)
