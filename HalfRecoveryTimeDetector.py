from scipy import signal
import numpy as np
import pylab as plt
from  scipy.ndimage.filters import gaussian_filter
class HalfRecoveryTimeDetector:
	def __init__(self,_data,_segment=None):
		self._data = _data
		self._segment = _segment
		self.limy = [0,5]
		self.limx = [0,len(_data)]
		self._peaks = []
		self.detect()

	def detect(self):
		#find all the peaks
		self._gaussianData = gaussian_filter(self._data,1)
                index = np.arange(len (self._gaussianData))
		self._peakind = signal.find_peaks_cwt(self._gaussianData, np.arange(1,2))

		#And then filter the right peaks
		for _i, _p in enumerate(self._peakind):
			if(_i < len(self._peakind) and _i > 0):
				_diff = self._gaussianData[_p] - self._gaussianData[self._peakind [_i-1  ]]

				#Calculate only data within the threshold
				if(_diff > 0.04): #this threshold looks good. Dayum!

					#calculate segments to search amplitude and rising time
					_limLeft = self._peakind[_i-1]
					_limRight = self._peakind[_i]
					_segmentToSearchRaisingTime = self._gaussianData[_limLeft:_limRight].tolist()
					_raisingPoint = _segmentToSearchRaisingTime.index(min(_segmentToSearchRaisingTime))
					_c = self._peakind[_i-1] + _raisingPoint

					#Calculate amplitude and rising time
					_amplitude = self._gaussianData[_p] - self._gaussianData[_c]
					_risingTime = _p - _c
					_currentPeak = self._peakind[_i]

					#calculate segment to search the Half Recovery Time
					if ( _i < len(self._peakind)-1):
						_nextPeak = self._peakind[_i+1]
						_segmentToSearchHalfRecoveryTime = self._gaussianData[_currentPeak:_nextPeak]
					else:
						_segmentToSearchHalfRecoveryTime = self._gaussianData[_currentPeak:]
					
					#calculate the half amplitude	
					_halfAmplitude = _amplitude / 2.0
					_halfRecoveryTime = None
					_hrtPointValue = None
					#And find the right HRT
					for _x,_val in enumerate(_segmentToSearchHalfRecoveryTime):
						_valueAtPeak = self._gaussianData[_currentPeak]
						_ampliDiff = _valueAtPeak - _halfAmplitude
						if( _val - _ampliDiff < 0.00000000000000001): #Now with Zero* diff!
							_hrtPoint = _currentPeak +_x
							_hrtPointValue = self._gaussianData[_hrtPoint]
							_halfRecoveryTime = _hrtPoint #+ _currentPeak
							break # we ain't no need your data dawg
					_risingTime = _p - _risingTime
					
					#Pack everything up!
					_peakData = [_p,_amplitude,_risingTime,_halfRecoveryTime,_hrtPointValue]
					self._peaks.append(_peakData)
					#print "HRTPeak: #%f, Amplitude: %f, Raise Time: %f, HRT: %s, ValAtHRT:%s" \
					#	%(_p,_amplitude,_risingTime,str(_halfRecoveryTime),str(_hrtPointValue))
			else:
				pass
	def plot(self,figname):
		fig, ax = plt.subplots()
                index = np.arange(len (self._gaussianData))
                ax.plot(self._gaussianData) #plot the processed data
		plt.grid(True)
		plt.show()
		#set axis. Nazi axis?
		plt.ylim(self.limy)
                plt.xlim(self.limx)

		for _p in self._peaks:
			#scatter rising point and peak
			ax.scatter(  _p[0] , self._gaussianData[_p[0]],color='r' )
			ax.scatter(  _p[2],self._gaussianData[_p[2]],color='y')
			#scatter the HRT
			if _p[3] != None:
				ax.scatter(  int(_p[3])  , self._gaussianData[ int(_p[3]) ],color='m',marker="x")

		#save it! Because.. humans
		plt.savefig(figname,dpi=450)
