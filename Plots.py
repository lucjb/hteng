import matplotlib
import matplotlib.pyplot as plt
import csv
import seaborn
import numpy as np

def e_collisions(k, N):
	c = k*(1-(1-1./N)**(k-1))
	#c =  k-N*(1.-((N-1.)/N)**k)
	return c

def plot_model():
	fig = plt.figure(figsize=(12,4))
	size = fig.get_size_inches()*fig.dpi # size in pixels
	print size, fig.get_size_inches(), fig.dpi
	for i, prefix in enumerate(['avazu', 'booking', 'criteo']):
		ax = fig.add_subplot(1,3,i+1)

	        data = csv.reader(open(prefix+'_col_log.csv'), delimiter=' ')
	        n, c = [], []
	        features = None
		all_collided_counter = 0
	        for row in data:
	                bits, features, collisions = map(float, row)
			if collisions==features:
				all_collided_counter+=1
	                n.append(2**bits)
	                c.append(collisions)
		n = n[all_collided_counter-1:]
		c = c[all_collided_counter-1:]
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
		ax.set_title(prefix, fontsize=16)
		ax.xaxis.label.set_size(16)
		plt.setp(ax.get_xticklabels(),fontsize=16, rotation=45)
                plt.setp(ax.get_yticklabels(),fontsize=16)

	        #plt.annotate('y=%.6fx+(%.6f)'%(z[0],z[1]), xy=(0,0), xycoords='data')
	plt.tight_layout()
        plt.savefig('article/model_fit.png')


def plot_impact(prefix):
	data = csv.reader(open(prefix+'_col_log.csv'), delimiter=' ')
        loss_data = csv.reader(open(prefix+'_hash_log.csv'), delimiter=' ')
        l = []
	g = 0
	x, n, c = [], [], []
	features = None
	for row in data:
		loss_row = loss_data.next()
                bits, loss = map(float, loss_row)
		bits, features, collisions = map(float, row)
		if collisions == features:
			g+=1
		l.append(loss)
		n.append(2**bits)
		x.append(collisions/features)
		c.append(collisions)
	
	x = x[g-1:]
	l = l[g-1:]
	n = n[g-1:]
	c = c[g-1:]
	fig, ax1 = plt.subplots()
	ax1.set_yscale('log', basey=2)
	ax1.plot(x, n, 'bo-')
	ax1.set_xlabel('% Collisions')
	ax1.set_ylabel('Hash Size (n)', color='b')
	ax1.tick_params('y', colors='b')

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
