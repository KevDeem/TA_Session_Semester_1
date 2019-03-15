import matplotlib.pyplot as plt
from PIL import Image


#Global smartphone sales chart data
x = [2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
y = [423,520,674,817,991,1153,1222,1211,1597,1775,1746,1807,1879,1424,1494,1537]
 

#Making the Global Smartphone sales Graph
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
plt.title("Global Smartphone sales")
plt.xlabel("year")
plt.ylabel("Million unit sold")


#Annotations for Milestones
ax1.annotate("First year of iphone sales",xy = (2007,1153),xytext = (2005,400), arrowprops = dict(facecolor = "black", shrink = 0.05))
ax1.annotate("", xy =(2017,1500), xytext = (2016,1150), arrowprops = dict(facecolor = "black", shrink = 0.05))
ax1.annotate("", xy =(2007,1150), xytext = (2004.6,1550), arrowprops = dict(facecolor = "black", shrink = 0.05))

#Plotting the Global Sales graph
ax1.plot(x, y)

#adding axes for the pie chart and image
ax2 = fig.add_axes([0.7,0.3,0.2,0.2])
ax3 = fig.add_axes([0.2,0.7,0.13,0.13])

#Pie chart contents
iphone_samsung = [21.9,15.2,62.9]
ax2.pie(iphone_samsung, autopct='%1.1f%%')
ax2.text(1,0.4,"Samsung")
ax2.text(-1,1.1,"Apple")
ax2.text(-1.5,-1.3,"Remaining manufacutrers")

#Insert Image
images = Image.open("iphone.jpg")
ax3.imshow(images)
ax3.axis("off") #making the axis grid invisible

#Plotting the figures
fig.show()