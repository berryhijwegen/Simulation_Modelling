import sys
sys.path.append('../Week 5')
from pseudorandom import pseudo_random
from numpy import arange
import matplotlib.pyplot as plt


import math
def normpdf(x, mean, sd):
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom



n = 10000
x               =   [x for x in arange(-10, 11, 1)]
prob            =   [normpdf(y, 0, 3) for y in x]
prob            =   [x/sum(prob) for x in prob]
random_numbers  = pseudo_random(84338064, n=n)

def weighted_choice(weights, index):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random_numbers[index] * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            return i

random_numbers = [x[weighted_choice(prob, i)] for i in range(n)]            
plt.hist(random_numbers, bins = len(x))
plt.savefig('plots/plot.png')
plt.show()