import matplotlib.pyplot as plt
import csv
import seaborn
import numpy as np

def e_collisions(k, N):
	c =  k-N*(1.-((N-1.)/N)**k)
	return c

def plot_model():
	fig = plt.figure(figsize=(12,4))
	for i, prefix in enumerate(['avazu', 'booking', 'criteo']):
		ax = fig.add_subplot(1,3,i+1)

	        data = csv.reader(open(prefix+'_col_log.csv'), delimiter=' ')
	        n, c = [], []
	        features = None
	        for row in data:
	                bits, features, coverage = map(float, row)
	                n.append(2**bits)
	                c.append(features-coverage)
	        ec = []
	        for ni in n:
	                ec.append(e_collisions(features, ni))
	        ax.plot(ec, c, 'o')

	        z = np.polyfit(c, ec, 1)
	        p = np.poly1d(z)
		if i == 1:
		        ax.set_xlabel('Expected Collisions according to the formula')
	        if i == 0:
			ax.set_ylabel('Actually observed collisiions')
		ax.plot(c,p(c),'r-', label='Linear Fit')
		if i == 0:
			ax.legend(loc=2)
		ax.set_title(prefix)
	        #plt.annotate('y=%.6fx+(%.6f)'%(z[0],z[1]), xy=(0,0), xycoords='data')
	plt.tight_layout()
        plt.savefig('article/'+prefix+'_model_fit.png')


def plot_impact(prefix):
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
	ax1.plot(x, n, 'bo-')
	ax1.set_xlabel('% Collisions')
	ax1.set_ylabel('Hash Size (n)', color='b')
	ax1.tick_params('y', colors='b')

	data = csv.reader(open(prefix+'_hash_log.csv'), delimiter=' ')
	l = []
	for row in data:
		bits, loss = map(float, row)
		l.append(loss)

	ax2 = ax1.twinx()
	ax2.plot(x, l, 'ro-')
	ax2.set_ylabel('logloss', color='r')
	ax2.tick_params('y', colors='r')

	fig.tight_layout()
	plt.savefig('article/'+prefix+'_impact.png')

plot_model()
plot_impact('avazu')
plot_impact('booking')
plot_impact('criteo')
