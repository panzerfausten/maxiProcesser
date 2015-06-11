import pylab as plt
import numpy as np

class MyPlotter:
        def __init__(self,title,data,labelX,labelY,limx=None,limy=None,color='red',sounds = None,codification = None,linestyle="solid",_plotEach = None,_xTick=None,_yTick=None,_yTickMinor=None):
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
		self.plotEach = _plotEach
                self._xTick = _xTick
                self._yTick = _yTick
                self._yTickMinor = _yTickMinor
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
                if (self._yTickMinor == None):
                    self._yTickMinor = self._xTick/2.0
                if (self._xTick != None or self._yTick != None):
                    # major ticks every 200, minor ticks every 100
                    major_ticks = np.arange(0, len(self.data), self._xTick)
                    minor_ticks = np.arange(0, len(self.data), self._xTick/2.0)

                    major_ticks_y = np.arange(0, len(self.data), self._yTick)
                    minor_ticks_y = np.arange(0, len(self.data), self._yTickMinor)
                    ax.set_xticks(major_ticks)
                    ax.set_xticks(minor_ticks, minor=True)          
                    #ax.set_yticks(major_ticks_y)                
                    #ax.set_yticks(minor_ticks_y, minor=True)                 
          


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

		if(self.plotEach != None):
			for _min in range(1,len(self.data),self.plotEach):
				plt.plot([_min,_min],[0,self.limy[1]],color='g',alpha=0.3)
			plt.savefig(outputFigure)
		plt.savefig(outputFigure)
		plt.close()	
	
