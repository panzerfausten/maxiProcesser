from MyPlotter import MyPlotter
from maxi import session
from sklearn import preprocessing

def plotGSR(subject,test,sessionpath):
	u = u'\u00B5'
        s = session(sessionpath)
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	for _x in s._dataGSR:
		_data_to_norm.append(_x[1])

	_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
 
        _title_raw = "GSR: [%s,%s,raw]" % (subject,test)
	_title_norm = "GSR [%s,%s,normalized]" % (subject,test)

	_path_raw = "%s/plots/%s_%s_GSR_raw" % (subject,subject,test)
	_path_norm = "%s/plots/%s_%s_GSR_normalized" % (subject,subject,test)
	m = MyPlotter(_title_raw,_data_to_norm,"Seconds","Avg Value "+u,)
        m.plot(_path_raw)
	
	m = MyPlotter(_title_norm,_data_normalized,"Seconds","Avg Value "+u)
        m.plot(_path_norm) 



def plotSample():
	u = u'\u00B5'
        s = session("n5/n5_sample/1425492334386/")
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	for _x in s._dataGSR:
		_data_to_norm.append(_x[1])

	_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
        
	m = MyPlotter("GSR: [n5,sample,raw]",_data_to_norm,"Seconds","Avg Value "+u,)
        m.plot("n5/plots/n5_sample_GSR_raw")
	m = MyPlotter("GSR [n5,sample,normalized]",_data_normalized,"Seconds","Avg Value "+u)
        m.plot("n5/plots/n5_sample_GSR_normalized") 

def plotT1():
	u = u'\u00B5'
        s = session("n5/n5_1/1425492729555/")
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	for _x in s._dataGSR:
		_data_to_norm.append(_x[1])

	_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
        
	m = MyPlotter("GSR: [n5,T1,raw]",_data_to_norm,"Seconds","Avg Value "+u,)
        m.plot("n5/plots/n5_t1_GSR_raw")
	m = MyPlotter("GSR [n5,T1,normalized]",_data_normalized,"Seconds","Avg Value "+u)
        m.plot("n5/plots/n5_t1_GSR_normalized") 


def plotT2():
	u = u'\u00B5'
        s = session("n5/n5_2/1425494040887/")
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	for _x in s._dataGSR:
		_data_to_norm.append(_x[1])

	_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
        
	m = MyPlotter("GSR: [n5,T2,raw]",_data_to_norm,"Seconds","Avg Value "+u,)
        m.plot("n5/plots/n5_t2_GSR_raw")
	m = MyPlotter("GSR [n5,T2,normalized]",_data_normalized,"Seconds","Avg Value "+u)
        m.plot("n5/plots/n5_t2_GSR_normalized") 


def plotT3():
	u = u'\u00B5'
        s = session("n5/n5_3/1425495483937/")
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	for _x in s._dataGSR:
		_data_to_norm.append(_x[1])

	_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
        
	m = MyPlotter("GSR: [n5,T3,raw]",_data_to_norm,"Seconds","Avg Value "+u,)
        m.plot("n5/plots/n5_t3_GSR_raw")
	m = MyPlotter("GSR [n5,T3,normalized]",_data_normalized,"Seconds","Avg Value "+u)
        m.plot("n5/plots/n5_t3_GSR_normalized") 

def generateMergeScript(subject,path):
	_base = "montage -geometry +1+1 %s_sample_GSR_raw.png  %s_sample_GSR_normalized.png %s_t1_GSR_raw.png %s_t1_GSR_normalized.png %s_t2_GSR_raw.png %s_t2_GSR_normalized.png %s_t3_GSR_raw.png %s_t3_GSR_normalized.png out.png\n"
	_toPdf = "convert out.png plots_%s.pdf"  % (subject)
	with open(path+"/merge.sh","w") as _script_file:
		_base = _base % ( (subject,)*8)
		_script_file.write(_base )
		_script_file.write(_toPdf)
		_script_file.write("\nrm out.png")
	_script_file.close()
def generateAlbumScript(subjects):
	with open("album.sh","w") as _album:
		_album.write("pdftk ")
		for _subject in subjects:
			_album.write(" %s/plots/plots_%s.pdf " %(_subject,_subject))
		_album.write(" output album.pdf")
	
if (__name__ == "__main__"):
	#N2
	plotGSR("n2","sample","n2/n2_sample/1425405680330/")
	plotGSR("n2","t1","n2/n2_1/1425406094608/")
	plotGSR("n2","t2","n2/n2_2/1425407232389/")
	plotGSR("n2","t3","n2/n2_3/1425408677098/")
	generateMergeScript("n2","n2/plots") 
	#N3
	plotGSR("n3","sample","n3/n3_sample/1425409979748/")
	plotGSR("n3","t1","n3/n3_1/1425410684040/")
	plotGSR("n3","t2","n3/n3_2/1425411806445/")
	plotGSR("n3","t3","n3/n3_3/1425413219572/")
	generateMergeScript("n3","n3/plots") 
	#N4
	plotGSR("n4","sample","n4/n4_sample/1425424011391/")
	plotGSR("n4","t1","n4/n4_1/1425424406612/")
	plotGSR("n4","t2","n4/n4_2/1425425734089/")
	plotGSR("n4","t3","n4/n4_3/1425427210413/")
	generateMergeScript("n4","n4/plots") 
	#N5
	plotGSR("n5","sample","n5/n5_sample/1425492334386/")
	plotGSR("n5","t1","n5/n5_1/1425492729555/")
	plotGSR("n5","t2","n5/n5_2/1425494040887/")
	plotGSR("n5","t3","n5/n5_3/1425495483937/")
	generateMergeScript("n5","n5/plots") 
	#N6
	plotGSR("n6","sample","n6/n6_sample/1425518091729/")
	plotGSR("n6","t1","n6/n6_1/1425518500874/")
	plotGSR("n6","t2","n6/n6_2/1425519830146/")
	plotGSR("n6","t3","n6/n6_3/1425521315634/")
	generateMergeScript("n6","n6/plots") 
	#N7
	plotGSR("n7","sample","n7/n7_sample/1425684948845/")
	plotGSR("n7","t1","n7/n7_1/1425685387543/")
	plotGSR("n7","t2","n7/n7_2/1425686709300/")
	plotGSR("n7","t3","n7/n7_3/1425688159174/")
	generateMergeScript("n7","n7/plots") 
	#N8
	plotGSR("n8","sample","n8/n8_sample/1425922143000/")
	plotGSR("n8","t1","n8/n8_1/1425922672389/")
	plotGSR("n8","t2","n8/n8_2/1425923390965/")
	plotGSR("n8","t3","n8/n8_3/1425924781341/")
	generateMergeScript("n8","n8/plots") 

	generateAlbumScript(["n2","n3","n4","n5","n6","n7","n8"])
