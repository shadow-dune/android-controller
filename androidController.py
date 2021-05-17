# This is a project to control android devices using python and adb.

import subprocess


# ENTER IP ADDRESS HERE
DEVICE_IP = ''

# ENTER THE DIRECTORY IN WHICH ADB IS INSTALLED HERE
ADB_LOCATION = ''


# variable to store the string inputted by the user
text = ''


class remote:
    # ip address of the device
    ipAddress = ''

    # directory in which adb is saved on the host
    directory = ''

    # dictionary to store adb values to run a command
    commandValues = {
        'up': '19',
        'down': '20',
        'left': '21',
        'right': '22',
        'back': '4',
        'ok': '23',
        'home': '3'
    }

    # create a list of all the commands
    commandValuesKeys = list(commandValues.keys())

    # constructor function
    def __init__(self, a, b):
        self.ipAddress = a
        self.directory = b

    # connect to adb device
    def connectToDevice(self):
        # connect to the adb device
        subprocess.Popen('adb connect ' + self.ipAddress,
                         shell=True, cwd=self.directory)

    # function to get values from the dictionary
    def getcommandValues(self, a):
        return self.commandValues.get(a)

    def sendCommand(self, a):
        # run the command in shell
        subprocess.Popen('adb shell input keyevent ' + a,
                         shell=True, cwd=self.directory)


# create a new object
remote1 = remote(DEVICE_IP, ADB_LOCATION)
# connect to adb device
remote1.connectToDevice()
print('Type a command to control your device')

# unless 'exit' is typed, run the loop
while text != 'exit':
    # get user input and store it in the variable 'text'
    text = input()
    # try and except block to send the adb command for the required action
    try:
        remote1.sendCommand(remote1.getcommandValues(text))
    except:
        print('error')
