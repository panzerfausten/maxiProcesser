from sklearn import svm
from random import shuffle
import sys
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
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
        return _dataA,_dataB,_dataC,_dataD
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
    _X =    _dataA[_s:_maxSample+_s] +  _dataB[_s:_maxSample+_s] + _dataC[_s:_maxSample+_s] + _dataD[_s:_maxSample+_s]
    _y =    [0]*_maxSample + [1]*_maxSample + [2]*_maxSample + [3]*_maxSample
    return _X,_y

def takeSampleFrom(_source,_maxSample,_s=0,):
    if(_source ==0):
        _X =    _dataA[_s:_maxSample+_s]
        _y =   [0]*_maxSample
        return _X,_y
    if(_source ==1):
        _X =    _dataB[_s:_maxSample+_s]
        _y =   [1]*_maxSample
        return _X,_y
    if(_source ==2):
        _X =    _dataC[_s:_maxSample+_s]
        _y =   [2]*_maxSample
        return _X,_y
    if(_source ==3):
        _X =    _dataD[_s:_maxSample+_s]
        _y =   [3]*_maxSample
        return _X,_y
def plot(_X,_y,_clf):
    _X = np.array(_X)
    plt.scatter(_X[:,2],_X[:,3],c =_y)
    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(0,12)
    yy = a * xx - clf.intercept_[0] / w[1]
    h0 = plt.plot(xx, yy, 'k-', label="non weighted div")
    plt.savefig("svm")
def randomiceData(data):
        for d in data:
                shuffle(d)
if __name__ == "__main__":
    _file_path = sys.argv[1]
    _dataA,_dataB,_dataC,_dataD  = readFile(_file_path)
    randomiceData([_dataA,_dataB,_dataC,_dataD])
    print "Data: %s" % (_file_path)
    print "     class 0 available data: %i" %(len(_dataA))
    print "     class 1 available data: %i" %(len(_dataB))
    print "     class 2 available data: %i" %(len(_dataC))
    print "     class 3 available data: %i" %(len(_dataD))
    print ""
    print "     Training elements: %i" %(20)
    print "     Test elements: %i" %(20)
    for i, kernel in enumerate(['linear','rbf','poly']):
        clf = svm.SVC(kernel=kernel)
        X,y = takeSample(20)
        _X,_y = takeSample(20,20)
        Z = clf.fit(X,y)
        y_pred = clf.predict(_X)
        cm = confusion_matrix(_y, y_pred)
        print "\n=====KERNEL: %s=====" %(kernel)
        print cm
        print "Precision: %f" %(precision_score(_y,y_pred)*100)
        print "Recall: %f" %(recall_score(_y,y_pred) *100)
    #plot(_X,_y,clf)
