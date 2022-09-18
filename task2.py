# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

try:
    number = int(input('\nEnter number N: \t'))
    result = []
    factors = (2, 3, 5, 7)
    for i in factors:
        while number % i == 0:
            result.append(i)
            number /= i
    if number > 1:
        result.append(int(number))
    print(f'\nList of prime factors -->\t{result}\n')
except ValueError:
    print('Incorrect data! You must enter number, try again!')
