# SerialPort-test-3
Tx/Rx test tool for transmitting signal from system under test serial port to modem continuously.

## Environment
language: Python 3.6.7

#### os
* Ubuntu 18.04(gnome)
* Manjaro 18.04(gnome)
* windows server 2012R2
* windows server 2016

## Requirement
Use the package manager pip to install pyserial.

    pip install pyserial
    pip install keyboard
Use the package manager apt to install tkinter.

    sudo apt-get install python3-tk

## execution
### Text mode
    sudo python main.py

### GUI mode
    sudo python mainUI.py

## Image
### Text mode
![](./images/text_first.png)

![](./images/text_second.png)

![](./images/text_third.png)
### GUI mode
![](./images/start.png)
![](./images/select.png)
![](./images/failed.png)
![](./images/pass.png)

