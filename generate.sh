# pyinstaller -F [xxx.py]
sudo pyinstaller -F main.py
sudo pyinstaller -F mainui.py

cd ./dist

# staticx [input file] [output file]
staticx main ../test
staticx mainui ../testgui

exit 0
