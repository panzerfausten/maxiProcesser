from MyPlotter import MyPlotter
from maxi import session
from sklearn import preprocessing
import numpy as np
from HalfRecoveryTimeDetector import HalfRecoveryTimeDetector
from HRFeatureExtractor import HRFeatureExtractor
from IBIFeatureExtractor import IBIFeatureExtractor
from TEMPFeatureExtractor import TEMPFeatureExtractor
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

def getFeaturesFrom(_session,gsr=True,hr=True,ibi=True,temp=True):
            _session.getAnxious()
            _dataAvgBySecHR = _session._dataZEPHYR_HR
            _dataAvgBySecIBI = _session._dataZEPHYR_IBI
            _dataAvgBySecTEMP = _session._dataTEMP
            _dataGSR = _session.groupBySec(_session._dataGSR,True,False)
            for seg in s._dataANXIETYRANGES:
                    _s,_e,_l = seg
                    if (_l != -1):
                            extraFeatures = []
                            if(gsr):
                                if  len(_dataGSR[_s:_e]) > 0:
                                    htr = HalfRecoveryTimeDetector(_dataGSR[_s:_e])
                                    extraFeatures.append(htr.extract())
                            if(hr):
                                if  len(_dataAvgBySecHR[_s:_e]) > 0:
                                    hrfe = HRFeatureExtractor(_dataAvgBySecHR[_s:_e])
                                    extraFeatures.append(hrfe.extract())
                            if(ibi):
                                if  len(_dataAvgBySecIBI[_s:_e]) > 0:
                                    ibife = IBIFeatureExtractor(_dataAvgBySecIBI[_s:_e])
                                    extraFeatures.append(ibife.extract())
                            if(temp):
                                if  len(_dataAvgBySecTEMP[_s:_e]) > 0:
                                    tempfe = TEMPFeatureExtractor(_dataAvgBySecTEMP[_s:_e])
                                    extraFeatures.append(tempfe.extract())
                            _line = str(_l)
                            if( len(extraFeatures) > 0):
                                for _t in extraFeatures:
                                    _line += ","+ ",".join(str(_x) for _x in _t)
                                print _line
                            #print _line

if (__name__ == "__main__"):

		s = session("p9/sandra_relax/1434150573545/")
		plotGSR("p9/sandra_relax","sandra_relax_GSR",s,_limy=[0.0,1.0])
		plotHR_ZEPHYR("p9/sandra_relax","sandra_relax_HR",s,_limy=[0,120])
                getFeaturesFrom(s)

		s = session("p9/sandra_relax3/1435619278734/")
		plotGSR("p9/sandra_relax3","sandra_relax3_GSR",s,_limy=[0.0,1.0])
		plotHR_ZEPHYR("p9/sandra_relax3","sandra_relax3_HR",s,_limy=[0,120])
                getFeaturesFrom(s)

                s = session("p7/alfonso_relax/1434064078558/")
                plotGSR("p7/alfonso_relax","alfonso_relax_GSR",s,_limy=[0.0,20.0])
                getFeaturesFrom(s)
                ######session2###################
                #s = session("p7/alfonso_relax2/1434495734670/")
                getFeaturesFrom(s)
                s = session("p7/alfonso_relax3/1435275565320/")
                plotGSR("p7/alfonso_relax3","alfonso_relax3_GSR",s,_limy=[0.0,20.0])
                plotHR_ZEPHYR("p7/alfonso_relax3","alfonso_relax3_HR",s,_limy=[0,120])
                getFeaturesFrom(s)
                ###
                s = session("p5/alma_rest/1433977560736/")
                getFeaturesFrom(s)
		
