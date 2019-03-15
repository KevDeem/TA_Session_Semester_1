#MARCELL ALVIANTO
# 2201797544

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


t = [2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
xsales = [423,520,674,817,991,1153,1222,1211,1597,1775,1746,1807,1879,1424,1495,1537]

fig = plt.figure(1); plt.clf()
ax1 = fig.add_subplot(1,1,1);

ax1.plot(t, xsales)


plt.annotate('Second year of Iphone sales', xy=(2008,1222), xytext=(2002,400),
             arrowprops = dict(facecolor = 'black', shrink = 0.05),
             )
plt.annotate('Iphone and Samsung Market Share', xy=(2014,1879), xytext=(2012,1200),
             arrowprops = dict(facecolor = 'black', shrink = 0.05),
             )
plt.annotate('', xy=(2009.6,1400), xytext=(2014.7,950),
             arrowprops = dict(facecolor = 'black', shrink = 0.05),
             )

plt.annotate('', xy=(2007,1200), xytext=(2005,1600),
             arrowprops = dict(facecolor = 'black', shrink = 0.05),
             )

#PIE CHART
ipsam = [15,30,55]
ax2 = fig.add_axes([0.7,0.2,0.2,0.2])
ax2.pie(ipsam, autopct = '%1.1f%%')
ax2.text(1,0.1,"iphone")
ax2.text(-1,0.9,"Samsung")
ax2.text(-1,-1,"Remaining")

ax3 = fig.add_axes([0.2,0.7,0.13,0.13])
images = Image.open("iphone.png")
images.load()
ax3.imshow(images)
ax3.axis('off')

ax1.set_xlabel("Year")
ax1.set_ylabel("Million units sold")
ax1.set_title("Global Smartphone Sales")

fig.show()

