name = input('Как вас зовут?  ')
print(f'Здравствуйте, {name} ! Давайте сыграем с вами в игру под названием Угадай число! У вас 6 попыток!')
import random
x = 1
flag = False
rand = random.randint(1, 50)
while x <= 6:
    number = float(input(f'Введите число номер {x}:  '))
    if number < rand:
        print('Загаданное число больше!')
    elif number == rand:
        print(f'Ура, {name}, ты победил!!! Загаданное число = ' + str(rand))
        flag = True
        break
    else:
        print('Загаданное число меньше!')
    x+=1
if flag == False:
	print(f'Вы проиграли, {name}!')

