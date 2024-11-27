my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
control = 0 # // Задаём счетчик
print('\n' * 2 + '  ')
print('Список', my_list, 'Положительные числах из списках')


while control < len(my_list):
    num = my_list[control] # // Задаём число из списка
    control = control + 1 # // Счетчик
    if num == 0:
        continue # // пропускаем 0
    elif num < 0:
        print('\n' * 1 + '-' * 50 + '\n' * 1)
        print('Встретилось отрицательное число:', num )
        break
    elif control == len(my_list):
        print(Num)
        print('Список закончился')
    else:
        print(num)