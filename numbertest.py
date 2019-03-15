import numpy as np
import matplotlib.pyplot as plt


x = np.array([])
for i in range(501):
	x = np.append(x,np.random.randn())



xMean = x.mean()
xStd = np.std(x, ddof = 1)
n = 501

fig = plt.figure(10); plt.clf()
ax = fig.add_subplot(1,1,1)
ax.hist(x, rwidth = 0.8)
ax.plot(x, 5*np.random.randn(n) - 20, ".")
ax.boxplot(x, vert = False, widths = 10, positions = [-50])
ax.errorbar(0, -75,xMean,xStd, capsize = 5)
ax.plot(xMean,-75,"sk")
ax.set_ylim(-100,300)



fig.show()