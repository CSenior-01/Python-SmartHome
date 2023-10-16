# Caitlin Senior
# Python Smart Home - frontend

from backend import *
from tkinter import *

mainWin = Tk()
home = SmartHome()

def setUpHome():
    """Sets up the list of devices in the smart home"""
    homeDevices = [SmartHeater(), SmartHeater(), SmartHeater(), SmartPlug(), SmartPlug()]
    for i in range(len(homeDevices)):
        home.addDevice(homeDevices[i])

def setUpMainWin():
    """Sets up the main window of the smart home GUI"""
    mainWin.title("Smart Home")
    devicesNum = len(home.devices)
    height = 50 * (devicesNum + 2)
    mainWin.geometry("600x{}".format(height))
    mainWin.resizable(False, False)

    mainWin.columnconfigure(index=0, weight=4)

    showDevices()

    mainWin.mainloop()

def showDevices():
    """Sets up the devices of the GUI"""
    devicesNum = len(home.devices)

    def turnAllOff():
        home.turnOffAll()
        updateLabels()

    def turnAllOn():
        home.turnOnAll()
        updateLabels()

    turnAllOffBtn = Button(mainWin, text="Turn all off", command=turnAllOff)
    turnAllOffBtn.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    turnAllOnBtn = Button(mainWin, text="Turn all on", command=turnAllOn)
    turnAllOnBtn.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    for deviceIndex in range(devicesNum):
        smartDevice = home.getDevicesAt(deviceIndex)

        deviceTxt = Text(mainWin, height=2, width=50)
        deviceTxt.insert("1.0", str(smartDevice))
        deviceTxt.grid(row=deviceIndex + 3, column=0, padx=10, pady=5)

        def updateLabels():
            showDevices()

        def toggleThis(i=deviceIndex):
            home.toggleSwitch(i)
            updateLabels()

        def devicesOn(i = deviceIndex):
            numDevicesOn = 0
            gettingDevice = home.getDevicesAt(i)
            onStatus = gettingDevice.getSwitch()
            for device in range(len(home.devices)):
                if onStatus == True:
                    numDevicesOn += 1
                else:
                    pass
            return numDevicesOn

        def modifyThis(i = deviceIndex):
            modifyWindow(i)

        toggleBtn = Button(mainWin, text="Toggle This", command=toggleThis)
        toggleBtn.grid(row=deviceIndex + 3, column=2, padx=10, pady=5)

        configBtn = Button(mainWin, text="Modify", command=modifyThis)
        configBtn.grid(row=deviceIndex + 3, column=1, padx=10, pady=5)

        devicesOn = Label(mainWin, text="Total devices on: {}".format(devicesOn()), height=2, width=50)
        devicesOn.grid(row=deviceIndex + 4, column=0, padx=10, pady=5, sticky="w")

def modifyWindow(deviceIndex):
    """Opens an additional window to modify the devices"""

    modifyWin = Toplevel(mainWin)
    modifyWin.geometry("400x150")
    modifyWin.resizable(False, False)

    deviceName = home.getDevicesAt(deviceIndex)
    deviceClass = deviceName.__class__.__name__

    modifyWin.title("Modify {}".format(deviceClass))

    infoTxt = Text(modifyWin, height=2, width=45)

    if deviceClass == "SmartHeater":
        infoTxt.insert("1.0", "Modify your Smart Heater")
        settingHeaterLabel = Label(modifyWin, text="Change the heater setting:")
        settingHeaterLabel.grid(row=1, column=0, padx=10, pady=10)

        settingEntry = Entry(modifyWin)
        settingEntry.insert(0, str(deviceName.getSetting()))
        settingEntry.grid(row=1, column=1, padx=10, pady=10)

        def submitCmd():
            newSetting = int(settingEntry.get())
            deviceName.changeSetting(newSetting)
            showDevices()
            modifyWin.destroy()

        submitBtn = Button(modifyWin, text="Submit", command=submitCmd)
        submitBtn.grid(row=2, column=1, padx=10, pady=2)

    elif deviceClass == "SmartPlug":
        infoTxt.insert("1.0", "Modify your Smart Plug")
        settingConsumptionLabel = Label(modifyWin, text="Change the consumption rate:")
        settingConsumptionLabel.grid(row=1, column=0, padx=10, pady=10)

        consumptionEntry = Entry(modifyWin)
        consumptionEntry.insert(0, str(deviceName.getConsumption()))
        consumptionEntry.grid(row=1, column=1, padx=10, pady=10)

        def submitCmd():
            newConsumption = int(consumptionEntry.get())
            deviceName.setConsumption(newConsumption)
            showDevices()
            modifyWin.destroy()

        confirmBtn = Button(modifyWin, text="Confirm", command=submitCmd)
        confirmBtn.grid(row=2, column=1, padx=10, pady=2)

    infoTxt.grid(row=0, column=0, padx=15, pady=5, columnspan=2)

    cancelBtn = Button(modifyWin, text="Cancel", command=modifyWin.destroy)
    cancelBtn.grid(row=2, column=0, padx=10, pady=10)

    modifyWin.mainloop()

def main():
    """Runs the main functions"""
    setUpHome()
    setUpMainWin()

main()
