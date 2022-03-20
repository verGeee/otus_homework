"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers, power=2):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** power for num in numbers]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(numbers):
    result = []
    if numbers > 1:
        for n in range(2, numbers):
            if numbers % n == 0:
                break
        else:
            result.append(numbers)
    return (result)

input_data = [0,1,2,3,4,5,6,7,8,9,10,11]

def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == "odd":
        return [num for num in numbers if num % 2 != 0]
    elif filter_type == "even":
        return [num for num in numbers if num % 2 == 0]
    elif filter_type == "prime":
        return list(filter(is_prime, numbers))
