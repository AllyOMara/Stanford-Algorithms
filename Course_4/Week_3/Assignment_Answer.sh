python Assignment_3_Test.py
passed_test=$?
if [ $passed_test -eq 0 ]
then
    echo "Tests passed."
    echo "Collecting answer..."
    python Week_1_Assignment.py g1.txt
else
    echo "Tests failed."
fi