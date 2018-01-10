import matplotlib.pyplot as plt
import seaborn
import math
import numpy as np
from decimal import Decimal

def e_collisions(k,N):
        N = Decimal(N)
        k = Decimal(k)
	c = k*(1-(1-1/N)**(k-1))
	return c

def compute(k, x):
	return k**2/x

def exact(k, c):
        k = Decimal(k)
	c = Decimal(c)
	return float(-1/((1-c/k)**(1/(k-1))-1))

def bisect(a, b, k, x):
	while a<b:
		n = (a+b)//2
		fn = e_collisions(k,n)
		if fn>x:
			a = n+1
		else:
			b = n
	return a

def scan(a, b, k, x):
	n = k
	while e_collisions(k, n)>x:
		 n+=1
	return n


k, MAX_N, x = 100, 2**70, 0.5
sol = bisect(k, MAX_N, k, x)
print MAX_N, e_collisions(k, MAX_N)
print sol, e_collisions(k, sol)


r = range(100000,1000000,20000)

fig, ax = plt.subplots()
for i,g in enumerate([1, 2, 3]):
        solutions, w = [], []
        for k in r:
                sol = bisect(k, MAX_N, k, g)
                solutions.append(exact(k,g))
		w.append(exact(k,g))
                print k, sol, e_collisions(k, sol), e_collisions(k, sol-1), e_collisions(k, exact(k,g))
        z = np.polyfit(r, solutions, 2)
        p = np.poly1d(z)
        plt.plot(r, solutions, 'o', label=str(g)+' collisions')
        plt.plot(r,p(r),'r-')

plt.plot(r,p(r),'r-', label='Parabolic Fit')

plt.legend(loc=2)
plt.xlabel('Feature Space Size (k)')
plt.ylabel('Hashing Space Size (n)')
plt.savefig('article/parabolas.png')

plt.clf()
plt.plot(solutions, w, 'o')
z = np.polyfit(solutions, w, 1)
p = np.poly1d(z)
plt.plot(solutions, p(solutions), 'r-')
plt.xlabel('Exact hash size according to Bisection')
plt.ylabel('Hash size according to Approximation')
plt.savefig('article/bisection_vs_approximation.png')

