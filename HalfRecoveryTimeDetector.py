from scipy import signal
import numpy as np
import pylab as plt
from  scipy.ndimage.filters import gaussian_filter
from sklearn import preprocessing
import json
class HalfRecoveryTimeDetector:
	def __init__(self,_data,_segment=None):
		self._data = self.removeNones(_data)
		self._segment = _segment
		self._peaks = []
                self.normalize()
		self.detect()
		self._xlim = None
	def removeNones(self,_data):
		return filter(lambda x: x!=None, _data)
        def normalize(self):
            min_max_scaler = preprocessing.MinMaxScaler()
            self._data = min_max_scaler.fit_transform(self._data)
	def detect(self):
		#find all the peaks
		self._gaussianData = gaussian_filter(self._data,1)
                index = np.arange(len (self._gaussianData))
		self._peakind = signal.find_peaks_cwt(self._gaussianData, np.arange(1,2))
                #if we have no data, then create this empty data
                if( len(self._peakind) == 0):
                         _peakData = { "peakIndex": None,"peakValue": None,
                                                "risingTimeIndex":None,"risingTimeValue": None,"halfRecoveryIndex":None,
                                                "halfRecoveryValue":None, "distanceToPrevPeak": None, "peakAmplitude":None}
                         self._peaks.append(_peakData)
		#And then filter the right peaks
		for _i, _p in enumerate(self._peakind):
			if(_i < len(self._peakind) and _i > 0):
				_diff = self._gaussianData[_p] - self._gaussianData[self._peakind [_i-1  ]]

				#Calculate only data within the threshold
				if(True): #this threshold looks good. Dayum!

					#calculate segments to search amplitude and rising time
					_limLeft = self._peakind[_i-1]
					_limRight = self._peakind[_i]
					_segmentToSearchRaisingTime = self._gaussianData[_limLeft:_limRight].tolist()
					_raisingPoint = _segmentToSearchRaisingTime.index(min(_segmentToSearchRaisingTime))
					_c = self._peakind[_i-1] + _raisingPoint
					_peakValue = self._gaussianData[_p]
					#Calculate amplitude and rising time
					_amplitude = self._gaussianData[_p] - self._gaussianData[_c]
                                        if(_amplitude > 0.01):
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
                                                    "halfRecoveryValue":_hrtPointValue, "distanceToPrevPeak": None, "peakAmplitude": _peakValue - _risingTimeValue  }
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
	def plot(self,figname,_ylim=None,_xlim=None,_xTick=200,_xMinorTick=100):
		fig, ax = plt.subplots()
                index = np.arange(len (self._gaussianData))
		plt.grid(True)
                plt.plot(self._gaussianData) #plot the processed data
            
		#set axis. Nazi axis?
		ax.set_ylabel("uS")
                ax.set_xlabel("Seconds")
                ax.set_title("GSR: Peak and Half Time Recovery detection")
                # major ticks every 200, minor ticks every 100
                major_ticks = np.arange(0, len(self._data), _xTick)                                              
                minor_ticks = np.arange(0, len(self._data), _xMinorTick)     

                major_ticks_y = np.arange(0, 1.1, 0.2)                                              
                minor_ticks_y = np.arange(0, 1.1, 0.1)     
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
		plt.xlim(_xlim)
		_peaksToPlotX =[]
		_peaksToPlotY =[]
		_risingsToPlotX =[]
		_risingsToPlotY =[]
		_hrtToPlotX =[]
		_hrtToPlotY =[]
		for _p in self._peaks:
			#overplot rising point and peak
			_peaksToPlotX.append( int(_p["peakIndex"]))
			_peaksToPlotY.append(  self._gaussianData[int(_p["peakIndex"])])
			_risingsToPlotX.append( _p["risingTimeIndex"])
			_risingsToPlotY.append( self._gaussianData[_p["risingTimeIndex"]])
			if _p["halfRecoveryIndex"] != None:
				_hrtToPlotX.append(  int(_p["halfRecoveryIndex"]))
				_hrtToPlotY.append( self._gaussianData[ int(_p["halfRecoveryIndex"])])

		plt.plot(_peaksToPlotX,_peaksToPlotY,  color='r',marker="o",markersize=5,linestyle='None' )
		plt.plot(_risingsToPlotX,_risingsToPlotY,  color='y',marker="o",markersize=5,linestyle='None')
		#overplot the hrt
		plt.plot(_hrtToPlotX,_hrtToPlotY, color='m',marker="x",markersize=5,linestyle='None')
		#save it! Because.. humans
		plt.savefig(figname)
        def toJson(self):
            return json.dumps(self._peaks)
        def toCSV(self):
	    _data = []
            for _peak in self._peaks:
                    _valsToPrint = []
                    _valsToPrint.append(str(_peak["peakValue"]))
                    _valsToPrint.append(str(_peak["peakAmplitude"]))
                    _valsToPrint.append(str(_peak["risingTimeValue"]))
                    _valsToPrint.append(str(_peak["halfRecoveryIndex"]))
                    #halfrecovery in secs
                    _valsToPrint.append(str(_peak["halfRecoveryValue"]))
                    _valsToPrint.append(str(_peak["distanceToPrevPeak"]))
                    _data.append([",".join(_valsToPrint)])
                    #TODO: How to merge multiple peaks in a single vector?
                    break
	    return _data
        def extract(self):
	    _data = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
            for _peak in self._peaks:
                    if _peak["peakValue"] != None:
                        _data[0] += _peak["peakValue"]
                        _data[1] += _peak["peakAmplitude"]
                        _data[2] += _peak["risingTimeValue"]
                    if _peak["halfRecoveryIndex"] !=None:
                        _data[3] += _peak["halfRecoveryIndex"] - _peak["peakIndex"] 
                        _data[4] += _peak["halfRecoveryValue"]
                    if _peak["distanceToPrevPeak"] != None:
                        _data[5] += _peak["distanceToPrevPeak"]

                    #TODO: How to merge multiple peaks in a single vector?
            #for _d in _data:
             #   _d = _d / len(_data)
            #_data.append(len(_data)
	    return _data
