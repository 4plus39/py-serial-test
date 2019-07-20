echo -n "Input your main python file name: "
read pyfile
echo -n "Input your output file name: "
read exefile

# pyinstaller -F [xxx.py]
sudo pyinstaller -F $pyfile

cd ./dist

# staticx [input file] [output file]
staticx ${pyfile/'.py'/} ../$exefile

exit 0
