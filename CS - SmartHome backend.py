# Caitlin Senior
# Python Smart Home - backend

class SmartPlug:
    """The settings and functions for the smart plug device"""

    def __init__(self):
        """Initialise the default settings for the smart plug"""
        self.switchedOn = False
        self.consumptionRate = 0

    def toggleSwitch(self, newSwitch):
        """Turning the smart plug switch on or off"""
        if newSwitch == True:
            self.switchedOn = not self.switchedOn
        elif newSwitch == False:
            self.switchedOn = not self.switchedOn

    def getSwitch(self):
        """Return the current state of the smart plug switch"""
        return self.switchedOn

    def getConsumption(self):
        """Return the current consumption rate of the smart plug"""
        return self.consumptionRate

    def setConsumption(self, newConsumption):
        """Setting a new consumption rate for the smart plug"""
        if newConsumption >= 0 and newConsumption <= 150:
            self.consumptionRate = newConsumption
            return True
        else:
            print("Value must be between 0 and 150!")
            return False

    def __str__(self):
        """Return a formatted string representation of the smart plug"""
        if self.switchedOn == True:
            return "Your Smart Plug is {} and the consumption rate is {}".format("on", self.consumptionRate)
        elif self.switchedOn == False:
            return "Your Smart Plug is {} and the consumption rate is {}".format("off", self.consumptionRate)


class SmartHeater(SmartPlug):
    """The settings and functions for the smart heater device"""

    def __init__(self):
        """Initialise the default settings for the smart heater, inherits from SmartPlug"""
        super().__init__()
        self.setting = 0

    def toggleSwitch(self, newSwitch):
        """Turning the smart heater switch on or off"""
        if newSwitch == True:
            self.switchedOn = not self.switchedOn
        elif newSwitch == False:
            self.switchedOn = not self.switchedOn

    def getSwitch(self):
        """Return the current state of the smart heater switch"""
        return self.switchedOn

    def getSetting(self):
        """Return the current setting of the smart heater"""
        return self.setting

    def changeSetting(self, newSetting):
        """Changing the setting of the smart heater"""
        if newSetting >= 0 and newSetting <= 5:
            self.setting = newSetting
            return True
        else:
            print("Value must be between 0 and 5!")
            return False

    def __str__(self):
        """Return a formatted string representation of the smart heater"""
        if self.switchedOn == True:
            return "Your Smart Heater is {} and the setting is {}".format("on", self.setting)
        elif self.switchedOn == False:
            return "Your Smart Heater is {} and the setting is {}".format("off", self.setting)

class SmartHome:
    """The functions of the smart home to manage and control the devices"""

    def __init__(self):
        """Create an empty list of devices for the smart home"""
        self.devices = []

    def getDevices(self):
        """Return the items stored in the list of devices"""
        return self.devices

    def getDevicesAt(self, index):
        """Take a value and return the device at that index within the device list"""
        return self.devices[index]

    def addDevice(self, device):
        """Add a new device to the list of devices"""
        self.devices.append(device)

    def toggleSwitch(self, index):
        """Turns a specific device in the device list on or off"""
        if index < len(self.devices):
            device = self.devices[index]
            if device.switchedOn == False:
                device.toggleSwitch(True)
                return device.switchedOn
            if device.switchedOn == True:
                device.toggleSwitch(False)
                return device.switchedOn

    def turnOnAll(self):
        """Turns on all devices in the list"""
        for device in self.devices:
            if device.switchedOn == False:
                device.switchedOn = True
            else:
                pass

    def turnOffAll(self):
        """Turns off all devices in the list"""
        for device in self.devices:
            if device.switchedOn == True:
                device.switchedOn = False
            else:
                pass

    def __str__(self):
        """Return a formatted string representation of all the devices in the device list"""
        output = "Current devices: \n"
        for device in self.devices:
            device = str(device)
            output += "{} \n".format(device)
        return output


def testSmartPlug():
    """Tests the functions of the smart plug class"""

    plug = SmartPlug()
    plug.toggleSwitch(True)
    if plug.getSwitch() == True:
        print("The switch is {}".format("on"))
    else:
        print("The switch is {}".format("off"))
    print("The current consumption rate is {}".format(plug.getConsumption()))
    while True:
        if (plug.setConsumption(int(input("What should the new value be? ")))) == False:
            pass
        else:
            print("The current consumption rate is {}".format(plug.getConsumption()))
            print(plug)
            break

# testSmartPlug()

def testDevice():
    """Tests the functions of the smart heater class"""

    heater = SmartHeater()
    heater.toggleSwitch(True)
    if heater.getSwitch() == True:
        print("The switch is {}".format("on"))
    else:
        print("The switch is {}".format("off"))
    print("The current setting is {}".format(heater.getSetting()))
    while True:
        if heater.changeSetting(int(input("What should the new setting be? "))) == False:
            pass
        else:
            print("The current setting is {}".format(heater.getSetting()))
            print(heater)
            break

# testDevice()

def testSmartHome():
    """Tests the functions of the smart home class"""

    home = SmartHome()
    plug1 = SmartPlug()
    plug2 = SmartPlug()
    heater = SmartHeater()
    plug2.toggleSwitch(True)
    plug2.setConsumption(45)
    heater.changeSetting(3)
    home.addDevice(plug1)
    home.addDevice(plug2)
    home.addDevice(heater)
    print(home)
    home.turnOnAll()
    print(home)

# testSmartHome()
