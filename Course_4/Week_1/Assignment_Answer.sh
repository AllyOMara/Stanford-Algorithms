python Assignment_1_Test.py
passed_test=$?
if [ $passed_test -eq 0 ]
then
python Week_1_Assignment.py g1.txt
python Week_1_Assignment.py g2.txt
python Week_1_Assignment.py g3.txt
fi
