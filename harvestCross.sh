rm p*.csv
rm p*_???,csv
rm test.csv
rm training.csv
rm resultsCross.csv
##GET ALL THE DATA
python process.py p1 gsr,ibi > p1.csv
python process.py p6 gsr,ibi > p6.csv
python process.py p7 gsr,ibi > p7.csv
python process.py p9 gsr,ibi > p9.csv

python process.py p1 gsr > p1_gsr.csv
python process.py p6 gsr > p6_gsr.csv
python process.py p7 gsr > p7_gsr.csv
python process.py p9 gsr > p9_gsr.csv

python process.py p1 ibi > p1_ibi.csv
python process.py p6 ibi > p6_ibi.csv
python process.py p7 ibi > p7_ibi.csv
python process.py p9 ibi > p9_ibi.csv
##TEST P1
cat p6.csv > training.csv
cat p7.csv >> training.csv
cat p9.csv >> training.csv
cp p1.csv test.csv
#P6+P7+P9 VS P1, ALL SIGNALS
echo "SUBJECT,SIGNAL,PRECISION,RECALL,PRECISION,RECALL,PRECISION,RECALL,TRAINING_SAMPLES,TEST_SAMPLES" > resultsCross.csv

python classify_files.py training.csv test.csv csv>> resultsCross.csv

#P6+P7+P9 VS P1, GSR
cat p6_gsr.csv > training.csv
cat p7_gsr.csv >> training.csv
cat p9_gsr.csv >> training.csv
cp p1_gsr.csv test.csv
python classify_files.py training.csv test.csv csv >> resultsCross.csv

#P6+P7+P9 VS P1, IBI
cat p6_ibi.csv > training.csv
cat p7_ibi.csv >> training.csv
cat p9_ibi.csv >> training.csv
cp p1_ibi.csv test.csv
python classify_files.py training.csv test.csv csv >> resultsCross.csv

##TEST P6
cat p1.csv > training.csv
cat p7.csv >> training.csv
cat p9.csv >> training.csv
cp p6.csv test.csv
#P1+P7+P9 VS P6, ALL SIGNALS
python classify_files.py training.csv test.csv csv>> resultsCross.csv

#P1+P7+P9 VS P6, GSR
cat p1_gsr.csv > training.csv
cat p7_gsr.csv >> training.csv
cat p9_gsr.csv >> training.csv
cp p6_gsr.csv test.csv
python classify_files.py training.csv test.csv csv >> resultsCross.csv

#P1+P7+P9 VS P6, IBI
cat p1_ibi.csv > training.csv
cat p7_ibi.csv >> training.csv
cat p9_ibi.csv >> training.csv
cp p6_ibi.csv test.csv
python classify_files.py training.csv test.csv csv >> resultsCross.csv


##TEST P7
cat p1.csv > training.csv
cat p6.csv >> training.csv
cat p9.csv >> training.csv
cp p7.csv test.csv
#P1+P6+P9 VS P7, ALL SIGNALS
python classify_files.py training.csv test.csv csv>> resultsCross.csv

#P1+P6+P9 VS P7, GSR
cat p1_gsr.csv > training.csv
cat p6_gsr.csv >> training.csv
cat p9_gsr.csv >> training.csv
cp p7_gsr.csv test.csv
python classify_files.py training.csv test.csv csv >> resultsCross.csv

#P1+P7+P9 VS P6, IBI
cat p1_ibi.csv > training.csv
cat p6_ibi.csv >> training.csv
cat p9_ibi.csv >> training.csv
cp p7_ibi.csv test.csv
python classify_files.py training.csv test.csv csv >> resultsCross.csv


##TEST P9
cat p1.csv > training.csv
cat p6.csv >> training.csv
cat p7.csv >> training.csv
cp p9.csv test.csv
#P1+P6+P9 VS P7, ALL SIGNALS
python classify_files.py training.csv test.csv csv>> resultsCross.csv

#P1+P6+P9 VS P7, GSR
cat p1_gsr.csv > training.csv
cat p6_gsr.csv >> training.csv
cat p7_gsr.csv >> training.csv
cp p9_gsr.csv test.csv
python classify_files.py training.csv test.csv csv >> resultsCross.csv

#P1+P7+P9 VS P6, IBI
cat p1_ibi.csv > training.csv
cat p6_ibi.csv >> training.csv
cat p7_ibi.csv >> training.csv
cp p9_ibi.csv test.csv
python classify_files.py training.csv test.csv csv >> resultsCross.csv

