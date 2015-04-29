from MyPlotter import MyPlotter
from maxi import session
from sklearn import preprocessing

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
	
	#m = MyPlotter(_title_norm,_data_normalized,"Seconds","Value "+u)
        #m.plot(_path_norm) 

def plotTEMP(subject,test,sessionpath):
        s = session(sessionpath)
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	for _x in s._dataTEMP:
		_data_to_norm.append(_x[1])

	_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
 
        _title_raw = "TEMP: [%s,%s,raw]" % (subject,test)
	_title_norm = "TEMP: [%s,%s,normalized]" % (subject,test)

	_path_raw = "%s/plots/%s_%s_TEMP_raw" % (subject,subject,test)
	_path_norm = "%s/plots/%s_%s_TEMP_normalized" % (subject,subject,test)
	m = MyPlotter(_title_raw,_data_to_norm,"Seconds","Value (C)",)
        m.plot(_path_raw)
	
	m = MyPlotter(_title_norm,_data_normalized,"Seconds","Value (C)")
        m.plot(_path_norm) 

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
	plotGSR("Piloto_1","Rest",s)
        s = session("piloto_1_t1/1430265036998/")
	plotGSR("Piloto_1_t1","Test",s)