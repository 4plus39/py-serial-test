# pyinstaller -F [xxx.py]
sudo pyinstaller -F main.py
sudo pyinstaller -F mainui.py

cd ./dist

# staticx [input file] [output file]
staticx main ../sp-test
staticx mainui ../sp-testui

exit 0
