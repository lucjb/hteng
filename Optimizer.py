import matplotlib.pyplot as plt
import seaborn
import math
import numpy as np
from decimal import Decimal
import decimal

def e_collisions2(k, N):
	c = k -  N*(1.-math.pow((1-1./N),k))
	return c

def e_collisions(k,N):
        N = Decimal(N)
        k = Decimal(k)
        c=k-N*(1-(1-1/N)**k)
	return c


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

r = range(100000,100000000,1000000)


for i,g in enumerate([1, 2, 3]):
	solutions = []
	for k in r:
	        sol = bisect(k, MAX_N, k, g)
	        solutions.append(sol)
		print k, sol, e_collisions(k, sol), e_collisions(k, sol-1)
	z = np.polyfit(r, solutions, 2)
	p = np.poly1d(z)
	plt.plot(r, solutions, 'o', label=str(g)+' collisions')
	if i==1:
		plt.plot(r,p(r),'r-', label='Parabolic Fit')
	else:
		plt.plot(r,p(r),'r-')


plt.legend(loc=2)
plt.xlabel('Feature Space Size (k)')
plt.ylabel('Hashing Space Size (n)')
plt.yscale('log', basey=2)
plt.show()




for t in [0.1, 0.001, 0.0001]:
	solutions = []
	r = range(100000,100000000,1000000)
	for k in r:
		sol = bisect(k, MAX_N, k, k*t)
		solutions.append(sol)
	plt.plot(r, solutions, 'o')
	plt.yscale('log', basey=2)
plt.show()

