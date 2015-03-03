import math
import time
import datetime
import os
import MyPlotter
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
				self._startTime = float( _r[1])
			elif(_r[0] == "END_TIME"):
				self._endTime = float (_r[1])
			elif(_r[0] == "DURATION"):
				self._duration = float (_r[1])
	def readFile(self,path):
		"""Reads a file from a path and returns a list with the raw data"""
		with open(path,"r") as _file:
			_data = _file.readlines()
		return _data
	def readDataType(self,dataType):
		"""Reads a selected datatype file. Valid DataTypes: ACC,IBI,SESSION,GSR,TEMP,BVP,HR"""
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
	def readAllDataTypes(self):
		"""Reads all datatypes files in the session"""
		self._dataACC = self.readFile(self._pathACC)
		self._dataIBI = self.readFile(self._pathIBI)
		self._dataSESSION = self.readFile(self._pathSESSION)
		self._dataGSR = self.readFile(self._pathGSR)
		self._dataTEMP = self.readFile(self._pathTEMP)
		self._dataBVP = self.readFile(self._pathBVP)
		self._dataHR = self.readFile(self._pathHR)
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
	def groupBySec(self,data, avg=False):
		_duration = int ( math.ceil(self._duration) )
		_data = [None] * _duration
		for _v in data:
			_pos = int(math.floor((_v[0] - self._startTime)))
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
		return _data
s = session("1425349830060/")
print s._subjectName
_data_slide = s.groupBySec(s._dataGSR[2000:4000],True)
print _data_slide
m = MyPlotter.MyPlotter("HR 60 secs",_data_slide)
m.plot("test")
