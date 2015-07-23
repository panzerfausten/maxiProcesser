import sys
from random import shuffle
with open(sys.argv[1], "r") as _FILE:
    data = []
    for _x in _FILE.readlines():
        data.append(_x)
    shuffle(data)
    with open(sys.argv[2],"w") as _OUTPUT:
        for _l in data:
            _OUTPUT.write(_l)


