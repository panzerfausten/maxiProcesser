from datetime import datetime
import traceback
import time
import sys
class SelfReport:
    def __init__(self,_tsvFile,_srFile,_h):
        self._tsvFile = _tsvFile   
        self._srFile = _srFile   
        self._h = _h
        with open(self._tsvFile,"r") as _file:
            _lines = _file.readlines()
            self._data = self.cleanData(_lines)

        with open(self._srFile,"r") as _file:
            _lines = _file.readlines()
            self._srData = self.cleanSrData(_lines)

        self._startTime = datetime.fromtimestamp(self._data[0][0]) #THIS STARTTIME IS TRANSCRIPT START TIME. NOT SESSION STARTIME
    def generateSelfReportFile(self):
        _xData = []
        _mData = []
        for _sr in self._srData:
            _h,_m  = self.getHM(_sr[0])
            _srTime = self._startTime.replace(hour=_h,minute=_m)
            _srTime = time.mktime(_srTime.timetuple())
            _x = self.findDataInTime(float(_srTime))
            if(_x != None):
                _xData.append([_x,_sr[1]])
            else:
                pass#$_mData.append([None,_)
        for _x,_sr in enumerate(self._data):
            if(len (_xData) > 0):
                if(_x == _xData[0][0]):
                    self.printLine(_sr,_xData[0][1])
                    _xData.pop(0)
                else:
                    self.printLine(_sr)
            else:
                self.printLine(_sr)


    def printLine(self,_oLine,_level=None):
        if(self._h):
            _oLine[0] =  self.toHTime(_oLine[0])
        if(_level !=None):
            print "\t".join(map(str, _oLine))+ "\t%s" %(_level)
        else:
            print "\t".join(map(str, _oLine))+ "\t"
    def toHTime(self,_time):
        _hTime = datetime.fromtimestamp(_time)
        return str(_hTime.hour) + ":" + str(_hTime.minute) + ":" + str(_hTime.second)
    def findDataInTime(self,_time):
        _time = datetime.fromtimestamp(_time)
        _time = _time.replace(second=0)
        for _x,_d in enumerate(self._data):
            _filetime = datetime.fromtimestamp(float(_d[0]))
            _ts = (_filetime - _time).total_seconds()
            if (_ts > 0 and _ts < 30):
                return _x
    def getHM(self,_time):
        return int(_time.split(":")[0]), int(_time.split(":")[1])
    def cleanData(self,_lines):
        _cData = []
        for _l in _lines:
            _l = _l.replace("\n","").split("\t")
            _l[0] = float(_l[0])
            #_l[2] = int(_l[2])
            _cData.append(_l)
        return _cData

    def cleanSrData(self,_lines):
        _cData = []
        for _l in _lines:
            _l = _l.replace("\n","").split("\t")
            _l[0] = str(_l[0]) #TODO:change to secs or something, this is the delta
            _l[1] = str(_l[1])
            _cData.append(_l)
        return _cData
def usage():
    print "USAGE:"
    print "     python SelfReport.py <INPUT_TSV_FILE> <INPUT_SELFREPORT_FILE> [-h]"
if __name__ == "__main__":
    try:
        _input_tsv_file = sys.argv[1]
        _input_sr_file = sys.argv[2]
        _h_flag = False
        try:
            _h_flag = sys.argv[3]
        except:
            pass
        if (_h_flag == "-h"):
            _h_flag
        _sr = SelfReport(_input_tsv_file,_input_sr_file,_h=_h_flag)
        _sr.generateSelfReportFile()
    except Exception as e:
        usage()
        traceback.print_exc()
