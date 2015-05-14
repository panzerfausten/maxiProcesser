from maxi import session
from GSRFeatureExtractor import GSRFeatureExtractor


def getFeatures(session):
	_groupedData = s.groupBySec(s._dataGSR,True,False)
	_maxWindows =  ( len(_groupedData) / 60) * 60
	for _i in range(0,_maxWindows,60):
		_gsrData = _groupedData[_i:_i+60]
		_gFE = GSRFeatureExtractor(_gsrData)
		_features =  _gFE.extract()
		print _features["peaksCount"]
		print _features["peakValues"]
		print _features["halfRecoveryTimes"]
		print _features["risingTimeValues"]
if __name__ == "__main__":
	s = session("piloto_1_t1/1430265036998/")
	getFeatures(s)
	s = session("p2/p2_t1/1430349866785/")
	getFeatures(s)
