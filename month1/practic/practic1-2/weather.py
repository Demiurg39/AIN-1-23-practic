#! Python3 
# Прогрмамма для высчета средней температуры воздуха по кыргызстану

# Температуры областей и Бишкека
bish_temp = float(input('Введите температуру воздуха Бишкека области\n> '))
chui_temp = float(input('Введите температуру воздуха Чуйской области\n> '))
issik_temp = float(input('Введите температуру воздуха Иссык-кульской области\n> '))
talas_temp = float(input('Введите температуру воздуха Таласской области\n> '))
jalal_abad_temp = float(input('Введите температуру воздуха Джалал-Абадской области\n> '))
naryn_temp = float(input('Введите температуру воздуха Нарынской области\n> '))
osh_temp = float(input('Введите температуру воздуха Ошской области\n> '))
batken_temp = float(input('Введите температуру воздуха Баткенской области\n> '))

# Средняя температура
medium_temp = (chui_temp+issik_temp+talas_temp+jalal_abad_temp+naryn_temp\
               +osh_temp+batken_temp+bish_temp)/8

print(f'Средний показатель температуры воздуха по Кыргызстану на сегодня: {round(medium_temp, 1)}')
