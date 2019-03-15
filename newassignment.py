import numpy as np
import matplotlib.pyplot as pl


x = list()
fig = pl.figure()
for i in range(1,26):
	number = np.random.rand()
	if number > 0.5:
		x.append(1)
		fig.add_subplot(5,5,i).set_facecolor('red')
	if number <= 0.5:
		x.append(0)
		fig.add_subplot(5,5,i)

print(x)
pl.show()
