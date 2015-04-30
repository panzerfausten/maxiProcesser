import numpy
import peakutils
import peakutils.plot
import sys

_path_input = sys.argv[1]
_path_output = sys.argv[2]
with open(_path_input,"r") as _file_input:
	_lines = _file_input.readlines()
	_data = []
	_positiveData = []
	for _l in _lines:
		_vals = _l.split(",")
		_vals[0] = float(_vals[0])
		_vals[1] = float(_vals[1])
		_data.append(_vals)
		if(_vals[1] > 0):
			#print _vals[1]
			_positiveData.append(60.0 /_vals[1])
	
	_indexes = peakutils.indexes(_positiveData, thres=0.1, min_dist=1)	
	_peakData = []
	for i in _indexes:
		_peakData.append( [_data[i][0], _positiveData[i]]) #peakData
	
	
	_hrData = _peakData
	for _i, _pD in enumerate(_peakData): #peakindexes
		if(_i < len(_peakData) -1):
			_r1 = _pD
			_r2 = _peakData[_i+1]
			_t1 = float(_pD[0])
			_d1 = float(_pD[1])
			_t2 = float(_r2[0])
			_d2 = float(_r2[1])
			if(_t1 + _d1 < _t2):
				_hrData.insert(_i+1,[_t1+_d1,_t2-_t1-_d1])
	with open(_path_output, "w") as _file_output:
		for _hr in _hrData:
			_hr[0] = str(_hr[0])
			_zeroesToFill = 14 - len(_hr[0])
			if( _zeroesToFill< 13):
				_hr[0] = _hr[0] + ( "0" * _zeroesToFill)
			_hr[1] = str(_hr[1])
			_l = ",".join(_hr)+"\n"
			_file_output.write(_l)
