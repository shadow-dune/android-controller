# android-controller
Welcome to my first github project!

This is a python script to control android devices (phones/TVs) using adb over LAN.

## The prerequisites are:
1) ADB has to be installed on the host device. [tutorial](https://www.xda-developers.com/install-adb-windows-macos-linux/)

2) Wireless debugging has to be enabled on the device being controlled.
   - On android phones or TVs, go to developer options and enable usb/wireless debugging
   - On Fire TVs, go to settings -> developer options -> turn on adb debugging

3) Python will also have to be installed on the host device. [download page](https://www.python.org/downloads/)

## How to use:
1) Find out the ip address of the device being controlled using any app of your choice (example: https://angryip.org/). Note that the ip address can change from time to time

2) Download the python file, open it, and change the two variables declared in the beginning

3) Run the file with python. Supported commands are declared in class remote -> commandValues

## Uses:
1) This program can be integrated with other python projects to increase its functionality
2) It is a simple way to control Android TVs from any platform
