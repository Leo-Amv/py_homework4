# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

polynom1 = str(open('polynom1.txt', 'r').readlines()[2:3])[15:].split(' =')[0]
polynom2 = str(open('polynom2.txt', 'r').readlines()[2:3])[15:].split(' =')[0]


print(f'\nPolynom from "polynom1.txt" -->\t{polynom1}')
print(f'\nPolynom from "polynom2.txt" -->\t{polynom2}\n')
print(f'Sum of polynomials -->\t{polynom1} + {polynom2}')

with open('sum_of_polynomials.txt', 'w') as sum:
    sum.write(f'Sum of polynomials -->\t{polynom1} + {polynom2}')
sum.close
