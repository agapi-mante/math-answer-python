import math

# Ввод переменных
x = int(input("Введите значение переменной x: "))
t = int(input("Введите значение переменной t: "))

# Вычисление выражения
z = ((9 * math.pi * t + 10 * math.cos(x)) / (math.sqrt(t) - math.fabs(math.sin(t)))) * math.pow(math.e, x)

# Вывод результата с двумя знаками после запятой
print("Результат выражения: {:.2f}".format(z))
