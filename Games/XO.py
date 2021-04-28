import sys
#sys.exit(1)
a = [['0' , '1' , '2'] , ['3' , '4', '5'] , ['6', '7' , '8']]
print(a[0])
print(a[1])
print(a[2])

while 1 == 1:

    while 1 == 1:

        while 1 == 1:

            print('В какую позицию вы хотите поставить х? ')
            x = input()
            if int(x) not in range(0, 9):
                print('Введите еще раз')
                continue
            break

        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == x:
                    index1 = i
                    index2 = j

        if a[index1][index2] != 'х' and a[index1][index2] != 'о':
            a[index1][index2] = 'х'
        else:
            print('Позиция занята уже, введите еще раз!')
            continue
        break

    print(a[0])
    print(a[1])
    print(a[2])

    for i in range(len(a)):
        if (a[i][0] == a[i][1] == a[i][2]) or (a[0][i] == a[1][i] == a[2][i]):
            print('Победа х!')
            sys.exit(1)
    if (a[0][0] == a[1][1] == a[2][2]) or (a[2][0] == a[1][1] == a[0][2]):
        print('Победа х!')
        sys.exit(1)
    while 1 == 1:

        while 1 == 1:

            print('В какую позицию вы хотите поставить о? ')
            x = input()
            if int(x) not in range(0, 9):
                print('Введите еще раз')
                continue
            break

        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == x:
                    index1 = i
                    index2 = j
        if a[index1][index2] != 'о' and a[index1][index2] != 'о':
            a[index1][index2] = 'о'
        else:
            print('Позиция занята уже, введите еще раз!')
            continue
        break
    print(a[0])
    print(a[1])
    print(a[2])
    for i in range(len(a)):
        if (a[i][0] == a[i][1] == a[i][2]) or (a[0][i] == a[1][i] == a[2][i]):
            print('Победа о!')
            sys.exit(1)
    if a[0][0] == a[1][1] == a[2][2] or a[2][0] == a[1][1] == a[0][2]:
        print('Победа о!')
        sys.exit(1)

