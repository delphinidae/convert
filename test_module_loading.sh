call()
{
if python3 convert.py -i input -o output -m $1 -c $2; then
echo "Status OK"
fi
echo
}

echo "Testing module loading"

#Positive cases
echo "Plugin is in the same directory"
call json_plugin.py JsonLine
mkdir temp_dir
cp json_plugin.py temp_dir/.
echo "Plugin is in different directory"
call temp_dir/json_plugin.py JsonLine
rm -rf temp_dir

#Negative cases
echo "Wrong module name, file doesn't exist"
call json_plugin JsonLine
echo "File exists, but not a python file"
ls > temp.py
call temp.py JsonLine
rm temp.py
echo "Wrong class name"
call json_plugin.py Jsonl
