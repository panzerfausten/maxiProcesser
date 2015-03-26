import pylab as plt
import numpy as np

class MyPlotter:
        def __init__(self,title,data,labelX,labelY,limx=None,limy=None,color='red',sounds = None):
                self.data = data
                self.title = title
		self.labelX = labelX
		self.labelY = labelY
		self.limy = limy
		self.limx = limx
		self.color = color
		self.sounds = sounds

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
		#for _i,_d in enumerate(self.data):
		#	if (_d != None):
		#		ax.fill_between([_i], 0, _d,color="green")
		if (self.sounds != None):
			print self.sounds
			print len(self.data)
			print self.data
			for _s in self.sounds:
				try:
					plt.plot( (_s,_s),(0,self.data[int(_s)]), color="green")
				except:
					pass
		plt.ylim(self.limy)
		plt.xlim(self.limx)
                plt.grid(True)
                plt.savefig(outputFigure)
		plt.close()	
	
