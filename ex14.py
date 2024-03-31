def find_min_odd_element(lst):
    """
    Функция находит наименьший нечетный элемент списка.
    
    Аргументы:
    lst: list - список целых чисел
    
    Возвращает:
    min_odd: int - наименьший нечетный элемент списка
    """
    # Инициализируем переменную для хранения наименьшего нечетного элемента
    min_odd = None
    
    # Проходим по каждому элементу списка
    for num in lst:
        if num % 2 != 0:  # Проверяем, является ли текущий элемент нечетным
            if min_odd is None or num < min_odd:  # Если min_odd еще не был инициализирован
                min_odd = num  # или текущий элемент меньше текущего min_odd, обновляем min_odd
    
    return min_odd  # Возвращаем наименьший нечетный элемент списка

# Пример использования:
lst = [2, 3, 5, 8, 9, 12, 15]
min_odd = find_min_odd_element(lst)
print("Наименьший нечетный элемент списка:", min_odd)

def swap_arrays(A, B):
    """
    Функция меняет местами содержимое двух массивов A и B
    и выводит их элементы поочередно.
    
    Аргументы:
    A: list - первый массив
    B: list - второй массив
    
    Возвращает:
    None
    """
    # Меняем местами содержимое массивов
    A[:], B[:] = B[:], A[:]
    
    # Выводим элементы преобразованного массива A
    print("Элементы преобразованного массива A:", A)
    
    # Выводим элементы преобразованного массива B
    print("Элементы преобразованного массива B:", B)

# Пример использования:
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
swap_arrays(A, B)

#Этот код находит наименьший нечетный элемент списка и выводит его на экран. Затем он меняет местами содержимое двух массивов и выводит элементы каждого массива поочередно.