import math

# Функция для вычисления площади треугольника по формуле Герона
def area_of_triangle(side):
    return math.sqrt(3) / 4 * side**2

# Ввод стороны шестиугольника
side_length = float(input("Введите длину стороны правильного шестиугольника: "))

# Вычисление площади шестиугольника (6 треугольников)
hexagon_area = 6 * area_of_triangle(side_length)

# Вывод результата
print("Площадь правильного шестиугольника:", hexagon_area)

