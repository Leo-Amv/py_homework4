# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint


# Первый вариант решения
def unique_numbers1(numbers):
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers


# Второй вариант решения
def unique_numbers2(numbers):
    unique_numbers = list(set(numbers))
    return unique_numbers


try:
    numbers = [randint(0, 9)
               for _ in range(int(input('\nEnter list length:\t')))]
    print(f'\nReceived list -->\t{numbers}')
    print(f'\nUnique numbers(1) -->\t{unique_numbers1(numbers)}')
    print(f'\nUnique numbers(2) -->\t{unique_numbers2(numbers)}\n')
except ValueError:
    print('Incorrect data! You must enter number, try again!')
