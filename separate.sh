cat data.csv | grep "^0," > 0.csv
cat data.csv | grep "^1," > 1.csv
kwrite 0.csv &
kwrite 1.csv &

cat optimalSet.csv | grep "^0," > 0_o.csv
cat optimalSet.csv | grep "^1," > 1_o.csv
kwrite 0_o.csv &
kwrite 1_o.csv &
