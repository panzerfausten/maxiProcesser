from maxi import session
from SessionUtils import SessionUtils
####open session files
s_sample = session("n2/n2_sample/1425405680330/")
_grouped_sample = s_sample.groupBySec(s_sample._dataGSR,True,False)

s_t1 = session("n2/n2_1/1425406094608/")
_grouped_t1 = s_t1.groupBySec(s_t1._dataGSR,True,False)

s_t2 = session("n2/n2_2/1425407232389/")
_grouped_t2 = s_t2.groupBySec(s_t2._dataGSR,True,False)
##### NORMALIZE AND THEN SEGMENTATE SAMPLE
_su = SessionUtils(s_sample)
_g_noNones_sample = _su.removeNones(_grouped_sample)
_normalized_sample  = s_sample.normalize(_g_noNones_sample)
_segments_sample = _su.segmentateData(_normalized_sample)
##### NORMALIZE AND THEN SEGMENTATE T1
_su = SessionUtils(s_t1)
_g_noNones_t1 =  _su.removeNones(_grouped_t1)
_normalized_t1  = s_t1.normalize(_g_noNones_t1)
_segments_t1 = _su.segmentateData(_normalized_t1)
##### NORMALIZE AND THEN SEGMENTATE T1
_su = SessionUtils(s_t2)
_g_noNones_t2 =  _su.removeNones(_grouped_t2)
_normalized_t2  = s_t2.normalize(_g_noNones_t2)
_segments_t2 = _su.segmentateData(_normalized_t2)




##############################MACHINE LEARNING
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn import cross_validation
import numpy as np
#Labels [y]
#0,0 = no anxiety
#1,1 = aanxiety
#print _segments_sample
X = np.array( [_segments_sample[0],_segments_t1[0],_segments_t2[0]])
y = [0,1,2]
clf = svm.SVC(kernel='linear', C=1.0)
y_pred = clf.fit(X, y)
#print len(_segments_sample), len(_segments_t1), len(_segments_t2)

results = []
r = []
for _x, _segment in enumerate(_segments_sample):
	r.append( clf.predict(_segment))
results.append(r)
r = []
for _x, _segment in enumerate(_segments_t1):
	r.append(clf.predict(_segment))

results.append(r)
r = []

for _x, _segment in enumerate(_segments_t2):
	r.append(clf.predict(_segment))
results.append(r)
r = []

######################SAVE TO DISK
with open("results.txt","w") as _file:
	for r in results:
		for _v in r:
			_file.write(str(_v))
		_file.write("\n")
