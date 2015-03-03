import pylab as plt
import numpy as np

class MyPlotter:
        def __init__(self,title,data):
                self.data = data
                self.title = title

        def plot(self,outputFigure):
                #init the plot
                fig, ax = plt.subplots()
                index = np.arange(len (self.data))
                bar_width = 1
                ax.plot(self.data,color='red')
                #ax.set_ylabel("%s value" %(self.e3data.dataType))
                ax.set_xlabel("X")
                ax.set_xlabel("Values")
                ax.set_title(self.title)
                plt.grid(True)
                plt.savefig(outputFigure)

