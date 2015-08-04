cat data.csv | grep "^0," > 0.csv
cat data.csv | grep "^1," > 1.csv
cat data.csv | grep "^-1," > 1_.csv
cat data.csv | wc -l
cat 0.csv | wc -l
cat 1.csv | wc -l
cat 1_.csv | wc -l
