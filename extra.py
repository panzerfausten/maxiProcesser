from MyPlotter import MyPlotter
from maxi import session
from sklearn import preprocessing

def plotGSR(subject,test,sessionpath):
	u = u'\u00B5'
        s = session(sessionpath)
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()

	_dataAvgBySec = s.groupBySec(s._dataGSR,True,False)
	#for _x in _dataAvgBySec:
	#	_data_to_norm.append(_x[])
	
	#_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
 
        _title_raw = "GSR: [%s,%s,raw]" % (subject,test)
	_title_norm = "GSR: [%s,%s,normalized]" % (subject,test)

	_path_raw = "%s/plots/%s_%s_GSR_raw" % (subject,subject,test)
	_path_norm = "%s/plots/%s_%s_GSR_normalized" % (subject,subject,test)
	m = MyPlotter(_title_raw,_dataAvgBySec,"Seconds","Value "+u,color='blue')
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

def plotHR_ZEPHYR(subject,test,sessionpath, sounds = []):
        s = session(sessionpath)
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	for _x in s._dataZEPHYR_HR:
		_data_to_norm.append(_x[1])

	#_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
 
        _title_raw = "HR: [%s,%s,raw]" % (subject,test)
	#_title_norm = "HR: [%s,%s,normalized]" % (subject,test)

	_path_raw = "%s/plots/%s_%s_HR_raw" % (subject,subject,test)
	#_path_norm = "%s/plots/%s_%s_HR_normalized" % (subject,subject,test)
	m = MyPlotter(_title_raw,_data_to_norm,"Seconds","Value (C)",[50,100])
        m.plot(_path_raw)
	
	#m = MyPlotter(_title_norm,_data_normalized,"Seconds","Value (C)",[50,100])
        #m.plot(_path_norm)  not norm by now

def generateMergeScript(subject,path):
	_baseGSR = "montage -geometry +1+1 %s_sample_GSR_raw.png  %s_sample_HR_raw.png %s_t1_GSR_raw.png %s_t1_HR_raw.png %s_t2_GSR_raw.png %s_t2_HR_raw.png %s_t3_GSR_raw.png %s_t3_HR_raw.png out.png\n"
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
		_album.write("pdftk ")
		for _subject in subjects:
			_album.write(" %s/plots/plots_GSR_HR_%s.pdf " %(_subject,_subject))
		_album.write(" output albumGSR.pdf\n")
		
		_album.write("\npdftk ")
		for _subject in subjects:
			_album.write(" %s/plots/plots_TEMP_%s.pdf " %(_subject,_subject))
		_album.write(" output albumTEMP.pdf\n")

if (__name__ == "__main__"):

	plotGSR("l1","t1","l1/l1_1/1427146438281/")
	plotGSR("l1","t2","l1/l1_2/1427147325779/")
	plotGSR("l1","t3","l1/l1_3/1427148713649/")
	plotGSR("l1","pre","l1/l1_pre/1427145620546/")
	

	plotGSR("l2","sample","l2/l2_sample/1427150028457/")
	plotGSR("l2","t1","l2/l2_1/1427150551647/")



	"""	plotGSR("e1","sample","e1/e1_sample/1426786584466/")
	plotHR_ZEPHYR("e1","sample","e1/e1_sample/1426786584466/")

	plotGSR("e1","e1","e1/e1/1426787101660/")
	plotHR_ZEPHYR("e1","e1","e1/e1/1426787101660/") 


	plotGSR("e2","sample","e2/e2_sample/1426792734905/")
#	plotHR_ZEPHYR("e2","sample","e2/e2_sample/1426792734905/")

	plotGSR("e2","t1","e2/e2_1/1426793287098/")
#	plotHR_ZEPHYR("e2","t2","e2/e2_1/1426793287098")

	plotGSR("e2","t2","e2/e2_2/1426794614764/")



	plotGSR("e3","sample","e3/e3_sample/1426797372598/")
	plotGSR("e3","t1","e3/e3_1_1/1426798177954/")
	plotGSR("e3","t2","e3/e3_2/1426798902171/")
	generateMergeScript("e1","e1/plots") 

	"""
generateAlbumScript(["e1"])
