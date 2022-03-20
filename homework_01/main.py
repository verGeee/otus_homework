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
    result = []
    for number in numbers:
        result.append(number ** power)
    return result

#print(power_numbers(2,3,4))

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(numbers):
    result = []
    for num in numbers:
        if num > 1:
            for n in range(2, num):
                if num % n == 0:
                    break
            else:
                result.append(num)
    return (result)

input_data = [0,1,2,3,4,5,6,7,8,9,10,11]

def filter_numbers(numbers, filter):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter == "odd":
        result = [num for num in numbers if num % 2 != 0]
    elif filter == "even":
        result = [num for num in numbers if num % 2 == 0]
    elif filter == "prime":
        result = (filter(is_prime, numbers))
    return(result)

print(filter_numbers([0,1,2,3,4,5,6,7,8,9,10,11], PRIME))
