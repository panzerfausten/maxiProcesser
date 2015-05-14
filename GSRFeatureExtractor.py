from HalfRecoveryTimeDetector import HalfRecoveryTimeDetector

class GSRFeatureExtractor:
	def __init__(self,_data):
		self._data = _data
		try:
			self._htr = HalfRecoveryTimeDetector(self._data)
		except:
			raise("HTR Exception. Maybe an error in your data?")
		self._features ={"peaksCount":0,"peakValues":[],"halfRecoveryTimes":[],"risingTimeValues":[]}
	def extract(self):
		"""
		Extracts all the possible features in the data set.
		Features: Peaks count, Peaks Amplitudes, Half Recovery index (time), Peak Rise Time
		"""
		self._features["peaksCount"] = len(self._htr._peaks)
		for _p in self._htr._peaks:
			self._features["peakValues"].append(_p["peakValue"])
			if( _p["halfRecoveryIndex"] != None):
				self._features["halfRecoveryTimes"].append(_p["halfRecoveryIndex"] - _p["peakIndex"])
			else:
				self._features["halfRecoveryTimes"].append(None)
			self._features["risingTimeValues"].append(_p["risingTimeValue"])

		return self._features
