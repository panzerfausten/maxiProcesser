from MyPlotter import MyPlotter
from maxi import session
from sklearn import preprocessing

def plotGSR(subject,sessionpath,):
	u = u'\u00B5'
        s = session(sessionpath)
	_data_to_norm = []
	min_max_scaler = preprocessing.MinMaxScaler()
	for _x in s._dataGSR:
		_data_to_norm.append(_x[1])

	_data_normalized = min_max_scaler.fit_transform(_data_to_norm)
 
        _title_raw = "GSR: [%s,sample,raw]" % (subject)
        _title_norm = "GSR: [%s,sample,raw]" % (subject)
	_path_raw = "%s/plots/n5_sample_GSR_raw" % (subject)
	_path_norm = "%s/plots/%s_sample_GSR_normalized" % (subject)

	m = MyPlotter(_title_raw,_data_to_norm,"Seconds","Avg Value "+u,)
        m.plot(_path_raw)

	m = MyPlotter("GSR [n5,sample,normalized]",_data_normalized,"Seconds","Avg Value "+u)
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
	_script_file.close()
if (__name__ == "__main__"):
	plotGSR("n5/n5_sample/1425492334386/","n5")
	plotGSR("n5/n5_1/1425492729555/","n5")
	plotGSR("n5/n5_2/1425494040887/","n5")
	plotGSR("n5/n5_3/1425495483937/","n5")
	generateMergeScript("n5","n5/plots")
