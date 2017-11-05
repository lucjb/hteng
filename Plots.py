import matplotlib.pyplot as plt
import csv


def plot(file_name):
	data = csv.reader(open(file_name), delimiter='\t')
	x, y = [], []
	for row in data:
		collisions, logloss = map(float, row)
		x.append(collisions)
		y.append(logloss)

	plt.scatter(x,y)


plot('booking.csv')
plot('criteo.csv')

plt.show()
