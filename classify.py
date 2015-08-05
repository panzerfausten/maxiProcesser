from sklearn import svm
from random import shuffle
import sys
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn import cross_validation
from sklearn import preprocessing
from sklearn.preprocessing import normalize
import numpy as np
import matplotlib.pyplot as plt
def readFile(_F):
    with open(_F,"r") as _FILE:
        _lines = _FILE.readlines()
        _dataA = []
        _dataB = []
        _dataC = []
        _dataD = []
        for _l in _lines:
            _line = _l.replace("\n","").split(",")
            _lineF = convertLine(_line)
            if (_lineF[0] == 0):
                _dataA.append(_lineF)
            elif (_lineF[0] == 1):
                _dataB.append(_lineF)
            elif (_lineF[0] == 2):
                _dataC.append(_lineF)
            elif (_lineF[0] == 3):
                _dataD.append(_lineF)
        return _dataA,_dataB
def convertLine(_line):
    _l = []
    for _x in range(0,len(_line)):
        if _x == 0:
            _l.append( int(_line[_x]))
        else:
            if (_line[_x] == "None"):
                _l.append(0.0)
            else:
                _l.append( float(_line[_x]))
    return _l
def takeSample(_maxSample,_s=0):
    #at this point, the samples are sorted
    _nm_A =    _dataA[_s:_maxSample+_s,:] 
    _nm_B = _dataB[_s:_maxSample+_s,:]
    _X = []
    for _x, _nm in enumerate(_nm_A):
        if(_x <= _maxSample):
            _X.append(_nm.tolist())
        else:
            break
    #print len(_nm_A.tolist())," ",len(_nm_B.tolist())
    for _x, _nm in enumerate(_nm_B):
        if(_x <= _maxSample):
            _X.append(_nm.tolist())
        else:
            break
    _y =    [0]*_maxSample + [1]*_maxSample
    return _X,_y
def removeLabel(_data,_tag=False):
    _dataNolabel = []
    for _d in _data:
        if(_tag):
            _dataNolabel.append(_d[1:])
        else:
            _dataNolabel.append([_d[0],_d[1:]])
    return _dataNolabel
def plot(_X,_y,_clf):
    _X = np.array(_X)
    plt.scatter(_X[:,2],_X[:,3],c =_y)
    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(0,12)
    yy = a * xx - clf.intercept_[0] / w[1]
    h0 = plt.plot(xx, yy, 'k-', label="non weighted div")
    plt.savefig("svm")
def validateVector(vector):
    _len = len(vector[0])
    for _x, _v in enumerate(vector):
        if (len(_v) != _len):
            raise Exception("Invalid Feature Vector. All lines MUST to have the same lenght. (Line: %i)" %(_x))

def randomiceData(data):
        for d in data:
                shuffle(d)
def normalize(_dataA,_dataB):
    x = np.array(_dataA+_dataB)
    _resA = x[:len(_dataA),:]
    _resB = x[len(_dataA):,:]
    norm1 = x / np.linalg.norm(x)
    #norm2 = normalize(x[:,np.newaxis], axis=0).ravel()
    return _resA,_resB
def saveSet(_setA,_setB):
    with open("optimalSet.csv","w") as _os:
        for _x,_l in enumerate(_setA):
            _v = str(_setB[_x])+","+",".join(map(str,(_l)))
            _os.write(_v+"\n")
def calcProportion(_p=.8):
    _lenA = len(_dataA)
    _lenB = len(_dataB)
    if(_lenA <= _lenB):
        _training = int(_lenA*_p)
        _testing  = _lenA - _training
    else:
        _training = int(_lenB*_p)
        _testing  = _lenB - _training
    return _training,_testing
if __name__ == "__main__":
    _file_path = sys.argv[1]
    _csv = False
    try:
        _csvRequest = sys.argv[2]
        if("csv" in _csvRequest):
            _csv = True
    except:
            pass
    _dataA,_dataB  = readFile(_file_path)
    _dataA = removeLabel(_dataA,True)
    _dataB = removeLabel(_dataB,True)
    #_dataA = normalize(_dataA+_dataB)
    #_dataB = normalize(_dataB)
    randomiceData([_dataA,_dataB])
    _dataA,_dataB = normalize(_dataA,_dataB)
    _training,_test = calcProportion(.8)
    if not _csv:
        print "Data: %s" % (_file_path)
        print "     class 0 available data: %i" %(len(_dataA))
        print "     class 1 available data: %i" %(len(_dataB))
        print ""
        print "     Training elements: %i" %(_training)
        print "     Test elements: %i" %(_test)
    _rLinear = []
    _pLinear = []
    _rRbf = []
    _pRbf = []
    _rPoly = []
    _pPoly = []
    for _runs in range(1,100):
        for i, kernel in enumerate(['linear','rbf','poly']):
             ##individual kernel
            clf = svm.SVC(kernel=kernel)
            X,y = takeSample(_training)
            Z = clf.fit(X,y)
            _X,_y = takeSample(_test,_training)
            y_pred = clf.predict(_X)
            saveSet(X+_X,y+_y)
            cm = confusion_matrix(_y, y_pred)
            _p = precision_score(_y,y_pred)*100
            _r = recall_score(_y,y_pred) *100
            if not _csv:
                print "\n=====KERNEL: %s=====" %(kernel)
                print cm
                print "Precision: %f" %(_p)
                print "Recall: %f" %(_r)

            if( kernel == 'linear'):
                _rLinear.append(_r)
                _pLinear.append(_p)
            if( kernel == 'rbf'):
                _rRbf.append(_r)
                _pRbf.append(_p)
            if( kernel == 'poly'):
                _rPoly.append(_r)
                _pPoly.append(_p)
    if not _csv:
        print ""
        print "LINEAR P:",np.average(_pLinear)
        print "LINEAR R:",np.average(_rLinear)
        print "RBF P:",np.average(_pRbf)
        print "RBF R:",np.average(_rRbf)
        print "POLY P:",np.average(_pPoly)
        print "POLY R:",np.average(_rPoly)
    else:
        print "%.2f" % np.average(_pLinear),",","%.2f"%np.average(_rLinear),",","%.2f"%np.average(_pRbf),",","%.2f"%np.average(_rRbf),",","%.2f"%np.average(_pPoly),",","%.2f"%np.average(_rPoly)+","+str(_training)+","+str(_test)
            #print "----CROSS-VALIDATION--"
            #clf = svm.SVC(kernel=kernel)
            #X,y = takeSample(_training+_test)
            #validateVector(X)
            #X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.5, random_state=0)
            #Z = clf.fit(X_train,y_test)
            #y_pred = clf.predict(X_test)
            #scores = cross_validation.cross_val_score(clf, X, y, cv=5)
            #print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
            #plot(_X,_y,clf)
            #if(_p < 60.0 and kernel =='poly'):
            #  print "Precision decayed below 60.0 after %i runs" %(_runs)
            #    break

