"""
Домашнее задание №1
Функции и структуры данных
"""
def power_numbers(numbers):
    result = []
    for number in numbers:
        result.append(number ** 2)
    return result

list1 = [1, 3, 4]
g = power_numbers(list1)
print(g)

    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(number):
    return isprime(number)

t = None
def filter_numbers(numbers, t):
    if t == "odd":
        print(t)
        result = filter(lambda x: x % 2 != 0, numbers)
        return result
    elif t == "even":
        print(t)
        result = filter(lambda x: x % 2 == 0, numbers)
        return result
    elif t == "prime":
        print(t)
        result = filter(is_prime, numbers)
        return result

print(list(filter_numbers([1, 2, 3, 4], ODD)))
print(list(filter_numbers([1, 2, 3, 4], EVEN)))
print(list(filter_numbers([1, 2, 3, 4, 5, 25, 17, 19], PRIME)))
