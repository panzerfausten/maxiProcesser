class HRFeatureExtractor:
	def __init__(self,_data):
		self._data = _data
		self._HRFeatures = []
		self._cdata = []
	def extract(self):
        	for _x in self._data:
			self._cdata.append(_x[1])
		_max = max(self._cdata)
		_avg = reduce(lambda x, y: x + y, self._cdata) / len(self._cdata)
		self._HRFeatures = [_max,_avg]
		return self._HRFeatures
