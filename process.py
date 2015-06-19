from MyPlotter import MyPlotter
from maxi import session
from sklearn import preprocessing
import numpy as np
from HalfRecoveryTimeDetector import HalfRecoveryTimeDetector
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
		m = MyPlotter(_title_raw,_dataToPlot,"Seconds","Value "+u,color='blue',limx=_limx,limy=_limy,codification=s._dataCODIFICATION,_xTick=200,_yTick=1)
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
def plotHR_ZEPHYR(subject,test,session, sounds = [],_limx=None,_limy=None,groupBySec=False):
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
	if(groupBySec):
		m = MyPlotter(_title_raw,_dataAvgBySec,"Seconds","Value (BPM) ",limx=_limx,limy=_limy,_xTick=200,_yTick=20)
	else:
		m = MyPlotter(_title_raw,_data_to_norm,"Seconds","Value (BPM) ",limx=_limx,limy=_limy,_xTick=200,_yTick=20)
		m.plot(_path_raw)
	
	#m = MyPlotter(_title_norm,_data_normalized,"Seconds","Value (C)",[50,100])
        #m.plot(_path_norm)  not norm by now
def plotIBI_ZEPHYR(subject,test,session, sounds = [],_limx=None,_limy=None,groupBySec=True):
        s = session
        _data_to_norm = []
        min_max_scaler = preprocessing.MinMaxScaler()
        for _x in s._dataZEPHYR_IBI:
                _data_to_norm.append(_x[1])

        _dataAvgBySec = s.groupBySec(s._dataZEPHYR_IBI,False,True)
        #_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
        _title_raw = "IBI: [%s,%s,raw]" % (subject,test)
        #_title_norm = "HR: [%s,%s,normalized]" % (subject,test)

        _path_raw = "%s/plots/%s_%s_IBI_raw" % (subject,subject,test)
        #_path_norm = "%s/plots/%s_%s_HR_normalized" % (subject,subject,test)
        if (s._dataSOUNDS != None):
                if(groupBySec):
                        m = MyPlotter(_title_raw,_dataAvgBySec,"Seconds","Value (seconds) ",limx=_limx,limy=_limy,sounds=s.toSecSounds(),_xTick=200,_yTick=1.0)
                else:
                        m = MyPlotter(_title_raw,_data_to_norm,"Seconds","Value (seconds) ",limx=_limx,limy=_limy,sounds=s.toSecSounds(),_xTick=200,_yTick=1.0,_yTickMinor=0.1)
        elif (s._dataCODIFICATION != None):
                if(groupBySec):
                        m = MyPlotter(_title_raw,_dataAvgBySec,"Seconds","Value (seconds) ",limx=_limx,limy=_limy,codification=s._dataCODIFICATION,_xTick=200,_yTick=2.0,_yTickMinor=0.1)
                else:
                        m = MyPlotter(_title_raw,_data_to_norm,"Seconds","Value (seconds) ",limx=_limx,limy=_limy,codification=s._dataCODIFICATION,_xTick=200,_yTick=2.0,_yTickMinor=0.1)

        else:
                if(groupBySec):
                        m = MyPlotter(_title_raw,_dataAvgBySec,"Seconds","Value (seconds) ",limx=_limx,limy=_limy,_xTick=200,_yTick=2.0,_yTickMinor=0.1)
                else:
                        m = MyPlotter(_title_raw,_data_to_norm,"Seconds","Value (seconds)",limx=_limx,limy=_limy,_xTick=200,_yTick=2.0,_yTickMinor=0.1)

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

		_album.write(" okular albumGSR.pdf\n")
if (__name__ == "__main__"):
                ######p1 and p2###################
                s = session("p1/carlos_S1_R1/1433807211979/")
		plotGSR("p1/carlos_S1_R1","carlos_S1_R1_GSR",s,_limy=[0.0,10.0])
		plotTEMP("p1/carlos_S1_R1","carlos_S1_R1_TEMP",s,_limy=[30,40])
                plotHR_ZEPHYR("p1/carlos_S1_R1","carlos_HR",s,_limy=[0,120],_limx=[0,2000])
                plotIBI_ZEPHYR("p1/carlos_S1_R1","carlos_IBI",s,_limy=[0.4,1],_limx=[0,2000])
                _data = s.groupBySec(s._dataGSR,True,False)
                htr = HalfRecoveryTimeDetector(_data)
		htr.plot("p1/carlos_S1_R1/plots/carlos_S1_R1_HTR")
        	###############session2
		s = session("p1/carlos_relax2/1434411781135/")
		plotGSR("p1/carlos_relax2","carlos_relax2_GSR",s,_limy=[0.0,10.0])
		plotTEMP("p1/carlos_relax2","carlos_relax2_TEMP",s,_limy=[30,40])
                plotHR_ZEPHYR("p1/carlos_relax2","carlos_relax2_HR",s,_limy=[0,120],_limx=[0,2000])
                plotIBI_ZEPHYR("p1/carlos_relax2","carlos_relax2_IBI",s,_limy=[0.4,1],_limx=[0,2000])
                _data = s.groupBySec(s._dataGSR,True,False)
                htr = HalfRecoveryTimeDetector(_data)
		htr.plot("p1/carlos_relax2/plots/p1/carlos_relax2_htr")

		s = session("p2/eduardo/1433809471952/")
		plotGSR("p2/eduardo","eduardo_GSR",s,_limy=[0.0,10.0])
		plotTEMP("p2/eduardo","eduardo_TEMP",s,_limy=[30,40])
		plotHR_ZEPHYR("p2/eduardo","eduardo_HR",s,_limy=[0.0,120])
		plotIBI_ZEPHYR("p2/eduardo","eduardo_IBI",s,_limy=[0.4,1])
		_data = s.groupBySec(s._dataGSR,True,False)
		htr = HalfRecoveryTimeDetector(_data)
		htr.plot("p2/eduardo/plots/eduardo_HTR")

                ######p3 and p4###################
        	s = session("p3/karime_T1/1433892485204/")
		plotGSR("p3/karime_T1","karime_T1_GSR",s,_limy=[0.0,10.0])
		plotTEMP("p3/karime_T1","karime_T1_TEMP",s,_limy=[30,40])
		plotHR_ZEPHYR("p3/karime_T1","karime_T1_HR",s,_limy=[0,120])
		plotIBI_ZEPHYR("p3/karime_T1","karime_T1_IBI",s,_limy=[0.4,1])
                _data = s.groupBySec(s._dataGSR,True,False)
                htr = HalfRecoveryTimeDetector(_data)
                htr.plot("p3/karime_T1/plots/karime_T1_TEMP")

        	s = session("p3/karime_relax2/1434498836908/")
		plotGSR("p3/karime_relax2","karime_relax2_GSR",s,_limy=[0.0,10.0])
		plotTEMP("p3/karime_relax2","karime_relax2_TEMP",s,_limy=[30,40])
		plotHR_ZEPHYR("p3/karime_relax2","karime_relax2_HR",s,_limy=[0,120])
		plotIBI_ZEPHYR("p3/karime_relax2","karime_relax2_IBI",s,_limy=[0.4,1])
                _data = s.groupBySec(s._dataGSR,True,False)
                htr = HalfRecoveryTimeDetector(_data)
                htr.plot("p3/karime_relax2/plots/karime2_htr")


                ######session2###################
                s = session("p4/celia_rest/1433894624813/")
		plotGSR("p4/celia_rest","celia_rest_GSR",s,_limy=[0.0,10.0])
                plotTEMP("p4/celia_rest","celia_rest_TEMP",s,_limy=[30,40.0])
		plotHR_ZEPHYR("p4/celia_rest","celia_rest_HR",s,_limy=[0,120])
		plotIBI_ZEPHYR("p4/celia_rest","celia_rest_IBI",s,_limy=[0.4,1])
                _data = s.groupBySec(s._dataGSR,True,False)
                htr = HalfRecoveryTimeDetector(_data)
                htr.plot("p4/celia_rest/plots/celia_HTR")
                ######p5 and p6###################
        	s = session("p5/alma_rest/1433977560736/")
		plotGSR("p5/alma_rest","alma_rest_GSR",s,_limy=[0.0,10.0])
		plotTEMP("p5/alma_rest","alma_rest_TEMP",s,_limy=[30,40])
		plotHR_ZEPHYR("p5/alma_rest","alma_rest_HR",s,_limy=[0,120])
		plotIBI_ZEPHYR("p5/alma_rest","alma_rest_IBI",s,_limy=[0.4,1])
                _data = s.groupBySec(s._dataGSR,True,False)
                htr = HalfRecoveryTimeDetector(_data)
                htr.plot("p5/alma_rest/plots/alma_rest_htr")


        	s = session("p6/luis_relax/1433979780288/")
		plotGSR("p6/luis_relax","luis_relax_GSR",s,_limy=[0.0,20.0])
		plotTEMP("p6/luis_relax","luis_relax_TEMP",s,_limy=[30,40])
		plotHR_ZEPHYR("p6/luis_relax","luis_relax_HR",s,_limy=[0,120])
		plotIBI_ZEPHYR("p6/luis_relax","luis_relax_IBI",s,_limy=[0.4,1])
                _data = s.groupBySec(s._dataGSR,True,False)
                htr = HalfRecoveryTimeDetector(_data)
                htr.plot("p6/luis_relax/plots/luis_relax_HTR",_ylim=[0,15])


        	s = session("p6/luismiguel_relax2/1434671046538/")
		plotGSR("p6/luismiguel_relax2","luismiguel_relax2_GSR",s,_limy=[0.0,20.0])
		plotTEMP("p6/luismiguel_relax2","luismiguel_relax2_TEMP",s,_limy=[30,40])
		plotHR_ZEPHYR("p6/luismiguel_relax2","luismiguel_relax2_HR",s,_limy=[0,120])
		plotIBI_ZEPHYR("p6/luismiguel_relax2","luismiguel_relax2_IBI",s,_limy=[0,1.5])
                _data = s.groupBySec(s._dataGSR,True,False)
                htr = HalfRecoveryTimeDetector(_data)
                htr.plot("p6/luismiguel_relax2/plots/luis_relax_HTR",_ylim=[0,15])

                ######p7 and p8###################
		s = session("p7/alfonso_relax/1434064078558/")
		plotGSR("p7/alfonso_relax","alfonso_relax_GSR",s,_limy=[0.0,20.0])
		plotTEMP("p7/alfonso_relax","alfonso_TEMP",s,_limy=[30,40])
		plotHR_ZEPHYR("p7/alfonso_relax","alfonso_relax_HR",s,_limy=[0,120])
		plotIBI_ZEPHYR("p7/alfonso_relax","alfonso_relax_IBI",s,_limy=[0.4,1])
                _data = s.groupBySec(s._dataGSR,True,False)
                htr = HalfRecoveryTimeDetector(_data)
                htr.plot("p7/alfonso_relax/plots/alfonso_relax_htr",_ylim=[0,20])

                ######session2###################
		s = session("p7/alfonso_relax2/1434495734670/")
		plotGSR("p7/alfonso_relax2","alfonso_relax2_GSR",s,_limy=[0.0,20.0])
		plotTEMP("p7/alfonso_relax2","alfonso_relax2_TEMP",s,_limy=[30,40])
		plotHR_ZEPHYR("p7/alfonso_relax2","alfonso_relax2_HR",s,_limy=[0,120])
		plotIBI_ZEPHYR("p7/alfonso_relax2","alfonso_relax2_IBI",s,_limy=[0.4,1])
                _data = s.groupBySec(s._dataGSR,True,False)
                htr = HalfRecoveryTimeDetector(_data)
                htr.plot("p7/alfonso_relax2/plots/alfonso_relax2_htr",_ylim=[0,20])



		s = session("p8/angello_relax/1434066549276/")
		plotGSR("p8/angello_relax","angello_relax_GSR",s,_limy=[0.0,10.0])
		plotTEMP("p8/angello_relax","angello_relax_TEMP",s,_limy=[30,40])
		plotHR_ZEPHYR("p8/angello_relax","angello_relax_HR",s,_limy=[0,120])
		plotIBI_ZEPHYR("p8/angello_relax","angello_relax_IBI",s,_limy=[0.4,1])
                _data = s.groupBySec(s._dataGSR,True,False)
                htr = HalfRecoveryTimeDetector(_data)
                htr.plot("p8/angello_relax/plots/angello_relax_HTR")
	
		s = session("p8/angello_relax2/1434668094145/")
		plotGSR("p8/angello_relax2","angello_relax2_GSR",s,_limy=[0.0,10.0])
		plotTEMP("p8/angello_relax2","angello_relax2_TEMP",s,_limy=[30,40])
		plotHR_ZEPHYR("p8/angello_relax2","angello_relax2_HR",s,_limy=[0,150])
		plotIBI_ZEPHYR("p8/angello_relax2","angello_relax2_IBI",s,_limy=[0,1.5])
                _data = s.groupBySec(s._dataGSR,True,False)
                htr = HalfRecoveryTimeDetector(_data)
                htr.plot("p8/angello_relax2/plots/angello_relax2_HTR")
		
	
		s = session("p9/sandra_relax/1434150573545/")
		plotGSR("p9/sandra_relax","sandra_relax_GSR",s,_limy=[0.0,10.0])
		plotTEMP("p9/sandra_relax","sandra_relax_TEMP",s,_limy=[30,40])
		plotHR_ZEPHYR("p9/sandra_relax","sandra_relax_HR",s,_limy=[0,120])
		plotIBI_ZEPHYR("p9/sandra_relax","sandra_relax_IBI",s,_limy=[0.4,1])
                _data = s.groupBySec(s._dataGSR,True,False)
                htr = HalfRecoveryTimeDetector(_data)
                htr.plot("p9/sandra_relax/plots/sandra_relax_HTR")
		
		s = session("p10/mirna_relax/1434153018088/")
		plotGSR("p10/mirna_relax","mirna_relax_GSR",s,_limy=[0.0,10.0])
		plotTEMP("p10/mirna_relax","mirna_relax_TEMP",s,_limy=[30,40])
		plotHR_ZEPHYR("p10/mirna_relax","mirna_relax_HR",s,_limy=[0,120])
		plotIBI_ZEPHYR("p10/mirna_relax","mirna_relax_IBI",s,_limy=[0.4,1])
                _data = s.groupBySec(s._dataGSR,True,False)
                htr = HalfRecoveryTimeDetector(_data)
                htr.plot("p10/mirna_relax/plots/mirna_relax_HTR",[0,10])
		##############session2
		s = session("p10/mirna_relax2/1434409029312/")
		plotGSR("p10/mirna_relax2","mirna_relax2_GSR",s,_limy=[0.0,10.0])
		plotTEMP("p10/mirna_relax2","mirna_relax2_TEMP",s,_limy=[30,40])
		plotHR_ZEPHYR("p10/mirna_relax2","mirna_relax2_HR",s,_limy=[0,120])
		plotIBI_ZEPHYR("p10/mirna_relax2","mirna_relax2_IBI",s,_limy=[0.4,1])
                _data = s.groupBySec(s._dataGSR,True,False)
                htr = HalfRecoveryTimeDetector(_data)
                htr.plot("p10/mirna_relax2/plots/mirna_relax_HTR",[0,10])
