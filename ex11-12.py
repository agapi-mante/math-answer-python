def filter_numbers(*args):
    """
    Функция фильтрует числа из аргументов, оставляя только те,
    которые принадлежат интервалу [1, 3].
    
    Аргументы:
    *args: int - целые числа для фильтрации
    
    Возвращает:
    filtered_numbers: list - список чисел, принадлежащих интервалу [1, 3]
    """
    filtered_numbers = []  # Создаем пустой список для хранения отфильтрованных чисел
    
    # Проходим по каждому числу из аргументов
    for num in args:
        if 1 <= num <= 3:  # Проверяем, принадлежит ли число интервалу [1, 3]
            filtered_numbers.append(num)  # Если да, добавляем число в список
    
    return filtered_numbers  # Возвращаем список отфильтрованных чисел

# Пример использования:
num1 = 2
num2 = 4
num3 = 1

result = filter_numbers(num1, num2, num3)
print("Числа из интервала [1, 3]:", result)

"""
Этот код определяет функцию filter_numbers, которая принимает переменное количество аргументов *args. 
Затем она проходит по каждому числу и проверяет, принадлежит ли оно интервалу [1, 3]. Если число удовлетворяет условию, оно добавляется в список filtered_numbers. 
В конце функция возвращает этот список.
"""
