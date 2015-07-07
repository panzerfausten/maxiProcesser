def find_between(s,_s1,_s2):
	_i1 = s.index("#")
	_i2 = s[_i1+1:].index("#")
	return s[_i1+1:_i2].replace("-",""),s[_i2+4:]
def deduct_secs(time,secs=1):
	_hours,_mins,_secs = time.split(":")
	_hours = int(_hours)
	_mins = int(_mins)
	_secs = int(_secs)

	_total_secs =  ( (_hours * 60) * 60) + (_mins * 60) + _secs
	_total_secs -= 1
	_hours = _total_secs /3600
	_total_secs -= _hours * 3600
	_mins = _total_secs /60
	_total_secs -= _mins * 60
	_secs = _total_secs

	return "%i:%i:%i" %(_hours,_mins,_secs)
with open("transcript.txt","r") as _FILE:
	_lines = _FILE.readlines()
	for _x in range(0,len(_lines) -1):
		_l = (_lines[_x])
		_ln = (_lines[_x+1])
		_start,_text  =  find_between(_l,"#","#")
		_startn,_textn = find_between(_ln,"#","#")
		_end = deduct_secs(_startn)
		_x += 1
		print "%i\n%s,000 --> %s,000\n%s" %(_x+1,_start,_end,_text)

