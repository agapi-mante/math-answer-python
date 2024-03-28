# Функция для вычисления площади прямоугольника
def rectangle_area(side1, side2):
    return side1 * side2

# Ввод сторон для трех прямоугольников
for i in range(3):
    side1 = float(input(f"Введите длину стороны A для прямоугольника {i+1}: "))
    side2 = float(input(f"Введите длину стороны B для прямоугольника {i+1}: "))
    area = rectangle_area(side1, side2)
    print(f"Площадь прямоугольника {i+1}: {area}")
