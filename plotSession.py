from MyPlotter import MyPlotter
from maxi import session
from sklearn import preprocessing
import numpy as np
from HalfRecoveryTimeDetector import HalfRecoveryTimeDetector
from HRFeatureExtractor import HRFeatureExtractor
from IBIFeatureExtractor import IBIFeatureExtractor
from TEMPFeatureExtractor import TEMPFeatureExtractor
from datetime import datetime
import sys
import traceback
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

	if (s._dataANXIETY != None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,_anxiData =s.getAnxious(),_xTick=200,_yTick=1,_session=session)
	elif(s._dataSOUNDS !=None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,sounds=s.toSecSounds(),_xTick=200,_yTick=1)
	else:
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,_xTick=200,_yTick=1)
        m.plot(_path_raw)
def plotTEMP(subject,test,session,_limx=None,_limy=None,_groupBySec=True):
	u = u'\u00B0'
        s = session
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	_label = "Seconds"
	if(_groupBySec):
		_dataToPlot = s.groupBySec(s._dataTEMP,True,False)
	else:	
		_dataToPlot = []
		_label = "Values ( -- Hz )"
		for _x in s._dataGSR:
			_dataToPlot.append(_x[1])

	
	#_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
 
        _title_raw = "TEMP: [%s,%s,BySec]" % (subject,test)
	_title_norm = "TEMP: [%s,%s,normalized]" % (subject,test)

	_path_raw = "%s/plots/%s_%s_TEMP_raw" % (subject,subject,test)
	_path_norm = "%s/plots/%s_%s_TEMP_normalized" % (subject,subject,test)

	if (s._dataCODIFICATION != None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u+"C",color='blue',limx=_limx,limy=_limy,codification=s._dataCODIFICATION,_xTick=200,_yTick=1)
	elif(s._dataSOUNDS !=None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u+"C",color='blue',limx=_limx,limy=_limy,sounds=s.toSecSounds(),_xTick=200,_yTick=1)
	else:
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u+"C",color='blue',limx=_limx,limy=_limy,_xTick=200,_yTick=1)
        m.plot(_path_raw)

def none_to_nan(values):
    """Replace every 0 with 'nan' and return a copy."""
    return [float('nan') if x==None else x for x in values]


def plotHR(subject,test,session,_limx=None,_limy=None,_groupBySec=False):
	u = u'\u00B5'
        s = session
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	_label = "Seconds"
	if(_groupBySec):
		_dataToPlot = s.groupBySec(s._dataHR,True,False)
		#for _i, _d in enumerate(_dataToPlot):
		#	if _d == None:
		#		_dataToPlot[_i] = 0
		#_dataToPlot = none_to_nan(_dataToPlot)
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
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,codification=s._dataCODIFICATION,_xTick=200,_yTick=20)
	elif(s._dataSOUNDS !=None):
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,sounds=s.toSecSounds(),_xTick=200,_yTick=20)
	else:
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,_xTick=200,_yTick=20)
        m.plot(_path_raw)
def plotHR_ZEPHYR(subject,test,session, sounds = [],_limx=None,_limy=None,groupBySec=True):
        s = session
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	for _x in s._dataZEPHYR_HR:
		_data_to_norm.append(_x[1])

	_dataAvgBySec = s.groupBySec(s._dataZEPHYR_HR,False,True)
        _title_raw = "HR: [%s,%s,raw]" % (subject,test)

	_path_raw = "%s/plots/%s_%s_HR_raw" % (subject,subject,test)
	if(groupBySec):
		if (s._dataANXIETY != None):
			m = MyPlotter(_title_raw,_dataAvgBySec,"Seconds","Value (BPM) ",limx=_limx,limy=_limy,_xTick=200,_yTick=20,_anxiData=s.getAnxious(),_session=s)
		else:
			m = MyPlotter(_title_raw,_dataAvgBySec,"Seconds","Value (BPM) ",limx=_limx,limy=_limy,_xTick=200,_yTick=20)
	else:
		if (s._dataANXIETY != None):
			m = MyPlotter(_title_raw,_data_to_norm,"Seconds","Value (BPM) ",limx=_limx,limy=_limy,_xTick=200,_yTick=20,_anxiData=s.getAnxious(),_session=s)
		else:
			m = MyPlotter(_title_raw,_data_to_norm,"Seconds","Value (BPM) ",limx=_limx,limy=_limy,_xTick=200,_yTick=20)
	m.plot(_path_raw)
	
def plotIBI_ZEPHYR(subject,test,session, sounds = [],_limx=None,_limy=None,groupBySec=True):
        s = session
        _data_to_norm = []
        min_max_scaler = preprocessing.MinMaxScaler()
        for _x in s._dataZEPHYR_IBI:
                _data_to_norm.append(_x[1])

        _dataAvgBySec = s.groupBySec(s._dataZEPHYR_IBI,False,True)
        _title_raw = "IBI: [%s,%s,raw]" % (subject,test)

        _path_raw = "%s/plots/%s_%s_IBI_raw" % (subject,subject,test)
        if(groupBySec):
                m = MyPlotter(_title_raw,_dataAvgBySec,"Seconds","Value (seconds) ",limx=_limx,limy=_limy,_xTick=200,_yTick=1.0)
        else:
                m = MyPlotter(_title_raw,_data_to_norm,"Seconds","Value (seconds) ",limx=_limx,limy=_limy,xTick=200,_yTick=1.0,_yTickMinor=0.1)

        m.plot(_path_raw)

def plotIBI_ZEPHYR2(subject,_data,_path ,_limx=None,_limy=None):
        _d = _data
        _title_raw = "IBI"
        _path_raw = _path
        m = MyPlotter(_title_raw,_data,"Seconds","Value (seconds) ",limx=_limx,limy=_limy,_xTick=200,_yTick=1.0)
        m.plot(_path_raw)
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

		_album.write(" okular albumGSR.pdf\n")\

def getFts(_s,plot=False,gsr=None,ibi=None):
    _dataGSR = _s.groupBySec(_s._dataGSR,True,False)
    _dataAvgBySecIBI = filter(None,_s.groupBySec(_s._dataZEPHYR_IBI,True,False))
    _dataSR = _s._dataSR
    _s = -1
    _features =[]
    for _z in range(0,len(_dataSR)):
        for _x,_d in enumerate(reversed(_dataGSR)):
            if((_x / 60.)  == _z+1.5):
                _tag = str(_dataSR[_z])
                _segmentNumber = _z
                _s1Features =[str(_dataSR[_z])]
                _s2Features =[str(_dataSR[_z])]
                _segment1 = _dataGSR[_x-30:_x]
                _segment2 = _dataGSR[_x:_x+30]
                _s = _x-30
                _e = _x
                _s2 = _x
                _e2 = _x+30
                if(gsr):
                    htr = HalfRecoveryTimeDetector(_segment1)
                    if(plot):
                        htr.plot("plots/GSR_"+str(_dataSR[_z])+"_"+str(_z)+"_1",_ylim=[0,15],_xTick=2)
                    for _f in htr.extract():
                        _s1Features.append(_f)
                    htr = HalfRecoveryTimeDetector(_segment2)
                    if(plot):
                        htr.plot("plots/GSR_"+str(_dataSR[_z])+"_"+str(_z)+"_2",_ylim=[0,15],_xTick=2)
                    for _f in htr.extract():
                        _s2Features.append(_f)

                if(ibi):
                    try:
                        ibife = IBIFeatureExtractor(_dataAvgBySecIBI[_x-30:_x])
                        if(plot):
                            _path = "plots/ibi_%s_%i_1" %(_tag,_segmentNumber)
                            ibife.plot(_path,_limy=[0.0,1.1])
                        for _f in ibife.extract():
                            _s1Features.append(_f)
                    except:
                        _s1Features.append(0)
                        _s1Features.append(0)
                        _s1Features.append(0)
                    try:
                        ibife = IBIFeatureExtractor(_dataAvgBySecIBI[_x:_x+30])
                        if(plot):
                            _path = "plots/ibi_%s_%i_2" %(_tag,_segmentNumber)
                            ibife.plot(_path,_limy=[0.0,1.1])
                        for _f in ibife.extract():
                            _s2Features.append(_f)
                    except:
                        _s2Features.append(0)
                        _s2Features.append(0)
                        _s2Features.append(0)
                _features.append(_s1Features)
                _features.append(_s2Features)
                break
    for _f in _features:
        print ",".join(map(str,_f))
def getGSRSegments(_s,gsr=True,ibi=True):
    _dataGSR = _s.groupBySec(_s._dataGSR,True,False)
    _dataAvgBySecIBI = filter(None,_s.groupBySec(_s._dataZEPHYR_IBI,True,False))
    _features = []
    for _x in range(0,len(_dataGSR),30):
        _dataG = filter(None,_dataGSR[_x:_x+60])
        _dataI = filter(None,_dataAvgBySecIBI[_x:_x+60])
        _feature =["-3"]
        if( len(_dataG) > 20 and len(_dataI) > 20):
            if(gsr):
                htr = HalfRecoveryTimeDetector(_dataI)
                for _f in htr.extract():
                    _feature.append(_f)

            if(ibi):
                ibife = IBIFeatureExtractor(_dataG)
                for _f in ibife.extract():
                    _feature.append(_f)
            _features.append(_feature)
    for _f in _features:
        print ",".join(map(str,_f))

def plotSessionSR(_s,path):
    _dataGSR = _s.groupBySec(_s._dataGSR,True,False)
    _dataAvgBySecIBI = _s.groupBySec(_s._dataZEPHYR_IBI,True,False)
    htr = HalfRecoveryTimeDetector(_dataGSR)
    htr.plot(path,_session=_s,_ylim=[0,15],_xTick=200,_xMinorTick=100,_xlim=[0,1900],_title="Periodos de ansiedad del P7,S2")
    ibife = IBIFeatureExtractor(_dataAvgBySecIBI[1:])
    ibife.plot("plotIBI.png",_limy=[0,1.1],_session=_s)
def getSessions(_sessions):
    _sessionsRtr = []
    for _s in _sessions:
        if(_s == "all"):
            s = session("p1/carlos_S1_R1/1433807211979/")
            _sessionsRtr.append(s)
            s = session("p1/carlos_relax3/1435362269780/")
            _sessionsRtr.append(s)
            s = session("p6/luis_relax/1433979780288/")
            _sessionsRtr.append(s)
            s = session("p6/luismiguel_relax2/1434671046538/")
            _sessionsRtr.append(s)
            s = session("p6/luis_relax3/1435273024530/")
            _sessionsRtr.append(s)
            s = session("p7/alfonso_relax/1434064078558/")
            _sessionsRtr.append(s)
            s = session("p7/alfonso_relax2/1434495734670/")
            _sessionsRtr.append(s)
            s = session("p7/alfonso_relax3/1435275565320/")
            _sessionsRtr.append(s)
            s = session("p9/sandra_relax/1434150573545/")
            _sessionsRtr.append(s)
            s = session("p9/sandra_relax3/1435619278734/")
            _sessionsRtr.append(s)
        if(_s == "p1"):
            s = session("p1/carlos_S1_R1/1433807211979/")
            _sessionsRtr.append(s)
            s = session("p1/carlos_relax3/1435362269780/")
            _sessionsRtr.append(s)
        if(_s == "p1s1"):
            s = session("p1/carlos_S1_R1/1433807211979/")
            _sessionsRtr.append(s)
        if(_s == "p1s3"):
            s = session("p1/carlos_relax3/1435362269780/")
            _sessionsRtr.append(s)
        if(_s == "p6"):
            s = session("p6/luis_relax/1433979780288/")
            _sessionsRtr.append(s)
            s = session("p6/luismiguel_relax2/1434671046538/")
            _sessionsRtr.append(s)
            s = session("p6/luis_relax3/1435273024530/")
            _sessionsRtr.append(s)
        if(_s =="p6s1"):
            s = session("p6/luis_relax/1433979780288/")
            _sessionsRtr.append(s)
        if(_s =="p6s2"):
            s = session("p6/luismiguel_relax2/1434671046538/")
            _sessionsRtr.append(s)
        if(_s =="p6s3"):
            s = session("p6/luis_relax3/1435273024530/")
            _sessionsRtr.append(s)
        if(_s == "p7"):
            s = session("p7/alfonso_relax/1434064078558/")
            _sessionsRtr.append(s)
            s = session("p7/alfonso_relax2/1434495734670/")
            _sessionsRtr.append(s)
            s = session("p7/alfonso_relax3/1435275565320/")
            _sessionsRtr.append(s)
        if(_s == "p7s1"):
            s = session("p7/alfonso_relax/1434064078558/")
            _sessionsRtr.append(s)
        if(_s == "p7s2"):
            s = session("p7/alfonso_relax2/1434495734670/")
            _sessionsRtr.append(s)
        if(_s == "p7s3"):
            s = session("p7/alfonso_relax3/1435275565320/")
            _sessionsRtr.append(s)
        if(_s == "p8"):
            s = session("p8/angello_relax/1434066549276/")
            _sessionsRtr.append(s)
            s = session("p8/angello_relax2/1434668094145/")
            _sessionsRtr.append(s)
            s = session("p8/angello_relax3/1435708008150/")
            _sessionsRtr.append(s)
        if(_s == "p8s1"):
            s = session("p8/angello_relax/1434066549276/")
            _sessionsRtr.append(s)
        if(_s == "p8s2"):
            s = session("p8/angello_relax2/1434668094145/")
            _sessionsRtr.append(s)
        if(_s == "p8s3"):
            s = session("p8/angello_relax3/1435708008150/")
            _sessionsRtr.append(s)
        if(_s == "p9"):
            s = session("p9/sandra_relax/1434150573545/")
            _sessionsRtr.append(s)
            s = session("p9/sandra_relax3/1435619278734/")
            _sessionsRtr.append(s)
        if(_s == "p9s1"):
            s = session("p9/sandra_relax/1434150573545/")
            _sessionsRtr.append(s)
        if(_s == "p9s3"):
            s = session("p9/sandra_relax3/1435619278734/")
            _sessionsRtr.append(s)
    return _sessionsRtr
if (__name__ == "__main__"):
    """
    s = session("p6/luis_relax/1433979780288/")
    plotGSR("p6/luis_relax","luismiguel_relax",s,_limy=[0.0,1.0])
    htr = HalfRecoveryTimeDetector(s.groupBySec(s._dataGSR,True,False))
    htr.plot("p6/luis_relax",_ylim=[0,1.1])
    plotHR_ZEPHYR("p6/luis_relax","luismiguel_relax_HR",s,_limy=[0,120])
    getFeaturesFrom(s)

    s = session("p6/luismiguel_relax2/1434671046538/")
    plotGSR("p6/luismiguel_relax2","luismiguel_relax2",s,_limy=[0.0,1.0])
    htr = HalfRecoveryTimeDetector(s.groupBySec(s._dataGSR,True,False))
    htr.plot("p6/luismiguel_relax2",_ylim=[0,1.1])
    plotHR_ZEPHYR("p6/luismiguel_relax2","luismiguel_relax2_HR",s,_limy=[0,120])
    getFeaturesFrom(s)

    s = session("p1/carlos_S1_R1/1433807211979/")
    plotGSR("p1/carlos_S1_R1","carlos_S1_R1",s,_limy=[0.0,1.0])
    htr = HalfRecoveryTimeDetector(s.groupBySec(s._dataGSR,True,False))
    htr.plot("p1/carlos_S1_R1/plots/carlos_S1_R1_htr",_ylim=[0,1.1])
    plotHR_ZEPHYR("p1/carlos_S1_R1","carlos_S1_R1_relax_HR",s,_limy=[0,120])
    getFeaturesFrom(s)
    s = session("p1/carlos_relax3/1435362269780/")
    plotGSR("p1","p1_relax_GSR",s,_limy=[0.0,6])
    htr = HalfRecoveryTimeDetector(s.groupBySec(s._dataGSR,True,False))
    htr.plot("p1/carlos_relax3/plots/carlos_relax3_htr",_ylim=[0,1.3])
    plotHR_ZEPHYR("p1/carlos_relax3","carlos_relax_HR",s,_limy=[0,120])
    getFeaturesFrom(s)
    s = session("p9/sandra_relax/1434150573545/")
    plotGSR("p9/sandra_relax","sandra_relax_GSR",s,_limy=[0.0,1.0])
    plotHR_ZEPHYR("p9/sandra_relax","sandra_relax_HR",s,_limy=[0,120])
    getFeaturesFrom(s)

    s = session("p9/sandra_relax3/1435619278734/")
    plotGSR("p9/sandra_relax3","sandra_relax3_GSR",s,_limy=[0.0,1.0])
    plotHR_ZEPHYR("p9/sandra_relax3","sandra_relax3_HR",s,_limy=[0,120])
    getFeaturesFrom(s)
    s = session("p5/alma_rest/1433977560736/")
    getFeaturesFrom(s)
    """
    _data = sys.argv[1]
    _signals = sys.argv[2]
    _data = _data.split(",")
    _signals = _signals.split(",")
    _getGSR = False
    _getIBI = False
    _fSession = True
    if("gsr" in _signals):
        _getGSR = True
    if("ibi" in _signals):
        _getIBI = True
    print _data
    for _s in getSessions(_data):
            print "plotting session..."
            plotSessionSR(_s,"plotSR.png")