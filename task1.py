
def pi(n):
    pi = 0
    for i in range(100):
        pi += float(1/(16**i))*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
    return round(pi, n)


try:
    n = int(input('\nEnter number of digits after the decimal point from 0 to 15:\t'))
    print(f'\nNumber π --> {pi(n)}\n')
except ValueError:
    print('Incorrect data! You must enter number, try again!')
