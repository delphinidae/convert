func()
{
echo "Running convert with $1 as input"
if python3 convert.py -i input_tests/$1 -o output; then
echo "Status OK, output file:"
echo
cat output
fi
echo
}
echo "Testing file processing"
#Positive cases
echo "Cyrillic symbols"
func input
echo "Different number of filled columns"
func input1
echo "First column is empty, but still exists"
func input2a

#Negative cases
echo "No columns"
func input2
echo "Empty file"
func input3
echo "Wrong number of columns"
func input4
echo "Wrong number of columns"
func input5
echo "Value is not a number"
func input6
echo "Columns names are not unique"
func input7
echo "No such file"
func input8


