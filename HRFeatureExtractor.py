from sklearn import preprocessing
class HRFeatureExtractor:
	def __init__(self,_data):
		self._data = _data
                self.cleanData()
                self.normalize()
		self._HRFeatures = [0.0,0.0]
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
		_max = max(self._data)
		_avg = reduce(lambda x, y: x + y, self._data) / len(self._data)
		self._HRFeatures = [_max,_avg]
		return self._HRFeatures
