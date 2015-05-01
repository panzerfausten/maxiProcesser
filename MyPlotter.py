import pylab as plt
import numpy as np

class MyPlotter:
        def __init__(self,title,data,labelX,labelY,limx=None,limy=None,color='red',sounds = None,codification = None,linestyle="solid"):
                self.data = data
                self.title = title
		self.labelX = labelX
		self.labelY = labelY
		self.limy = limy
		self.limx = limx
		self.color = color
		self.sounds = sounds
		self.codification = codification 
		self.linestyle = linestyle
        def plot(self,outputFigure):
                #init the plot
                fig, ax = plt.subplots()
                index = np.arange(len (self.data))
                bar_width = 1
                ax.plot(self.data,color=self.color,linestyle=self.linestyle)
                #ax.set_ylabel("%s value" %(self.e3data.dataType))
                ax.set_xlabel(self.labelX)
                ax.set_ylabel(self.labelY)
                ax.set_title(self.title)


		#for _i,_d in enumerate(self.sounds):
		#	if (_d != None):
		#		ax.fill_between([_i], 0, _d,color="green")


		if (self.codification != None):
			for _i,_c in enumerate(self.codification):
				if(_c[2] == "t"):
					ax.axvspan(_c[0],_c[1],color="green",alpha=0.3)
				if(_c[2] == "w"):
					ax.axvspan(_c[0],_c[1],color="blue",alpha=0.3)
				if(_c[2] == "e"):
					ax.axvspan(_c[0],_c[1],color="yellow",alpha=0.3)
		if (self.sounds != None):
			for _s in self.sounds:
				try:
					plt.plot( (_s,_s),(0,self.data[int(_s)]), color="green")
				except:
					print "Error"
					pass
		plt.ylim(self.limy)
		plt.xlim(self.limx)
                plt.grid(True)
                plt.savefig(outputFigure)
		plt.close()	
	
