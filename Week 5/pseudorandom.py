import math

def pseudo_random(seed, n=10, m=2**32, a=1103515245, c=12345):
    """
    generate random list of `n` numbers
    """
    if not check_rules(m,c,a):
        print('No full period')
        return False

    lst = []
    for _ in range(n):
        seed = (a*seed + c) % m
        lst.append(seed / m)
    
    if n == 1:
        return lst[0]
    return lst

def check_rules(m, c, a):
    """
    Check rules to guarantee full period
    """
    return no_common_divisor(m,c) and check_prime_factors(a,m) and m_4(a,m)

def no_common_divisor(m,c):
    """
    Check if `m` and `c` have no common divisors (except 1).
    """
    return not any([m % i == c % i == 0 for i in range(2, min(m, c)+1)])

def check_prime_factors(a, m):
    """
    Check if `a` = 1 (mod r) if r is a prime factor of `m`.
    """
    prime_factors = get_prime_factors(m)
    return not any([a % prime_factor != 1 for prime_factor in prime_factors])

def m_4(a,m):
    """
    If `m` is a multiple of 4, check if `a` = 1 (mod 4).
    """
    if m % 4 == 0:
        return a % 4 == 1
    return True

def get_prime_factors(x):  
    """
    Get all prime factors of given number `x`
    """ 
    primes = []   

    while x % 2 == 0: 
        primes.append(2)
        x = x / 2
          
    for i in range(3,int(math.sqrt(x))+1,2): 
        while x % i== 0: 
            primes.append(i)
            x = x / i 
              
    if x > 2: 
        primes.append(x)
    
    return primes

if __name__ == '__main__':
    import seaborn as sns
    import matplotlib.pyplot as plt

    for n in [10, 10**2, 10**3, 10**4, 10**5, 10**6]:
        x = pseudo_random(345345345, n=n)
        sns.distplot(x)
        plt.savefig(f"./plots/distribution_{n}")
        plt.close()