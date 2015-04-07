from MyPlotter import MyPlotter
from maxi import session
from sklearn import preprocessing

def plotGSR(subject,test,sessionpath,_limx=None,_limy=None,_groupBySec=False):
	u = u'\u00B5'
        s = session(sessionpath)
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

def plotHR_ZEPHYR(subject,test,sessionpath, sounds = [],_limx=None,_limy=None,groupBySec=False):
        s = session(sessionpath)
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
		m = MyPlotter(_title_raw,_dataAvgBySec,"Seconds","Value (BPM) ",limx=_limx,limy=_limy)
	else:
		m = MyPlotter(_title_raw,_data_to_norm,"Seconds","Value (BPM) ",limx=_limx,limy=_limy)
		
        m.plot(_path_raw)
	
	#m = MyPlotter(_title_norm,_data_normalized,"Seconds","Value (C)",[50,100])
        #m.plot(_path_norm)  not norm by now

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
	plotGSR("l1","pre","l1/l1_pre/1427145620546/",_limy=[0.35,1.05])
	plotHR_ZEPHYR("l1","pre","l1/l1_pre/1427145620546/",_limy=[35,100] )
	plotGSR("l1","t1","l1/l1_1/1427146438281/",_limy=[0.35,1.05])
	plotHR_ZEPHYR("l1","t1","l1/l1_1/1427146438281/",_limy=[35,100] )
	plotGSR("l1","t2","l1/l1_2/1427147325779/",_limx=[0,1200],_groupBySec=True,_limy=[0.35,1.05])
	### For Academic Purposes
	plotGSR("l1","t2_ng","l1/l1_2/1427147325779/",_groupBySec=False,_limy=[0.35,1.05])
	### 
	plotHR_ZEPHYR("l1","t2","l1/l1_2/1427147325779/",_limx=[0,1200],_limy=[35,100] )
	plotGSR("l1","t3","l1/l1_3/1427148713649/",_limx=[0,120],_limy=[0.35,1.05])
	plotHR_ZEPHYR("l1","t3","l1/l1_3/1427148713649/",_limx=[0,120],_limy=[35,100] )
	generateMergeScript("l1","l1/plots")
		
	plotGSR("l2","sample","l2/l2_sample/1427150028457/",_limx=[0,300],_limy=[0.35,1.05])
	plotHR_ZEPHYR("l2","sample","l2/l2_sample/1427150028457/",_limx=[0,300],_limy=[35,100] )
	plotGSR("l2","t1","l2/l2_1/1427150551647/",_limx=[0,1200],_limy=[0.35,1.05])
	plotHR_ZEPHYR("l2","t1","l2/l2_1/1427150551647/",_limx=[0,1200],_limy=[35,100] )
	plotGSR("l2","t2","l2/l2_2/1427152284131/",_limx=[0,1200],_limy=[0.35,1.05])
	plotHR_ZEPHYR("l2","t2","l2/l2_2/1427152284131/",_limx=[0,1200],groupBySec=True)
	plotGSR("l2","t3","l2/l2_3/1427153781978/",_limx=[0,120],_limy=[0.35,1.05])
	plotHR_ZEPHYR("l2","t3","l2/l2_3/1427153781978/",_limx=[0,120],_limy=[35,100] )
	generateMergeScript("l2","l2/plots")
	
	plotGSR("l3","sample","l3/l3_sample/1427156710381/",_limx=[0,300],_limy=[0.35,1.05])
	plotHR_ZEPHYR("l3","sample","l3/l3_sample/1427156710381/",_limx=[0,300],groupBySec=False,_limy=[35,100] )
	plotGSR("l3","t1","l3/l3_1/1427157308300/",_limx=[0,1200],_limy=[0.35,1.05])
	plotHR_ZEPHYR("l3","t1","l3/l3_1/1427157308300/",_limx=[0,1200],_limy=[35,100] )
	plotGSR("l3","t2","l3/l3_2/1427159032942/",_limx=[0,1200],_limy=[0.35,1.05])
	plotHR_ZEPHYR("l3","t2","l3/l3_2/1427159032942/",_limx=[0,1200],_limy=[35,100] )
	plotGSR("l3","t3","l3/l3_3/1427160538271/",_limx=[0,120],_limy=[0.35,1.05])
	plotHR_ZEPHYR("l3","t3","l3/l3_3/1427160538271/",_limx=[0,120],_limy=[35,100] )
	generateMergeScript("l3","l3/plots")
	
	generateAlbumScript(["l1","l2","l3"])
