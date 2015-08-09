##GET ALL THE DATA
python process.py p1 gsr,ibi > p1.csv
python process.py p6 gsr,ibi > p6.csv
#python process.py p7 gsr,ibi > p7.csv
python process.py p9 gsr,ibi > p9.csv


cat p1.csv > training.csv
cat p6.csv >> training.csv
#cat p7.csv >> training.csv
cat p9.csv >> training.csv

python process.py p7s2 gsr,ibi -fs > fs.csv
python classifySession.py training.csv fs.csv csv > fs_results.csv
python plotApp.py fs_results.csv ; 
convert -append plotSR.png app.png prediction.png
gwenview prediction.png
