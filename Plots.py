import matplotlib.pyplot as plt
import csv
import seaborn
import numpy as np

def e_collisions(k, N):
	c =  k-N*(1.-((N-1.)/N)**k)
	return c

def plot(prefix):
	data = csv.reader(open(prefix+'_col_log.csv'), delimiter=' ')
	x, n, c = [], [], []
	features = None
	for row in data:
		bits, features, coverage = map(float, row)
		n.append(2**bits)
		x.append(1-coverage/features)
		c.append(features-coverage)

	fig, ax1 = plt.subplots()
	ax1.set_yscale('log', basey=2)
	ax1.plot(x, n, 'b-')
	ax1.set_xlabel('% Collisions')
	ax1.set_ylabel('Hash Size', color='b')
	ax1.tick_params('y', colors='b')

	data = csv.reader(open(prefix+'_hash_log.csv'), delimiter=' ')
	l = []
	for row in data:
		bits, loss = map(float, row)
		l.append(loss)

	for i, v in enumerate(l):
		l[i] = 1-v/l[-1]

	ax2 = ax1.twinx()
	ax2.plot(x, l, 'r-')
	ax2.set_ylabel('logloss', color='r')
	ax2.tick_params('y', colors='r')

	fig.tight_layout()
	plt.savefig('article/'+prefix+'_impact.png')
	plt.clf()

	ec = []
	for ni in n:
		ec.append(e_collisions(features, ni))
	plt.plot(c, ec, 'o')

	z = np.polyfit(c, ec, 1)
	p = np.poly1d(z)
	plt.plot(c,p(c),'r-')
	#print 'y=%.6fx+(%.6f)'%(z[0],z[1])

	plt.show()

plot('avazu')
plot('booking')
plot('criteo')
