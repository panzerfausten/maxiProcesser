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
            elif (_lineF[0] == -3):
                _dataC.append(_lineF)
            elif (_lineF[0] == 3):
                _dataD.append(_lineF)
        return _dataA,_dataB,_dataC
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

def takeTest():
    #at this point, the samples are sorted
    _nm_A =    _data_t_A
    _nm_B = _data_t_B
    _X = []
    for _x, _nm in enumerate(_nm_A):
        _X.append(_nm.tolist())
    for _x, _nm in enumerate(_nm_B):
        _X.append(_nm.tolist())
    _y =    [0]*len(_nm_A) + [1]*len(_nm_B)
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
def normalize(_dataToNorm):
    x = np.array(_dataToNorm)
    return preprocessing.scale(x)

    return _resA,_resB,_resC
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
    _file_path = sys.argv[1] #training
    _csv = False
    try:
        _testFile = sys.argv[2]
        _csvRequest = sys.argv[3]
        if("csv" in _csvRequest):
            _csv = True
    except:
            pass
    _dataA,_dataB,_dataC  = readFile(_file_path)
    _data_t_A,_data_t_B,_data_t_C  = readFile(_testFile)
    _dataA = removeLabel(_dataA,True)
    _dataB = removeLabel(_dataB,True)
    _dataC = removeLabel(_dataC,True)
    _data_t_A = removeLabel(_data_t_A,True)
    _data_t_B = removeLabel(_data_t_B,True)
    _data_t_C = removeLabel(_data_t_C,True)
    _dataA = normalize(_dataA)
    _dataB = normalize(_dataB)
    _dataC = normalize(_dataC)
    _data_t_A = normalize(_data_t_A)
    _data_t_B = normalize(_data_t_B)
    _data_t_C = normalize(_data_t_C)

 
    _training,_test = calcProportion(1.0) #take all for training, ignore _test for now

    if(len(_data_t_A) < len(_data_t_B)):
        _test = len(_data_t_A)
    else:
        _test = len(_data_t_B)
    if not _csv:
        print "Data: %s" % (_file_path)
        print "     class 0 available data: %i" %(len(_dataA)+ len(_data_t_A))
        print "     class 1 available data: %i" %(len(_dataB)+ len(_data_t_B))
        print ""
        print "     Training elements: %i" %(_training)
        print "     Test elements: %i" %( len(_dataC))
    _rLinear = []
    _pLinear = []
    _rRbf = []
    _pRbf = []
    _rPoly = []
    _pPoly = []
    for _runs in range(1,2):
        for i, kernel in enumerate(['rbf']):
            clf = svm.SVC(kernel=kernel)
            X,y = takeSample(_training)
            Z = clf.fit(X,y)
            for _x,_sample in enumerate(_data_t_C):
                print str(_x),",",clf.predict(_sample)[0]
