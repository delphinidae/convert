success_msg="\033[0;32mStatus OK\033[0m"
fail_msg="\033[0;31mTest faild!\033[0m"
fail()
{
    echo -en $fail_msg
    echo
    exit 1
}
call()
{
    if $3 eq "true"; then
        if python3 convert.py -i input -o output -m $1 -c $2; then
            echo -en $success_msg
        else
            fail
        fi
    else 
        if python3 convert.py -i input -o output -m $1 -c $2; then
            fail
        else
            echo -en $success_msg
        fi
    fi
    echo
    echo
}

echo "Testing module loading"

#Positive cases
ls > input #TODO there coud be such file already 
echo "Plugin is in the same directory"
call json_plugin.py JsonLine true
mkdir temp_dir
cp json_plugin.py temp_dir/.
echo "Plugin is in different directory"
call temp_dir/json_plugin.py JsonLine true
rm -rf temp_dir

#Negative cases
echo "Wrong module name, file doesn't exist"
call json_plugin JsonLine false
echo "File exists, but not a python file"
ls > temp.py
call temp.py JsonLine false
rm temp.py
echo "Wrong class name"
call json_plugin.py Jsonl false
rm input
