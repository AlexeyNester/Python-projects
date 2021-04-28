print('Привет, сейчас мы сыграем в игру "Палочки"')
nam1 = input('Введите имя 1ого игрока: ')
nam2 = input('Введите имя 2ого игрока: ')
sticks = int(input('Введите число палочек: '))
i = 1
f1 = 0
f2 = 0
while i == 1:
    s1 = int(input(f'{nam1}, cколько палочек от 1 до 3 вы хотите вытянуть: '))
    sticks = sticks - s1
    if sticks <= 0:
        print(f'Поздравляем, {nam2}! Вы победили {nam1}')
        break
    print('Осталось палочек: ' + str(sticks))
    s2 = int(input(f'{nam2}, cколько палочек от 1 до 3 вы хотите вытянуть: '))
    sticks = sticks - s2
    if sticks <= 0:
        print(f'Поздравляем, {nam1}! Вы победили {nam2}')
        break
    print('Осталось палочек: ' + str(sticks))
print('Конец игры!')