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
		self.detect()
		self.peaks = []
	def removeDuplicates(self,seq):
		seen = set()
		seen_add = seen.add
		return [ x for x in seq if not (x in seen or seen_add(x))]
	def detect(self):
		self._gaussianData = gaussian_filter(self._data,1)
		self._peakind = signal.find_peaks_cwt(self._gaussianData, np.arange(1,2))
		self._peakind = self.removeDuplicates(self._peakind)
	def plot(self,figname):
		fig, ax = plt.subplots()
                index = np.arange(len (self._gaussianData))
                ax.plot(self._gaussianData)
		for _i, _p in enumerate(self._peakind):
			if(_i < len(self._peakind) and _i > 0):
				
				#print "peak",self._gaussianData[_p], self._gaussianData [ self._peakind [_i-1  ]]
				_diff = self._gaussianData[_p] - self._gaussianData[self._peakind [_i-1  ]]
				#Calculate only data within the threshold
				if(_diff > 0.04): #
					#calculateRaisingTime
					_limLeft = self._peakind[_i-1]
					_limRight = self._peakind[_i]
					_segmentToSearchRaisingTime = self._gaussianData[_limLeft:_limRight].tolist()
					_raisingPoint = _segmentToSearchRaisingTime.index(min(_segmentToSearchRaisingTime))
					_c = self._peakind[_i-1] + _raisingPoint

					#Calculate amplitude and rising time
					_amplitude = self._gaussianData[_p] - self._gaussianData[_c]
					_risingTime = _p - _c

					_currentPeak = self._peakind[_i]
					#calculateHalfRecoveryTime
					if ( _i < len(self._peakind)-1):
						_nextPeak = self._peakind[_i+1]
						#print "HR_peak",_currentPeak,_nextPeak
						_segmentToSearchHalfRecoveryTime = self._gaussianData[_currentPeak:_nextPeak]
					else:
						_segmentToSearchHalfRecoveryTime = self._gaussianData[_currentPeak:]
						
			
					_halfAmplitude = _amplitude / 2.0
					_halfRecoveryTime = None
					_hrtPointValue = None
					for _x,_val in enumerate(_segmentToSearchHalfRecoveryTime):
						_valueAtPeak = self._gaussianData[_currentPeak]
						_ampliDiff = _valueAtPeak - _halfAmplitude
						if( _val - _ampliDiff < 0.00000000000000001): #Now with Zero* diff!
							#print "hrt",_currentPeak,_ampliDiff, _x + _currentPeak
							_hrtPoint = _currentPeak +_x
							_hrtPointValue = self._gaussianData[_hrtPoint]
							ax.scatter(  _hrtPoint  , self._gaussianData[_hrtPoint],color='m',marker="x")
							_halfRecoveryTime = _hrtPoint - _currentPeak
							break # we ain't no need your data dawg
					ax.scatter(  _p , self._gaussianData[_p],color='r' )
					ax.scatter(  _c,self._gaussianData[_c],color='y')
					_peakData = [_p,_amplitude,_risingTime,str(_halfRecoveryTime),str(_hrtPointValue)]
					self.peaks.append(_peakData)
					#print "amplitude",_amplitude
					#print "rise time",_risingTime
					#print "peakIndex",_p
					#print "HRTPeak: #%f, Amplitude: %f, Raise Time: %f, HRT: %s, ValAtHRT:%s" \
					#	%(_p,_amplitude,_risingTime,str(_halfRecoveryTime),str(_hrtPointValue))
			else:
				ax.scatter(  _p , self._gaussianData[_p],color='g' )
		plt.grid(True)
		plt.show()
		plt.ylim(self.limy)
                plt.xlim(self.limx)

		plt.savefig(figname,dpi=450)
		
