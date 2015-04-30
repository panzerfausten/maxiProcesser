from MyPlotter import MyPlotter
from maxi import session
from sklearn import preprocessing
import numpy as np
def plotGSR(subject,test,session,_limx=None,_limy=None,_groupBySec=True):
	u = u'\u00B5'
        s = session
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	_label = "Seconds"
	if(_groupBySec):
		_dataToPlot = s.groupBySec(s._dataGSR,True,False)
	else:	
		_dataToPlot = []
		_label = "Values ( 4.0 Hz )"
		for _x in s._dataGSR:
			_dataToPlot.append(_x[1])

	
	#_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
 
        _title_raw = "GSR: [%s,%s,BySec]" % (subject,test)
	_title_norm = "GSR: [%s,%s,normalized]" % (subject,test)

	_path_raw = "%s/plots/%s_%s_GSR_raw" % (subject,subject,test)
	_path_norm = "%s/plots/%s_%s_GSR_normalized" % (subject,subject,test)

	if (s._dataCODIFICATION != None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,codification=s._dataCODIFICATION)
	elif(s._dataSOUNDS !=None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,sounds=s.toSecSounds())
	else:
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy)
        m.plot(_path_raw)
def plotHR(subject,test,session,_limx=None,_limy=None,_groupBySec=True):
	u = u'\u00B5'
        s = session
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	_label = "Seconds"
	if(_groupBySec):
		_dataToPlot = s.groupBySec(s._dataHR,True,False)
		for _i, _d in enumerate(_dataToPlot):
			if _d == None:
				_dataToPlot[_i] = 0
		_dataToPlot = np.array(_dataToPlot)
	else:	
		_dataToPlot = []
		_label = "Values ( 4.0 Hz )"
		for _x in s._dataHR:
			_dataToPlot.append(_x[1])

	
	#_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
 
        _title_raw = "HR: [%s,%s,BySec]" % (subject,test)
	_title_norm = "GSR: [%s,%s,normalized]" % (subject,test)

	_path_raw = "%s/plots/%s_%s_HR_raw" % (subject,subject,test)
	_path_norm = "%s/plots/%s_%s_HR_normalized" % (subject,subject,test)

	if (s._dataCODIFICATION != None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,codification=s._dataCODIFICATION)
	elif(s._dataSOUNDS !=None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,sounds=s.toSecSounds())
	else:
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy)
        m.plot(_path_raw)
	
def plotTEMP(subject,test,session,_limx=None,_limy=None,_groupBySec=True):
	u = u'\u00B5'
        s = session
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	_label = "Seconds"
	if(_groupBySec):
		_dataToPlot = s.groupBySec(s._dataTEMP,True,False)
	else:	
		_dataToPlot = []
		_label = "Values ( 4.0 Hz )" #TODO
		for _x in s._dataTEMP:
			_dataToPlot.append(_x[1])

	
	#_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
 
       	_title_raw = "TEMP: [%s,%s,raw]" % (subject,test)
	_title_norm = "TEMP: [%s,%s,normalized]" % (subject,test)

	_path_raw = "%s/plots/%s_%s_TEMP_raw" % (subject,subject,test)
	_path_norm = "%s/plots/%s_%s_TEMP_normalized" % (subject,subject,test)

	if (s._dataCODIFICATION != None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value (C)"+u,color='blue',limx=_limx,limy=_limy,codification=s._dataCODIFICATION)
	elif(s._dataSOUNDS !=None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value (C)"+u,color='blue',limx=_limx,limy=_limy,sounds=s.toSecSounds())
	else:
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value (C)"+u,color='blue',limx=_limx,limy=_limy)
        m.plot(_path_raw)

def plotHR_ZEPHYR(subject,test, sounds = [],_limx=None,_limy=None,groupBySec=False):
        s = session
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	for _x in s._dataZEPHYR_HR:
		_data_to_norm.append(_x[1])

	_dataAvgBySec = s.groupBySec(s._dataZEPHYR_HR,False,True)
	#_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
        _title_raw = "HR: [%s,%s,raw]" % (subject,test)
	#_title_norm = "HR: [%s,%s,normalized]" % (subject,test)

	_path_raw = "%s/plots/%s_%s_HR_raw" % (subject,subject,test)
	#_path_norm = "%s/plots/%s_%s_HR_normalized" % (subject,subject,test)
	if (s._dataSOUNDS != None):
		if(groupBySec):
			m = MyPlotter(_title_raw,_dataAvgBySec,"Seconds","Value (BPM) ",limx=_limx,limy=_limy,sounds=s.toSecSounds())
		else:
			m = MyPlotter(_title_raw,_data_to_norm,"Seconds","Value (BPM) ",limx=_limx,limy=_limy,sounds=s.toSecSounds())
	elif (s._dataCODIFICATION != None):
		if(groupBySec):
			m = MyPlotter(_title_raw,_dataAvgBySec,"Seconds","Value (BPM) ",limx=_limx,limy=_limy,codification=s._dataCODIFICATION)
		else:
			m = MyPlotter(_title_raw,_data_to_norm,"Seconds","Value (BPM) ",limx=_limx,limy=_limy,codification=s._dataCODIFICATION)

	else:
		if(groupBySec):
			m = MyPlotter(_title_raw,_dataAvgBySec,"Seconds","Value (BPM) ",limx=_limx,limy=_limy)
		else:
			m = MyPlotter(_title_raw,_data_to_norm,"Seconds","Value (BPM) ",limx=_limx,limy=_limy)
		
        m.plot(_path_raw)
	
	#m = MyPlotter(_title_norm,_data_normalized,"Seconds","Value (C)",[50,100])
        #m.plot(_path_norm)  not norm by now
def plotEEG1(subject,test,session,_limx=None,_limy=None,_groupBySec=True):
	u = u'\u00B5'
        s = session
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	_label = "Seconds"
	if(_groupBySec):
		_dataToPlot = s.groupBySec(s._dataEEG1,True,False)
		print _dataToPlot[0]
		print s._dataEEG1[0]
	else:	
		_dataToPlot = []
		_label = "Values "
		for _x in s._dataEEG1:
			_dataToPlot.append(_x[1])

	
	#_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
 
        _title_raw = "EEG1: [%s,%s,BySec]" % (subject,test)
	_title_norm = "EEG1: [%s,%s,normalized]" % (subject,test)

	_path_raw = "%s/plots/%s_%s_EEG1_raw" % (subject,subject,test)
	_path_norm = "%s/plots/%s_%s_EEG1_normalized" % (subject,subject,test)

	if (s._dataCODIFICATION != None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,codification=s._dataCODIFICATION)
	elif(s._dataSOUNDS !=None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,sounds=s.toSecSounds())
	else:
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy)
        m.plot(_path_raw)
	
def plotEEG2(subject,test,session,_limx=None,_limy=None,_groupBySec=True):
	u = u'\u00B5'
        s = session
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	_label = "Seconds"
	if(_groupBySec):
		_dataToPlot = s.groupBySec(s._dataEEG2,True,False)
	else:	
		_dataToPlot = []
		_label = "Values "
		for _x in s._dataEEG2:
			_dataToPlot.append(_x[1])

	
	#_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
 
        _title_raw = "EEG2: [%s,%s,BySec]" % (subject,test)
	_title_norm = "EEG2: [%s,%s,normalized]" % (subject,test)

	_path_raw = "%s/plots/%s_%s_EEG2_raw" % (subject,subject,test)
	_path_norm = "%s/plots/%s_%s_EEG2_normalized" % (subject,subject,test)

	if (s._dataCODIFICATION != None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,codification=s._dataCODIFICATION)
	elif(s._dataSOUNDS !=None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,sounds=s.toSecSounds())
	else:
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy)
        m.plot(_path_raw)

def plotEEG3(subject,test,session,_limx=None,_limy=None,_groupBySec=True):
	u = u'\u00B5'
        s = session
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	_label = "Seconds"
	if(_groupBySec):
		_dataToPlot = s.groupBySec(s._dataEEG3,True,False)
	else:	
		_dataToPlot = []
		_label = "Values "
		for _x in s._dataEEG3:
			_dataToPlot.append(_x[1])

	
	#_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
 
        _title_raw = "EEG3: [%s,%s,BySec]" % (subject,test)
	_title_norm = "EEG3: [%s,%s,normalized]" % (subject,test)

	_path_raw = "%s/plots/%s_%s_EEG3_raw" % (subject,subject,test)
	_path_norm = "%s/plots/%s_%s_EEG3_normalized" % (subject,subject,test)

	if (s._dataCODIFICATION != None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,codification=s._dataCODIFICATION)
	elif(s._dataSOUNDS !=None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,sounds=s.toSecSounds())
	else:
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy)
        m.plot(_path_raw)


def plotEEG4(subject,test,session,_limx=None,_limy=None,_groupBySec=True):
	u = u'\u00B5'
        s = session
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	_label = "Seconds"
	if(_groupBySec):
		_dataToPlot = s.groupBySec(s._dataEEG4,True,False)
	else:	
		_dataToPlot = []
		_label = "Values "
		for _x in s._dataEEG4:
			_dataToPlot.append(_x[1])

	
	#_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
 
        _title_raw = "EEG4: [%s,%s,BySec]" % (subject,test)
	_title_norm = "EEG4: [%s,%s,normalized]" % (subject,test)

	_path_raw = "%s/plots/%s_%s_EEG4_raw" % (subject,subject,test)
	_path_norm = "%s/plots/%s_%s_EEG4_normalized" % (subject,subject,test)

	if (s._dataCODIFICATION != None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,codification=s._dataCODIFICATION)
	elif(s._dataSOUNDS !=None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,sounds=s.toSecSounds())
	else:
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy)
        m.plot(_path_raw)


def generateMergeScript(subject,path):
	_baseGSR = "montage -geometry +1+1 %s_sample_GSR_raw.png  %s_t1_GSR_raw.png  %s_t2_GSR_raw.png %s_t3_GSR_raw.png %s_sample_HR_raw.png  %s_t1_HR_raw.png %s_t2_HR_raw.png  %s_t3_HR_raw.png out.png\n"
	#_baseTEMP = "montage -geometry +1+1 %s_sample_TEMP_raw.png  %s_sample_TEMP_normalized.png %s_t1_TEMP_raw.png %s_t1_TEMP_normalized.png %s_t2_TEMP_raw.png %s_t2_TEMP_normalized.png %s_t3_TEMP_raw.png %s_t3_TEMP_normalized.png out.png\n"
	_toPdfGSR = "convert out.png plots_GSR_HR_%s.pdf"  % (subject)
	#_toPdfTEMP = "convert out.png plots_TEMP_%s.pdf"  % (subject)
	with open(path+"/merge.sh","w") as _script_file:
		_baseGSR = _baseGSR % ( (subject,)*8)
		#_baseTEMP = _baseTEMP % ( (subject,)*8)
		_script_file.write(_baseGSR )
		_script_file.write(_toPdfGSR)
		_script_file.write("\nrm out.png\n")
		#_script_file.write(_baseTEMP )
		#_script_file.write(_toPdfTEMP)
		#_script_file.write("\nrm out.png\n")
	_script_file.close()

def generateAlbumScript(subjects):
	with open("album.sh","w") as _album:
		_album.write("sh joins.sh\n")
		_album.write("pdftk ")
		for _subject in subjects:
			_album.write(" %s/plots/plots_GSR_HR_%s.pdf " %(_subject,_subject))
		_album.write(" output albumGSR.pdf\n")
		
		_album.write("\npdftk ")
		for _subject in subjects:
			_album.write(" %s/plots/plots_TEMP_%s.pdf " %(_subject,_subject))
		_album.write(" output albumTEMP.pdf\n")

		_album.write(" okular albumGSR.pdf\n")
if (__name__ == "__main__"):
        s = session("piloto_1/1430264513038/")
	#plotGSR("piloto_1","Rest",s,_limy=[0.0,5.0])
	plotHR("piloto_1","Rest",s)
        

	s = session("piloto_1_t1/1430265036998/")
	plotHR("piloto_1_t1","Rest",s)

	###P2
	s = session("p2/p2_test/1430349218221/")
	plotGSR("p2/p2_test","Rest",s,_limy=[0.0,5.0])
	plotHR("p2/p2_test","Rest",s,_limy=[0.0,5.0])

	s = session("p2/p2_t1/1430349866785/")
	plotGSR("p2/p2_t1","t1",s,_limy=[0.0,5.0])
	plotHR("p2/p2_t1","t1",s)
	
	"""plotEEG1("piloto_1","Rest",s)
	plotEEG2("piloto_1","Rest",s)
	plotEEG3("piloto_1","Rest",s)
	plotEEG4("piloto_1","Rest",s)
	#plotTEMP("piloto_1","Rest",s,_limy=[30.0,40.0]) not useful
	plotGSR("piloto_1_t1","Test",s,_limy=[0.0,5.0])
	plotEEG1("piloto_1_t1","Test",s,_limx=[800,1200])
	plotEEG2("piloto_1_t1","Test",s,_limx=[800,1200])
	plotEEG3("piloto_1_t1","Test",s,_limx=[800,1200])
	plotEEG4("piloto_1_t1","Test",s,_limx=[800,1200])
	plotTEMP("piloto_1_t1","Test",s,_limy=[30.0,40.0])
	"""
