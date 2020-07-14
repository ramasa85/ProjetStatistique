from random import random
from scipy.special import binom
import matplotlib.pyplot as plt

import random
import loi_binomiale
from math import sqrt, exp, pi

def rand_bernoulli(p):
 x = random.random()
 if x <= p: return 1
 else: return 0
print([rand_bernoulli(0.2) for k in range(10000)])

def rand_binomial(n, p):
 s = 0
 for k in range(n):
     s = s + rand_bernoulli(p)
     return s

def power_down(n, k):
 p = 1
 for j in range(k): p = p * (n - j)
 return p


def factorial(n):
    return power_down(n, n)

def binomial(n, k):
 return power_down(n, k) // factorial(k)

def binom_law(n, p, k):
 return binomial(n, k) * p ** k * (1 - p) ** (n - k)

def histogramme(s):
 m = max(s)
 h = (m + 1) * [0]
 c = 0
 for k in s:
     h[k] = h[k] + 1
     c = c + 1
 for i in range(len(h)): h[i] = h[i] / c
 return h

n, p = 30, 0.2
s = [rand_binomial(n, p) for k in range(10000)]
#plt.axis([0,n,0,0.2])
plt.plot(histogramme(s), 'ko')
s1 = [binom_law(n, p, k) for k in range(0, n + 1)]
plt.grid()
plt.plot(s1, 'r-')
plt.show()
