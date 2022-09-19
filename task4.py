# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

from random import randint


try:
    k = int(input('\nEnter power k: \t'))

    factors = [randint(0, 10) for _ in range(k+1)]

    def polynom(k, factors):
        polynom = []
        for i in range(k):
            if factors[i] > 1 and k - i > 1:
                polynom.append(f'{str(factors[i])}X^{k - i}')
            elif factors[i] > 1 and k - i == 1:
                polynom.append(f'{str(factors[i])}X')
            elif factors[i] == 1 and k - i > 1:
                polynom.append(f'X^{k - i}')
            elif factors[i] == 1 and k - i == 1:
                polynom.append('X')
        if factors[-1] != 0:
            polynom.append(str(factors[-1]))
        pol = ' + '.join(polynom)+' = 0'
        return pol

    pol = polynom(k, factors)
    print('\nRandom factors -->\t', *factors)
    print(f'\nPolynom -->\t{pol}\n')

except ValueError:
    print('Incorrect data! You must enter number, try again!')
with open('polynom2.txt', 'a') as data:
    data.write(f'Power k -->\t{k}')
    data.write(f'\nRandom factors -->\t{factors}')
    data.write(f'\nPolynom -->\t{pol}\n')
data.close()
