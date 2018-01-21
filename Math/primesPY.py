#
# Functions developed to calculate the primality of numbers
#

import math

def show_six_n(min_key, max_key):
    for i in range(min_key, max_key+1):
        val = 6*i
        print ('{} --> {}' .format(val - 1, is_prime_sqrt(val-1)))
        print ('{} --> {}' .format(val + 1, is_prime_sqrt(val+1)))

def show_primes(min, max):
    for i in range(min, max):
        if is_prime_sqrt(i) == 0:
            print(i)

def is_prime_sqrt(value):
    # use range[2, sqrt(value)]
    vMax = math.sqrt(value) + 1
    
    vMax = int(str(vMax).split('.')[0])

    for i in range(2, vMax):
        if (i%2 != 0) or (i == 2):
            if value % i == 0:
                return i
                break

    return 0


def is_prime_six(min_key, max_key):
    cp = 2

    for i in range(min_key, max_key+1):
        aux = 6*i

        mOne = is_prime_sqrt(aux - 1)
        pOne = is_prime_sqrt(aux+1)

        if mOne == 0:
          cp += 1
        if pOne == 0:
            cp += 1

    return cp



def primes_lab(min, max):
    print('# OF PRIMES IN 6 times-N plus-or-minus 1')

    print('min = {}\nmax = {}' .format(6*min-1, 6*max+1))

    c_p = is_prime_six(1, max)
    c_cp = ((2 * max) - c_p + 2)
    print('P[{}] = CP[{}]' .format(c_p, c_cp))


def main():
    print('PRIME NUMBERS LAB')
    min = int(input('MIN: '))
    max = int(input('MAX: '))
    base = int(input('BASE: '))

    print('EXP\tN\t6N-1\t6N+1\tP\tCP\tTE\tO')

    for i in range(min, max+1):
        val = int(math.pow(base, i))
        six_n = 6*val
        c_p = is_prime_six(1, val)
        c_cp = ((2 * val) - c_p + 2)

        if val%2 == 0 or val == 1:
            ord_even = (six_n/2)  - (c_p + c_cp - 1) 
            odd = six_n/2
        else:
            ord_even = ((six_n+1)/2) - (c_p + c_cp - 1)
            odd = ((six_n-1)/2)
        
        print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}' .format(i, val, six_n-1, six_n+1, c_p, c_cp, ord_even, odd))
        #print('\n', '*'*10, 'TEST FOR n={}' .format(val), '*'*10)
        #primes_lab(1, val)

    #show_six_n(min, int(math.pow(6,max-1)))
