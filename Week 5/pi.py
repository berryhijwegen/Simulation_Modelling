from pseudorandom import pseudo_random
from math import sqrt, pi


def calculate_pi(n):
    """
    Calculate pi using `n` random numbers
    """
    random_nums = pseudo_random(seed, n=n*2)
    half = int(n)

    nums_x = random_nums[:half]
    nums_y = random_nums[half:]

    under_1 = sum([sqrt(x**2 + y**2)<=1 for x,y in zip(nums_x, nums_y)])
    pi= 4 * under_1 / n
    return pi


if __name__ == "__main__":
    seed = 352756

    for n in [10,10**2,10**3,10**4,10**5,10**6]:
        calculated_pi = calculate_pi(n)
        error = abs(pi - calculated_pi)
        print(f"{n=:<10} {calculated_pi=:<11} {pi=:<12.6f} {error=:.6f}")
