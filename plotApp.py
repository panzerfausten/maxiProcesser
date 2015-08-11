import numpy as np
import pylab as plt
import sys
from maxi import session
def getSessions(_s):
    _sessionsRtr = []
    if(_s == "all"):
        s = session("p1/carlos_S1_R1/1433807211979/")
        _sessionsRtr.append(s)
        s = session("p1/carlos_relax3/1435362269780/")
        _sessionsRtr.append(s)
        s = session("p6/luis_relax/1433979780288/")
        _sessionsRtr.append(s)
        s = session("p6/luismiguel_relax2/1434671046538/")
        _sessionsRtr.append(s)
        s = session("p6/luis_relax3/1435273024530/")
        _sessionsRtr.append(s)
        s = session("p7/alfonso_relax/1434064078558/")
        _sessionsRtr.append(s)
        s = session("p7/alfonso_relax2/1434495734670/")
        _sessionsRtr.append(s)
        s = session("p7/alfonso_relax3/1435275565320/")
        _sessionsRtr.append(s)
        s = session("p8/angello_relax/1434066549276/")
        _sessionsRtr.append(s)
        s = session("p8/angello_relax2/1434668094145/")
        _sessionsRtr.append(s)
        s = session("p8/angello_relax3/1435708008150/")
        _sessionsRtr.append(s)
        s = session("p9/sandra_relax/1434150573545/")
        _sessionsRtr.append(s)
        s = session("p9/sandra_relax3/1435619278734/")
        _sessionsRtr.append(s)
    if(_s == "p1"):
        s = session("p1/carlos_S1_R1/1433807211979/")
        _sessionsRtr.append(s)
        s = session("p1/carlos_relax3/1435362269780/")
        _sessionsRtr.append(s)
    if(_s == "p1s1"):
        s = session("p1/carlos_S1_R1/1433807211979/")
        _sessionsRtr.append(s)
    if(_s == "p1s3"):
        s = session("p1/carlos_relax3/1435362269780/")
        _sessionsRtr.append(s)
    if(_s == "p6"):
        s = session("p6/luis_relax/1433979780288/")
        _sessionsRtr.append(s)
        s = session("p6/luismiguel_relax2/1434671046538/")
        _sessionsRtr.append(s)
        s = session("p6/luis_relax3/1435273024530/")
        _sessionsRtr.append(s)
    if(_s =="p6s1"):
        s = session("p6/luis_relax/1433979780288/")
        _sessionsRtr.append(s)
    if(_s =="p6s2"):
        s = session("p6/luismiguel_relax2/1434671046538/")
        _sessionsRtr.append(s)
    if(_s =="p6s3"):
        s = session("p6/luis_relax3/1435273024530/")
        _sessionsRtr.append(s)
    if(_s == "p7"):
        s = session("p7/alfonso_relax/1434064078558/")
        _sessionsRtr.append(s)
        s = session("p7/alfonso_relax2/1434495734670/")
        _sessionsRtr.append(s)
        s = session("p7/alfonso_relax3/1435275565320/")
        _sessionsRtr.append(s)
    if(_s == "p7s1"):
        s = session("p7/alfonso_relax/1434064078558/")
        _sessionsRtr.append(s)
    if(_s == "p7s2"):
        s = session("p7/alfonso_relax2/1434495734670/")
        _sessionsRtr.append(s)
    if(_s == "p7s3"):
        s = session("p7/alfonso_relax3/1435275565320/")
        _sessionsRtr.append(s)
    if(_s == "p8"):
        s = session("p8/angello_relax/1434066549276/")
        _sessionsRtr.append(s)
        s = session("p8/angello_relax2/1434668094145/")
        _sessionsRtr.append(s)
        s = session("p8/angello_relax3/1435708008150/")
        _sessionsRtr.append(s)
    if(_s == "p8s1"):
        s = session("p8/angello_relax/1434066549276/")
        _sessionsRtr.append(s)
    if(_s == "p8s2"):
        s = session("p8/angello_relax2/1434668094145/")
        _sessionsRtr.append(s)
    if(_s == "p8s3"):
        s = session("p8/angello_relax3/1435708008150/")
        _sessionsRtr.append(s)
    if(_s == "p9"):
        s = session("p9/sandra_relax/1434150573545/")
        _sessionsRtr.append(s)
        s = session("p9/sandra_relax3/1435619278734/")
        _sessionsRtr.append(s)
    if(_s == "p9s1"):
        s = session("p9/sandra_relax/1434150573545/")
        _sessionsRtr.append(s)
    if(_s == "p9s3"):
        s = session("p9/sandra_relax3/1435619278734/")
        _sessionsRtr.append(s)
    return _sessionsRtr
def readFile(_path):
    _lines = []
    with open(_path,"r") as _file:
        _lines = _file.readlines()
    return  cleanFile(_lines)
def erotion(_data):
    _d = []
    _se =[0]*3
#    _se = [0,0,0,0]
    for _x in range(0,len(_data),3):
        _d = []
        if(_x+len(_se) < len(_data)):
            for _z in range(_x,_x+len(_se)):
                _d.append(int(_data[_z][1]))
            #print _d
            #print _se
            #print "------"
            if( _d== _se):
                for _y in range(_x,_x+len(_se)):
                    _data[_y][1] = 0
            else:
                for _y in range(_x,_x+len(_se)):
                    _data[_y][1] = 1

    return _data
def cleanFile(_l):
    _cFile = []
    for _line in _l:
        _lc = _line.replace("\n","")
        _lc = _lc.split(",")
        _cFile.append(_lc)
    return _cFile
def calcTimes(_cf):
    _times = []
    for _c in _cf:
        _t = int(_c[0]) * 30
        _times.append([_t,_t+60,_c[1]])
    return _times
def plot(s,_path,_data,_xTick=200,_xMinorTick=100):
    fig, ax = plt.subplots()
    plt.grid(True)

    #set axis. Nazi axis?
    ax.set_ylabel("uS")
    ax.set_xlabel("Seconds")
    ax.set_title("Predicted Anxiety events")
    # major ticks every 200, minor ticks every 100
    major_ticks = np.arange(0, len(_data)/2*60, _xTick)
    minor_ticks = np.arange(0, len(_data)/2*60, _xMinorTick) 

    ax.set_xticks(major_ticks)      
    ax.set_xticks(minor_ticks, minor=True)
    plt.ylim([0,15])
    plt.xlim([0,1900])
    # and a corresponding grid                                                       
    
    ax.grid(which='both')     

    # or if you want differnet settings for the grids:                               
    ax.grid(which='minor', alpha=0.2)                                   
    ax.grid(which='major', alpha=0.5)
    for _i,_c in enumerate(_data):
        if(int(_c[2]) == 0):
            ax.axvspan(_c[0],_c[1],color="green",alpha=1)
        if(int(_c[2]) == 1):
            ax.axvspan(_c[0],_c[1],color="red",alpha=1)
    _dataGSR = s.groupBySec(s._dataGSR,True,False)
    plt.plot(_dataGSR)
    plt.savefig(_path)

_file_path = sys.argv[1]
_session_sel = sys.argv[2]
print _session_sel
_s = getSessions(_session_sel)
_filter = sys.argv[3]
_fil_erotion = True
_data = readFile(_file_path)
if(_filter == "erosion"):
    _data = erotion(_data)
    plot(_s[0],"app_erosion.png",calcTimes(_data))
else:
    plot(_s[0],"app.png",calcTimes(_data))
#_data = calcTimes(_data) 
