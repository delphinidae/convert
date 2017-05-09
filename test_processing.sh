success_msg="\033[0;32mStatus OK\033[0m"
fail_msg="\033[0;31mTest faild!\033[0m"
fail()
{
    echo -en $fail_msg
    echo
    exit 1
}
func()
{
    echo "Running convert with $1 as input"
    if $2 eq "true"; then
        if python3 convert.py -i input_tests/$1 -o output; then
            echo -en $success_msg
        else
            fail
        fi
    else
        if python3 convert.py -i input_tests/$1 -o output; then
            fail
        else
            echo -en $success_msg
        fi
    fi
    echo
    echo
}
echo "Testing file processing"
#Positive cases
echo "Cyrillic symbols"
func input true
echo "Different number of filled columns"
func input1 true
echo "First column is empty, but still exists"
func input2a true

#Negative cases
echo "No columns"
func input2 false
echo "Empty file"
func input3 false
echo "Wrong number of columns"
func input4 false
echo "Wrong number of columns"
func input5 false
echo "Value is not a number"
func input6 false
echo "Columns names are not unique"
func input7 false
echo "No such file"
func input8 false


