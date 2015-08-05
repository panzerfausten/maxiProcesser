from sklearn import preprocessing
from MyPlotter import MyPlotter
import numpy
import pylab as plt
class IBIFeatureExtractor:
	def __init__(self,_data):
		self._data = _data
                #self.cleanData()
                #self.normalize()
		self._IBIFeatures = [0,0,0,0,0,0]
		self._cdata = []
        def cleanData(self):
                data = []
        	for _x in self._data:
	                data.append(_x[1])
                self._data = data
        def normalize(self):
                min_max_scaler = preprocessing.MinMaxScaler()
                self._data = min_max_scaler.fit_transform(self._data)

	def extract(self):
                _min = numpy.min(self._data)
                _max = numpy.max(self._data)
                _avg = numpy.average(self._data)
                _sd  = numpy.std(self._data)
                _amp = _max - _min
                _succ_diffs = []
                for _x,_ibi in enumerate(self._data):
                    if(_x > 0 and _x < len(self._data) -1 and self._data[_x+1] != None and self._data[_x] != None):
                        _succ_diffs.append(abs(self._data[_x] - self._data[_x+1]))
                _sdsd = numpy.std(_succ_diffs)
		self._IBIFeatures = [_min,_avg,_sd]
		return self._IBIFeatures
        def plot(self,_path ,_limx=None,_limy=None,_session=None,_xTick=2,_xMinorTick=1):
                _title_raw = "IBI"
                _path_raw = _path
                fig, ax = plt.subplots()
                index = numpy.arange(len (self._data))
                plt.grid(True)

                major_ticks = numpy.arange(0, len(self._data), _xTick)
                minor_ticks = numpy.arange(0, len(self._data), _xMinorTick)

                ax.grid(which='both')

                # or if you want differnet settings for the grids:                               
                ax.grid(which='minor', alpha=0.2)
                ax.grid(which='major', alpha=0.5)
                if (_limy == None):
                        _limy = [0,1.1]
                plt.ylim(_limy)
                #major_ticks_y = np.arange(0, 1.1, 0.2)                                              
                #minor_ticks_y = np.arange(0, 1.1, 0.1)     
                ax.set_xticks(major_ticks)
                ax.set_xticks(minor_ticks, minor=True)
                #set axis. Nazi axis?
                ax.set_ylabel("Seconds")
                ax.set_xlabel("Seconds")
                ax.set_title("IBI values")
                plt.plot(self._data,color="red") #plot the processed data

                if(_session != None):
                    if (_session._SRRanges != None):
                        for _i,_c in enumerate(_session._SRRanges):
                            if(_c[0] == '0'):
                                ax.axvspan(_c[1],_c[2],color="green",alpha=1)
                            if(_c[0] == '1'):
                                ax.axvspan(_c[1],_c[2],color="red",alpha=1)
                            if(_c[0] == '-1'):
                                ax.axvspan(_c[1],_c[2],color="gray",alpha=.7)


                plt.savefig(_path)
