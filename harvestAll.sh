echo "SUBJECT,SIGNAL,PRECISION,RECALL,PRECISION,RECALL,PRECISION,RECALL,TRAINING_SAMPLES,TEST_SAMPLES" > resultsAll.csv
python process.py all gsr,ibi >  data.csv
python classify.py data.csv csv >> resultsAll.csv

python process.py all gsr >  data.csv
python classify.py data.csv csv >> resultsAll.csv

python process.py all ibi >  data.csv
python classify.py data.csv csv >> resultsAll.csv
