"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers (*p_num):
    return  [el ** 2 for el in p_num]
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


result = power_numbers (1, 2, 5, 7)
print (result)

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def check_odd (p_num):
  if p_num % 2  != 0:
    return True
  else:
    return False


def check_even (p_num):
  if p_num % 2  == 0:
    return True
  else:
    return False


def chek_prime(p_num):
    for i in range(2, (p_num//2)+1):
        if p_num % i == 0:
            return False
    return True


def filter_numbers(p_num, p_param):
    if p_param == ODD:
        return list(filter (check_odd, p_num))
    if p_param == EVEN:
        return list(filter (check_even, p_num))
    if p_param == PRIME:
      return list(filter (chek_prime, p_num))
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

result = filter_numbers([1, 2, 3, 5,6,7,8], PRIME)
print(result)