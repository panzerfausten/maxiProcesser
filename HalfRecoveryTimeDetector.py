from scipy import signal
import numpy as np
import pylab as plt
from  scipy.ndimage.filters import gaussian_filter
import json
class HalfRecoveryTimeDetector:
	def __init__(self,_data,_segment=None):
		self._data = self.removeNones(_data)
		self._segment = _segment
		self._peaks = []
		self.detect()
		self._xlim = None
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
	def plot(self,figname,_ylim=None):
		fig, ax = plt.subplots()
                index = np.arange(len (self._gaussianData))
		plt.grid(True)
                plt.plot(self._gaussianData) #plot the processed data
            
		#set axis. Nazi axis?
		ax.set_ylabel("uS")
                ax.set_xlabel("Seconds")
                ax.set_title("Peak and Half Time Recovery detection")
                # major ticks every 200, minor ticks every 100
                major_ticks = np.arange(0, len(self._data), 200)                                              
                minor_ticks = np.arange(0, len(self._data), 100)     

                major_ticks_y = np.arange(0, len(self._data), 1)                                              
                minor_ticks_y = np.arange(0, len(self._data), 0.5)     
                ax.set_xticks(major_ticks)                                                       
                ax.set_xticks(minor_ticks, minor=True)                                           
                ax.set_yticks(major_ticks_y)                                                       
                ax.set_yticks(minor_ticks_y, minor=True)                                           

                # and a corresponding grid                                                       
                
                ax.grid(which='both')                                                            

                # or if you want differnet settings for the grids:                               
                ax.grid(which='minor', alpha=0.2)                                                
                ax.grid(which='major', alpha=0.5)    
                if (_ylim == None):
			_ylim = [0,6]
		plt.ylim(_ylim)
		plt.xlim(self._xlim)
		for _p in self._peaks:
			#overplot rising point and peak
			plt.plot(  int(_p["peakIndex"]) , self._gaussianData[int(_p["peakIndex"])],color='r',marker="o",markersize=5 )
			plt.plot(  _p["risingTimeIndex"],self._gaussianData[_p["risingTimeIndex"]],color='y',marker="o",markersize=5)
			#overplot the HRT
			if _p["halfRecoveryIndex"] != None:
				plt.plot(  int(_p["halfRecoveryIndex"])  , self._gaussianData[ int(_p["halfRecoveryIndex"]) ],color='m',marker="x",markersize=5)

		#save it! Because.. humans
		plt.savefig(figname,dpi=450)
        def toJson(self):
            return json.dumps(self._peaks)
        def toCSV(self):
            for _peak in self._peaks:
                    _valsToPrint = []
                    for _val in _peak:
                        _valsToPrint.append(str(_peak[_val]))
                    print ",".join(_valsToPrint)

