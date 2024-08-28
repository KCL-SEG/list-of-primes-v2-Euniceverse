"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    list = []
    i = 2
    
    while(len(list) < number_of_primes): 
        is_prime = True
        for y in range(2,int(i ** 0.5) + 1):
                if i%y == 0:
                    is_prime = False
                    break
        if is_prime:
            list.append(i)
        i += 1
    return list
