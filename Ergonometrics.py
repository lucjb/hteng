import matplotlib.pyplot as plt
import random
import string

def e_collisions(k, N):
	u =  N*(1.-((N-1.)/N)**k)
	c = k-u
	if c < 0:
		c = 0
	return c



def random_key():
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))

def sim_collisions(k, N):
	keys = [random_key() for _ in range(k)]
	buckets = set()
	for key in keys:
		buckets.add(hash(key)%N)
	return k-len(buckets)

def avg_collisions(k, N):
	x = []
	for _ in range(100):
	        x.append(sim_collisions(k, N))
	return sum(x)/float(len(x))

for b in range(18,30):
	print b, e_collisions(39752014, 2**b)

sim = []
calc = []
for k in range(1, 1000, 100):
	for N in range(k, k+100, 10):
		s = avg_collisions(k, N)
		e = e_collisions(k, N)
		sim.append(s)
		calc.append(e)
		print s, e
plt.scatter(sim, calc)
plt.show()


solutions = [0]



r = range(1, 10000, 100)
for k in r:
	if k == 0:
		continue
	N = k
	colisions=k
	while colisions>0.1:
		colisions = e_collisions(k, N)
		N+=1
	print k, N, colisions, sim_collisions(k, N)
	solutions.append(N)

plt.scatter(r, solutions)
plt.show()
