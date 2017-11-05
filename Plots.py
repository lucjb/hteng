import matplotlib.pyplot as plt
import csv
import seaborn

def plot(prefix):
	data = csv.reader(open(prefix+'_col_log.csv'), delimiter=' ')
	x, y = [], []
	for row in data:
		bits, features, collisions = map(float, row)
		y.append(2**bits)
		x.append(1-collisions/features)


	fig, ax1 = plt.subplots()
	ax1.set_yscale('log', basey=2)
	ax1.plot(x, y, 'b-')
	ax1.set_xlabel('% Collisions')
	ax1.set_ylabel('Hash Size', color='b')
	ax1.tick_params('y', colors='b')


	data = csv.reader(open(prefix+'_hash_log.csv'), delimiter=' ')
	y = []
	for row in data:
		bits, loss = map(float, row)
		y.append(loss)

	ax2 = ax1.twinx()
	ax2.plot(x, y, 'r-')
	ax2.set_ylabel('logloss', color='r')
	ax2.tick_params('y', colors='r')

	fig.tight_layout()
	plt.show()

plot('avazu')
plot('booking')
