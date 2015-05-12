from scipy import signal
import numpy as np
import pylab as plt
from  scipy.ndimage.filters import gaussian_filter
class HalfRecoveryTimeDetector:
	def __init__(self,_data,_segment=None):
		self._data = _data
		self._segment = _segment
		self.detect()
	def detect(self):
		self._gaussianData = gaussian_filter(self._data,1)
		self._peakind = signal.find_peaks_cwt(self._gaussianData, np.arange(1,2))
	def plot(self,figname):
		fig, ax = plt.subplots()
                index = np.arange(len (self._gaussianData))
                ax.plot(self._gaussianData)
                #ax.plot(self._data)
		for _i, _p in enumerate(self._peakind):
			if(_i < len(self._peakind) and _i > 0):
				
				print "peak",self._gaussianData[_p], self._gaussianData [ self._peakind [_i-1  ]]
				_diff = self._gaussianData[_p] - self._gaussianData[self._peakind [_i-1  ]]
				print "diff ->",abs(_diff)
				if(_diff > 0.04): #
					ax.scatter(  _p , self._gaussianData[_p],color='r' )
			else:
				ax.scatter(  _p , self._gaussianData[_p],color='g' )
		plt.grid(True)
		plt.show()
		plt.savefig(figname,dpi=450)
		
