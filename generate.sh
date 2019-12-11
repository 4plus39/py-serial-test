# pyinstaller -F [xxx.py]
sudo pyinstaller -F main.py
sudo pyinstaller -F mainui.py

cd ./dist

# staticx [input file] [output file]
staticx main ../sptc
staticx mainui ../sptu

exit 0
