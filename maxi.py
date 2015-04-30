import math
import time
import datetime
import os
import MyPlotter
import numpy as np
from sklearn import preprocessing

class session:
	def __init__(self,folderPath):
		self._path = folderPath
		self.initFiles()
		self.readSessionMetadata()
		self.readAllDataTypes()
		self.sanitizeAllData()
	def initFiles(self):
		"""Finds the files in the selected folder"""
		self._dirList = os.listdir(self._path)
		
		self._pathZEPHYR  = None
		self._pathSOUNDS  = None
		self._pathACC = None
		self._pathIBI = None
		self._pathSESSION = None
		self._pathGSR = None
		self._pathTEMP = None
		self._pathBVP = None
		self._pathHR = None
		self._pathZEPHYR = None
		self._pathSOUNDS = None
		self._pathCODIFICATION = None
		self._pathEEG = None
                self._dataZEPHYR  = None
                self._dataSOUNDS  = None
                self._dataACC = None
                self._dataIBI = None
                self._dataSESSION = None
                self._dataGSR = None
                self._dataTEMP = None
                self._dataBVP = None
                self._dataHR = None
                self._dataZEPHYR = None
                self._dataSOUNDS = None
                self._dataCODIFICATION = None
                self._dataEEG = None

		for _f in self._dirList:
			if "ACC" in _f:
				self._pathACC = self._path  + _f
			elif "IBI" in _f:
				self._pathIBI = self._path + _f
			elif "SESSION" in _f:
				self._pathSESSION = self._path + _f
			elif "GSR" in _f:
				self._pathGSR = self._path + _f
			elif "TEMP" in _f:
				self._pathTEMP = self._path + _f
			elif "BVP" in _f:
				self._pathBVP = self._path + _f
			elif "HR" in _f:
				self._pathHR = self._path +_f
			elif "ZEPHYR" in _f:
				self._pathZEPHYR = self._path +_f
			elif "SOUNDS" in _f:
				self._pathSOUNDS = self._path +_f
			elif "CODIFICATION" in _f:
				self._pathCODIFICATION = self._path +_f
			elif "EEG" in _f:
				self._pathEEG = self._path + _f

	def readSessionMetadata(self):
		"""Reads the metadata in session.csv"""
		_lines = None
		with open(self._pathSESSION,"r") as _file_session:
			_lines = _file_session.readlines()
		
		#find the subject name:
		for _l in _lines:
			_r = _l.replace("\n","").split(",")
			if(_r[0] == "SUBJECT"):
				self._subjectName = _r[1]
			elif(_r[0] == "START_TIME"):
				self._startTime = float( _r[1][:10] +"." +_r[1][10:])
			elif(_r[0] == "END_TIME"):
				self._endTime = float ( _r[1][:10] +"." +_r[1][10:])
			elif(_r[0] == "DURATION"):
				self._duration = float ( _r[1][:3] +"." +_r[1][3:])

	def readFile(self,path):
		"""Reads a file from a path and returns a list with the raw data"""
		with open(path,"r") as _file:
			_data = _file.readlines()
		return _data
	def readDataType(self,dataType):
		"""Reads a selected datatype file. Valid DataTypes: ACC,IBI,SESSION,GSR,TEMP,BVP,HR"""
		self._dataZEPHYR  = None
		if(dataType == "ACC"):
			self._dataACC = self.readFile(self._pathACC)
		elif(dataType == "IBI"):
			self._dataIBI = self.readFile(self._pathIBI)
		elif(dataType == "GSR"):
			self._dataGSR = self.readFile(self._pathGSR)
		elif(dataType == "TEMP"):
			self._dataTEMP = self.readFile(self._pathTEMP)
		elif(dataType == "BVP"):
			self._dataBVP = self.readFile(self._pathBVP)
		elif(dataType == "HR"):
			self._dataHR = self.readFile(self._pathHR)
		elif(dataType == "ZEPHYR"):
			self._dataZEPHYR = self.readFile(self._pathZEPHYR)
	def readAllDataTypes(self):
		"""Reads all datatypes files in the session"""
		if(self._pathACC != None):
			self._dataACC = self.readFile(self._pathACC)
		
		if(self._pathIBI != None):
			self._dataIBI = self.readFile(self._pathIBI)

		if(self._pathSESSION != None):
			self._dataSESSION = self.readFile(self._pathSESSION)
	
		if(self._pathGSR != None):
			self._dataGSR = self.readFile(self._pathGSR)

		if(self._pathTEMP != None):
			self._dataTEMP = self.readFile(self._pathTEMP)

		if(self._pathBVP != None):
			self._dataBVP = self.readFile(self._pathBVP)
	
		if(self._pathHR != None):
			self._dataHR = self.readFile(self._pathHR)

		if(self._dataCODIFICATION != None):
			self._dataCODIFICATION = None

		if(self._pathZEPHYR != None):
			self._dataZEPHYR = self.readFile(self._pathZEPHYR)
		else:
			self._dataZEPHYR = None
		if(self._pathSOUNDS != None):
			self._dataSOUNDS = self.readFile(self._pathSOUNDS)
		else:
			self._dataSOUNDS = None
			self._dataSOUNDSUNIX = None

		if(self._pathCODIFICATION != None):
			self._dataCODIFICATION = self.readFile(self._pathCODIFICATION)
		if(self._pathEEG != None):
			self._dataEEG = self.readFile(self._pathEEG)

	def sanitizeAllData(self):
		"""Removes breaklines and splits data into positions in the lists"""
		_splittedData = []
		if(self._dataACC != None):
			for _row in self._dataACC:
				_row = _row.replace("\n","").split(",")
				_row[0] = float(_row[0])
				_row[1] = float(_row[1])
				_splittedData.append( _row)
			self._dataACC = _splittedData
		_splittedData = []
		if(self._dataIBI != None):
			for _row in self._dataIBI:
				_row = _row.replace("\n","").split(",")
				_row[0] = float(_row[0])
				_row[1] = float(_row[1])
				_splittedData.append( _row)
			self._dataIBI = _splittedData
		_splittedData = []
		if(self._dataGSR != None):
			for _row in self._dataGSR:
				_row = _row.replace("\n","").split(",")
				_row[0] = float(_row[0])
				_row[1] = float(_row[1])
				_splittedData.append( _row)
			self._dataGSR = _splittedData
		_splittedData = []
		if(self._dataTEMP != None):
			for _row in self._dataTEMP:
				_row = _row.replace("\n","").split(",")
				_row[0] = float(_row[0])
				_row[1] = float(_row[1])
				_splittedData.append( _row)
			self._dataTEMP = _splittedData
		_splittedData = []
		if(self._dataBVP != None):
			for _row in self._dataBVP:
				_row = _row.replace("\n","").split(",")
				_row[0] = float(_row[0])
				_row[1] = float(_row[1])
				_splittedData.append( _row)
			self._dataBVP = _splittedData
		_splittedData = []
		if(self._dataHR != None):
			for _row in self._dataHR:
				_row = _row.replace("\n","").split(",")
				_row[0] = float(_row[0])
				_row[1] = float(_row[1])
				_splittedData.append( _row)
			self._dataHR = _splittedData

		self._dataZEPHYR_HR = []
		self._dataZEPHYR_IBI = []
		if(self._dataZEPHYR != None):
			for _row in self._dataZEPHYR:
				_data = []
				_row  = _row.replace("\n","").split(",")
				_data.append(float(_row[0]))
				_data.append( float(_row[3]))
				if(_row[2] == "heartbeat_interval"):
					self._dataZEPHYR_IBI.append( _data)
					#_hr =  _data[1] 
					#self._dataZEPHYR_HR.append([_data[0],_hr])
				elif(_row[2] == "heart_rate"):
					self._dataZEPHYR_HR.append( _data)
		if(self._dataSOUNDS  != None):
			self._dataSOUNDSUNIX = []
			for _row in self._dataSOUNDS:
				_data = []
				_row  = _row.replace("\n","").split(",")
				_sd =   self.soundTimeToUnixStamp(str(_row[1]))
				_ed =   self.soundTimeToUnixStamp(str(_row[2]))
				_data.append(_sd)
				_data.append(_ed)
				self._dataSOUNDSUNIX.append(_data)
		_splittedData = []
		if(self._dataCODIFICATION != None):
			for _row in self._dataCODIFICATION:
				_row = _row.replace("\n","").split(",")
				_row[0] = int(_row[0])
				_row[1] = int(_row[1])
				_splittedData.append( _row)
			self._dataCODIFICATION = _splittedData

		_splittedData = []
		if(self._dataEEG != None):
			self._dataEEG1 = []
			self._dataEEG2 = []
			self._dataEEG3 = []
			self._dataEEG4 = []
			for _row in self._dataEEG:
				_row = _row.replace("\n","").split(",")
				_row[0] = float(_row[0])
				_row[1] = float(_row[1])
				_row[2] = float(_row[2])
				_row[3] = float(_row[3])
				_row[4] = float(_row[4])
				#_splittedData.append(_row)
				self._dataEEG1.append( [ _row[0] , _row[1] ] )
				self._dataEEG2.append( [ _row[0] , _row[2] ] )
				self._dataEEG3.append( [ _row[0] , _row[3] ] )
				self._dataEEG4.append( [ _row[0] , _row[4] ] )

	def normalizeGSR(self):
		_data_with_timestamps = np.asarray(self._dataGSR)
			
		_data_to_norm = _data_with_timestamps[:,1]
		min_max_scaler = preprocessing.MinMaxScaler()

		_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
		return _data_normalized
	#TODO: Move this to SessionUtils
	def normalize(self,data):
		_data_to_norm = np.asarray(data)
		min_max_scaler = preprocessing.MinMaxScaler()
		_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
		return _data_normalized

	def positiveBVPToHR(self):
		_hr = [None]  * len(self._positiveBVP)
		
		for _x in range(0,len(self._positiveBVP)):
			if(self._positiveBVP[_x] != None and self._positiveBVP[_x][1] > 0.0):
				_data = self._positiveBVP[_x]
				_data[1] = 60.0 / _data[1]
				_hr[_x] = _data
		return _hr
	def soundTimeToUnixStamp(self,_sound_time):
		_date,_time = _sound_time.split(" ")
		_y,_m,_d = _date.split("-")
		_h,_mm,_s = _time.split(":")
		_s,_ms = _s.split(".")
		unixStamp = datetime.datetime(int(_y),int(_m),int(_d),int(_h),int(_mm),int(_s),int(_ms))
		return unixStamp.strftime("%s")
	def toSecSounds(self):
		secSounds = []
		for _sound in self._dataSOUNDSUNIX:
			secSounds.append(  math.floor( float(_sound[1]) -  self._startTime ))
		return secSounds
	def getAVGHR(self):
		_avg = 0.0
		for _v in self._dataHR:
			_avg += float(_v[1])
		return (_avg / len( self._dataHR))
	def getAVGIBI(self):
		_avg = 0.0
		for _v in self._dataIBI:
			_avg += float(_v[1])
		return (_avg / len( self._dataIBI))
	def getAVGGSR(self):
		_avg = 0.0
		for _v in self._dataGSR:
			_avg += float(_v[1])
		return (_avg / len( self._dataGSR))
	def getAVGTEMP(self):
		_avg = 0.0
		for _v in self._dataTEMP:
			_avg += float(_v[1])
		return (_avg / len( self._dataTEMP))
	def groupBySec(self,data, avg=False , _max=False):
		_duration = int ( math.ceil(self._duration) )
		_data = [None] * _duration
		for _v in data:
			#print _v[0]
			#print self._startTime
			#TODO:DELETE ME ONCE YOU FIX THE APP
			if (len(str(_v[0])) > 10):
				_pos = int(math.floor(( int( str(_v[0])[:10]) - self._startTime)))	
			else:
				_pos = int(math.floor((_v[0] - self._startTime)))
			#print "firstdata -> %i"  %(int(math.floor((_v[0]))))
			#print "startTime-> %i" %(self._startTime)
			#print "len(data)-> %i" %(len(_data))
			if(_pos > 1 and _pos < len(_data) -1):
				if(_data[_pos-1] == None):
					_data[_pos-1] = []
					_data[_pos-1].append(_v)
				else:
					_data[_pos-1].append(_v)

		if(avg):
			_avgs = [None] * _duration
			_x = 0
			for _d in _data:
				_total = 0.0
				if not (_d == None):
					for _v in _d:
						_total += _v[1]
					_avg = _total / len(_d)
					_avgs[_x] = _avg
				_x += 1
			return _avgs
		if(_max):
			_maxs = [None] * _duration
			_x = 0
			for _d in _data:
				_max = -999999999999999
				if not (_d == None):
					for _v in _d:
						#_total += _v[1]
						if( _v[1] > _max):
							_max = _v[1]
					_maxs[_x] = _max
				_x += 1
			return _maxs
		return _data
########################N1
if(__name__ == "__main__"):
	u = u'\u00B5'
	s = session("n1/e3/n1/1425332915304/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session test 1",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n1/plots/GSR_1")

	#HR
	print s._positiveBVP[50:73]
	print "\n"
	_data_slide = s.groupBySec(s._positiveBVP,True)
	print s._cleanHR[50:73]
	m = MyPlotter.MyPlotter("Clean HR full session test 3",_data_slide,"Seconds","HR value")
	m.plot("n1/plots/HR_1")

	#HR ZEPYHR


	s = session("n1/e3/n1_2/1425334248275/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session test 2",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n1/plots/GSR_2")

	s = session("n1/e3/n1_3/1425335647100/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session test 3",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n1/plots/GSR_3")



	#######################N2
	#plot sample
	s = session("n2/n2_sample/1425405680330/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session SAMPLE",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n2/plots/GSR_sample")


	#plot HR from stage1
	_data_slide = s.groupBySec(s._positiveBVP,False,_max=True)
	m = MyPlotter.MyPlotter("Clean HR session SAMPLE",_data_slide,"Seconds","HR value")
	m.plot("n2/plots/HR_SAMPLE_1")



	#plot stage1
	s = session("n2/n2_1/1425406094608/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session 1",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n2/plots/GSR_1")


	#plot HR from stage1
	_data_slide = s.groupBySec(s._positiveBVP,False,_max=True)
	m = MyPlotter.MyPlotter("Clean HR full session test 1",_data_slide[850:900],"Seconds","HR value")
	m.plot("n2/plots/HR_1")



	#plot HR ZEPHYR from stage1
	_data_slide = s.groupBySec(s._dataZEPHYR_HR,True,False)
	m = MyPlotter.MyPlotter("HR from Zephyr full session test 1",_data_slide[60:120],"Seconds","HR value")
	m.plot("n2/plots/HR_ZEPHYR_1")


	#plot GSR from stage 2
	s = session("n2/n2_2/1425407232389/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session 2",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n2/plots/GSR_2")



	#plot GSR from stage 3
	s = session("n2/n2_3/1425408677098/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session 3",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n2/plots/GSR_3")


	#######################N3
	s = session("n3/n3_sample/1425409979748/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session SAMPLE",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n3/plots/GSR_sample")

	s = session("n3/n3_1/1425410684040/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session 1",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n3/plots/GSR_1")

	s = session("n3/n3_2/1425411806445/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session 2",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n3/plots/GSR_2")

	s = session("n3/n3_3/1425413219572/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session 3",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n3/plots/GSR_3")
	#######################N4
	s = session("n4/n4_sample/1425424011391/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session SAMPLE",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n4/plots/GSR_sample")

	s = session("n4/n4_1/1425424406612/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session 1",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n4/plots/GSR_1")

	s = session("n4/n4_2/1425425734089/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session 2",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n4/plots/GSR_2")

	s = session("n4/n4_3/1425427210413/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session 3",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n4/plots/GSR_3")
	#######################N4
	s = session("n5/n5_sample/1425492334386/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session SAMPLE",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n5/plots/GSR_sample")

	s = session("n5/n5_1/1425492729555/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session 1",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n5/plots/GSR_1")

	s = session("n5/n5_2/1425494040887/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session 2",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n5/plots/GSR_2")

	s = session("n5/n5_3/1425495483937/")
	_data_slide = s.groupBySec(s._dataGSR,True)
	m = MyPlotter.MyPlotter("GSR full session 3",_data_slide,"Seconds","Avg Value "+u)
	m.plot("n5/plots/GSR_3")

