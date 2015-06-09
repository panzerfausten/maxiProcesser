from scipy import signal
import numpy as np
import pylab as plt
from  scipy.ndimage.filters import gaussian_filter
class HalfRecoveryTimeDetector:
	def __init__(self,_data,_segment=None):
		self._data = self.removeNones(_data)
		self._segment = _segment
		self._peaks = []
		self.detect()
	def removeNones(self,_data):
		return filter(lambda x: x!=None, _data)
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
					_peakValue = self._gaussianData[_p]
					#Calculate amplitude and rising time
					_amplitude = self._gaussianData[_p] - self._gaussianData[_c]
					_risingTime = _p - _c
					_risingTime = _p - _risingTime
					_risingTimeValue = self._gaussianData[_risingTime]
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
					_hrtPointIndex = None
					_halfRecoveryIndex = None
					#And find the right HRT
					for _x,_val in enumerate(_segmentToSearchHalfRecoveryTime):
						_valueAtPeak = self._gaussianData[_currentPeak]
						_ampliDiff = _valueAtPeak - _halfAmplitude
						if( _val - _ampliDiff < 0.00000000000000001): #Now with Zero* diff!
							_hrtPointIndex = _currentPeak +_x
							_hrtPointValue = self._gaussianData[_hrtPointIndex]
							_halfRecoveryTime = _hrtPointIndex #+ _currentPeak
							break # we ain't no need your data dawg
					
					#Pack everything up!
					_halfRecoveryIndex = _hrtPointIndex
					_peakData = { "peakIndex": _p,"peakValue": _peakValue,	
						"risingTimeIndex":_risingTime,"risingTimeValue": _risingTimeValue,"halfRecoveryIndex":_halfRecoveryIndex,
						"halfRecoveryValue":_hrtPointValue, "distanceToPrevPeak": None}
					self._peaks.append(_peakData)

				#Aaand do some more math
				self.calculateDistances()
	def calculateDistances(self):
		if (self._peaks != None):
			for  _i, _peak in enumerate(self._peaks):
				if ( _i > 0):
					_peak["distanceToPrevPeak"] = _peak["peakIndex"] - self._peaks[_i-1]["peakIndex"]
					
		else:
			raise Exception("You must to call detect() first")
	def plot(self,figname):
		fig, ax = plt.subplots()
                index = np.arange(len (self._gaussianData))
                ax.plot(self._gaussianData) #plot the processed data
		plt.grid(True)
		plt.show()

		#set axis. Nazi axis?
		ax.set_ylabel("uS")
                ax.set_xlabel("Seconds")
                ax.set_title("Peak and Half Time Recovery detection")

		for _p in self._peaks:
			#scatter rising point and peak
			plt.scatter(  _p["peakIndex"] , self._gaussianData[_p["peakIndex"]],color='r' )
			plt.scatter(  _p["risingTimeIndex"],self._gaussianData[_p["risingTimeIndex"]],color='y')
			#scatter the HRT
			if _p["halfRecoveryIndex"] != None:
				plt.scatter(  int(_p["halfRecoveryIndex"])  , self._gaussianData[ int(_p["halfRecoveryIndex"]) ],color='m',marker="x")

		#save it! Because.. humans
		plt.savefig(figname,dpi=450)
