from sklearn import svm
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
    _X =   _dataA[_s:_maxSample+_s] + _dataB[_s:_maxSample+_s] + _dataC[_s:_maxSample+_s] + _dataD[_s:_maxSample+_s]
    _y =   [0]*_maxSample +[1]*_maxSample + [2]*_maxSample + [3]*_maxSample
    return _X,_y
if __name__ == "__main__":
    _file_path = sys.argv[1]
    _dataA,_dataB,_dataC,_dataD  = readFile(_file_path)
    print "Data: %s" % (_file_path)
    print "     class 0 available data: %i" %(len(_dataA))
    print "     class 1 available data: %i" %(len(_dataB))
    print "     class 2 available data: %i" %(len(_dataC))
    print "     class 3 available data: %i" %(len(_dataD))
    print "     Taking sample of: %i" %(12)
    clf = svm.SVC(kernel='linear')
    X,y = takeSample(5)
    _X,_y = takeSample(4,5)
    clf.fit(X,y)
    y_pred = clf.predict(_X)
    cm = confusion_matrix(_y, y_pred)
    print cm
    print "Precision: %f" %(precision_score(_y,y_pred)*100)
    print "Recall: %f" %(recall_score(_y,y_pred) *100)

   
