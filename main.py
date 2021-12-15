print('Ход конём')

# По заданным вещественным координатам коня
# и второй точки программа определяет может ли конь ходить в эту точку.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

import math

print('Введите местоположение коня:')
horse_x = float(input())
horse_y = float(input())

print('Введите местоположение точки на доске:')
point_x = float(input())
point_y = float(input())

horse_int_x = math.floor(horse_x * 10)
horse_int_y = math.floor(horse_y * 10)

point_int_x = math.floor(point_x * 10)
point_int_y = math.floor(point_y * 10)

print('Конь в клетке (' + str(horse_int_x) + ', ' + str(horse_int_y) + '). Точка в клетке (' + str(point_int_x) + ', ' + str(point_int_y) + ').')

# Найдём сумму квадратов катетов:
# модуль horse_int_x - horse_int_y — катет 1
# модуль point_int_x - point_int_y — катет 2

# Один из катетов должен раняться 1, другой — 2, следовательно, квадрат гипотенузы (траектория коня), должен равняться 5

if (abs(horse_int_x - horse_int_y)) ** 2 + (abs(point_int_x - point_int_y)) ** 2 == 5:
  print('Да, конь может ходить в эту точку.')
else:
  print('Нет, конь не может ходить в эту точку.')
