import pylab as plt
import numpy as np

class MyPlotter:
        def __init__(self,title,data,labelX,labelY,limx=None,limy=None,color='red'):
                self.data = data
                self.title = title
		self.labelX = labelX
		self.labelY = labelY
		self.limy = limy
		self.limx = limx
		self.color = color

        def plot(self,outputFigure):
                #init the plot
                fig, ax = plt.subplots()
                index = np.arange(len (self.data))
                bar_width = 1
                ax.plot(self.data,color=self.color)
                #ax.set_ylabel("%s value" %(self.e3data.dataType))
                ax.set_xlabel(self.labelX)
                ax.set_ylabel(self.labelY)
                ax.set_title(self.title)
		plt.ylim(self.limy)
		plt.xlim(self.limx)
                plt.grid(True)
                plt.savefig(outputFigure)
		plt.close()	
	
