from sklearn import preprocessing
from MyPlotter import MyPlotter
import numpy
class IBIFeatureExtractor:
	def __init__(self,_data):
		self._data = _data
                self.cleanData()
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
        def plot(self,_path ,_limx=None,_limy=None):
                _title_raw = "IBI"
                _path_raw = _path
                m = MyPlotter(_title_raw,self._data,"Seconds","Value (seconds) ",limx=_limx,limy=[0,1],_xTick=2,_yTick=1.0)
                m.plot(_path_raw)
