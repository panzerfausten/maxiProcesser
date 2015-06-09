with open ("HR.csv","r") as _file:
	start = 0
	for _col, _row in enumerate(_file):
		_val = _row.split(",")
		if( _col == 0):
			start = float(_val[0])
		else:
			_val[0] = str(float(_val[0]) + start)
			_zeroesToFill = 14 - len(_val[0])
                        if( _zeroesToFill< 13):
                        	_val[0] = _val[0] + ( "0" * _zeroesToFill)
				_val[1] =  str(60.0/ float (_val[1]) )
			print ",".join(_val).replace("\n","")
