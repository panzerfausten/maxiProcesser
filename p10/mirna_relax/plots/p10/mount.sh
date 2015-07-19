GSR=$(find . | grep HTR)
HR=$(find . | grep HR)
IBI=$(find . | grep IBI)
TEMP=$(find . | grep TEMP)
convert +append $GSR $HR $IBI $TEMP 1.png
