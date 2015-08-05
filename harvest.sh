rm p*.csv
rm p*_???.csv
rm results.csv
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
echo "SUBJECT,SIGNAL,PRECISION,RECALL,PRECISION,RECALL,PRECISION,RECALL,TRAINING_SAMPLES,TEST_SAMPLES" > results.csv
python classify.py p1.csv >> results.csv csv
python classify.py p1_gsr.csv >> results.csv csv
python classify.py p1_ibi.csv >> results.csv csv
python classify.py p6.csv >> results.csv csv
python classify.py p6_gsr.csv >> results.csv csv
python classify.py p6_ibi.csv >> results.csv csv
python classify.py p7.csv >> results.csv csv
python classify.py p7_gsr.csv >> results.csv csv
python classify.py p7_ibi.csv >> results.csv csv
python classify.py p9.csv >> results.csv csv
python classify.py p9_gsr.csv >> results.csv csv
python classify.py p9_ibi.csv >> results.csv csv
