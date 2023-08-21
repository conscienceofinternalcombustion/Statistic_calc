import numpy as np




def math_expectation(table_for_count):
  number_of_elems = len(table_for_count)
  sum_of_em = sum(table_for_count)
  return sum_of_em // number_of_elems

def num_in_square(take_num):
  return [i ** 2 for i in take_num]

def num_in_cube(take_num):
  return [i ** 3 for i in take_num]

def num_in_four(take_num):
  return [i ** 4 for i in take_num]

def disperses(math_expect_from_smt_in_square, usual_math_expect):
  us_m_exp = usual_math_expect**2
  dispers = math_expect_from_smt_in_square - us_m_exp
  return dispers

def x_mult_y (x, y):
  resl = np.multiply(x,y)
  return resl




#x_people = int(input('Введиде население: '))
#per_cent_of_growth = input('На какой процент увеличилось население: ')
x = list(map(float, input('x = ').split())) 
y = list(map(float, input('y = ').split()))
number_of_elems = int(input('Число элементов списка: '))

math_expect_x = math_expectation(x)
math_expect_y = math_expectation(y)
print("Мат. ожидание X: ", math_expect_x)
print("Мат. ожидание Y: ", math_expect_y)

Xi_in_square = num_in_square(x)
Yi_in_square = num_in_square(y)
print('Xi^2: ', Xi_in_square)
print('Yi^2: ', Yi_in_square)

math_expect_x_in_square = math_expectation(Xi_in_square)
math_expect_y_in_square = math_expectation(Yi_in_square)
print('Мат. ожидание Xi^2: ', math_expect_x_in_square)
print('Мат. ожидание Yi^2: ', math_expect_y_in_square)

dispersion_x = disperses(math_expect_x_in_square, math_expect_x)
dispersion_y = disperses(math_expect_y_in_square, math_expect_y)
print('Дисперсия X: ', dispersion_x)
print('Дисперсия Y: ', dispersion_y)

# Икс умноженный на игрек
x_mul_y = x_mult_y(x, y)
print('X * Y = ', x_mul_y)


# Ищем мат ожидание от икса и игрека ужноженных друг на друга
m_xy = math_expectation(x_mul_y)
print('M(X*Y) = ', m_xy)

# Ищем б
first_part_of_formula_for_b = m_xy - math_expect_x * math_expect_y
seacond_part_of_formula_for_b = math_expect_x_in_square - math_expect_x**2
b = first_part_of_formula_for_b/seacond_part_of_formula_for_b
print('b = ', b)

# Считаем а
a = math_expect_y - b * math_expect_x
print('a = ', a)


# Считаем игрек в шапочке
p = a + b
yi_under_hat = p*np.array(x)
print('Yi в шапке: ', yi_under_hat)

# Рост населения прогноз
'''one_per_cent = 90 / 100
x_per_cents = one_per_cent * 10 #per_cent_of_growth
result_number_of_growth = 90 + x_per_cents #x_people + x_per_cents
y_with_per_cent_of_population = b * result_number_of_growth + a
print('У с учетом роста населения равен: ', y_with_per_cent_of_population)'''

# Сумма иксов
sum_of_x = sum(x)
print('Сумма иксов: ', sum_of_x)
# Сумма иксов в квадрате
sum_of_x_in_square = sum(Xi_in_square)
print('Сумма иксов в квадрате: ', sum_of_x_in_square)
# Сумма иксов в кубе
sum_of_x_in_cube = sum(num_in_cube(x))
print('Сумма иксов в кубе: ', sum_of_x_in_cube)
# Сумма иксов в 4 степени
sum_of_x_in_four = sum(num_in_four(x))
print('Сумма иксов в 4 степени: ', sum_of_x_in_four)

#b=k
#a=b
y_prediction = b * 12
res_y = y_prediction + a
print('y = kx + b ', res_y)
